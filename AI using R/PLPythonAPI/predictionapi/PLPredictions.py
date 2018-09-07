import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn
from scipy.stats import poisson, skellam
import statsmodels.api as sm
import statsmodels.formula.api as smf

PLTrainingData = pd.read_csv("D:\Documents\AI project\PremierLeagueTraining.csv")
PLTrainingData = PLTrainingData[['HomeTeam', 'AwayTeam', 'FTHG', 'FTAG']]
PLTrainingData = PLTrainingData.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})

pl_standings = pd.read_csv("D:\Documents\AI project\PL1819Standings.csv")
pl_fixtures = pd.read_csv("D:\Documents\AI project\PL1819Fixtures.csv")

standings_dataframe = pd.DataFrame(pl_standings)
fixtures_dataframe = pd.DataFrame(pl_fixtures)

goal_model_data = pd.concat([PLTrainingData[['HomeTeam', 'AwayTeam', 'HomeGoals']].assign(home=1).rename(
    columns={'HomeTeam': 'team', 'AwayTeam': 'opponent', 'HomeGoals': 'goals'}),
    PLTrainingData[['AwayTeam', 'HomeTeam', 'AwayGoals']].assign(home=0).rename(
        columns={'AwayTeam': 'team', 'HomeTeam': 'opponent', 'AwayGoals': 'goals'})])

poisson_model = smf.glm(formula="goals ~ home + team + opponent", data=goal_model_data,
                        family=sm.families.Poisson()).fit()

def predict_match(homeTeam, awayTeam):
    prediction_matrix = simulate_match(homeTeam=homeTeam, awayTeam=awayTeam)

    print(prediction_matrix)

    prediction = {
        "homeTeam": homeTeam,
        "awayTeam": awayTeam,
        "mostProbableScore": get_n_probable_score(prediction_matrix, 1),
        "secondMostProbableScore": get_n_probable_score(prediction_matrix, 2),
        "thirdMostProbableScore": get_n_probable_score(prediction_matrix, 3),
    }

    return prediction


def simulate_match(homeTeam, awayTeam):
    max_goals = 4
    home_goals_avg = poisson_model.predict(pd.DataFrame(data={'team': homeTeam,
                                                              'opponent': awayTeam, 'home': 1},
                                                        index=[1])).values[0]
    away_goals_avg = poisson_model.predict(pd.DataFrame(data={'team': awayTeam,
                                                              'opponent': homeTeam, 'home': 0},
                                                        index=[1])).values[0]
    team_pred = [[poisson.pmf(i, team_avg) for i in range(0, max_goals + 1)] for team_avg in
                 [home_goals_avg, away_goals_avg]]
    return (np.outer(np.array(team_pred[0]), np.array(team_pred[1])))


def get_n_probable_score(probablity_matrix, n):
    rows = np.shape(probablity_matrix)[0]
    columns = np.shape(probablity_matrix)[1]

    probablity = np.sort(probablity_matrix.flatten())[-n]

    for i in range(0, rows):
        for j in range(0, columns):
            if probablity_matrix[i, j] == probablity:
                scoreline = {
                    "homeTeamGoals": i,
                    "awayTeamGoals": j
                }
                break
    return scoreline

def get_standings_as_dataframe():
    for key, value in fixtures_dataframe.iterrows():
        update_standings(predict_match(value.HomeTeam, value.AwayTeam))

    return standings_dataframe.sort_values(['P','GD'], ascending=False)

def update_standings(match_result):

    homeTeamRowIndex = standings_dataframe[standings_dataframe['Team'] == match_result["homeTeam"]].index.values.astype(int)[0]
    awayTeamRowIndex = standings_dataframe[standings_dataframe['Team'] == match_result["awayTeam"]].index.values.astype(int)[0]

    # reading

    homeTeamOldData = {
        "homeTeam": match_result["homeTeam"],
        "W": standings_dataframe.at[homeTeamRowIndex, 'W'],
        "D": standings_dataframe.at[homeTeamRowIndex, 'D'],
        "L": standings_dataframe.at[homeTeamRowIndex, 'L'],
        "GF": standings_dataframe.at[homeTeamRowIndex, 'GF'],
        "GA": standings_dataframe.at[homeTeamRowIndex, 'GA'],
    }

    awayTeamOldData = {
        "awayTeam": match_result["awayTeam"],
        "W": standings_dataframe.at[awayTeamRowIndex, 'W'],
        "D": standings_dataframe.at[awayTeamRowIndex, 'D'],
        "L": standings_dataframe.at[awayTeamRowIndex, 'L'],
        "GF": standings_dataframe.at[awayTeamRowIndex, 'GF'],
        "GA": standings_dataframe.at[awayTeamRowIndex, 'GA'],
    }

    # print(homeTeamOldData)
    # print(awayTeamOldData)

    # updating

    homeTeamGoals = match_result.get("mostProbableScore").get("homeTeamGoals")
    awayTeamGoals = match_result.get("mostProbableScore").get("awayTeamGoals")

    standings_dataframe.ix[homeTeamRowIndex, 'GF'] = homeTeamOldData['GF'] + homeTeamGoals
    standings_dataframe.ix[homeTeamRowIndex, 'GA'] = awayTeamOldData['GA'] + awayTeamGoals
    standings_dataframe.ix[awayTeamRowIndex, 'GF'] = awayTeamOldData['GF'] + awayTeamGoals
    standings_dataframe.ix[awayTeamRowIndex, 'GA'] = homeTeamOldData['GA'] + homeTeamGoals

    standings_dataframe.ix[homeTeamRowIndex, 'GD'] = standings_dataframe.at[homeTeamRowIndex, 'GF'] - standings_dataframe.at[homeTeamRowIndex, 'GA']
    standings_dataframe.ix[awayTeamRowIndex, 'GD'] = standings_dataframe.at[awayTeamRowIndex, 'GF'] - standings_dataframe.at[awayTeamRowIndex, 'GA']

    if homeTeamGoals > awayTeamGoals:
        standings_dataframe.ix[homeTeamRowIndex, 'W'] = homeTeamOldData['W'] + 1
        standings_dataframe.ix[awayTeamRowIndex, 'L'] = awayTeamOldData['L'] + 1
    elif awayTeamGoals > homeTeamGoals:
        standings_dataframe.ix[awayTeamRowIndex, 'W'] = awayTeamOldData['W'] + 1
        standings_dataframe.ix[homeTeamRowIndex, 'L'] = homeTeamOldData['L'] + 1
    else:
        standings_dataframe.ix[awayTeamRowIndex, 'D'] = awayTeamOldData['D'] + 1
        standings_dataframe.ix[homeTeamRowIndex, 'D'] = homeTeamOldData['D'] + 1

    standings_dataframe.ix[homeTeamRowIndex, 'P'] = (3 * standings_dataframe.at[homeTeamRowIndex, 'W']) + standings_dataframe.at[homeTeamRowIndex, 'D']
    standings_dataframe.ix[awayTeamRowIndex, 'P'] = (3 * standings_dataframe.at[awayTeamRowIndex, 'W']) + standings_dataframe.at[awayTeamRowIndex, 'D']

    return standings_dataframe


