from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse
from predictionapi import PLPredictions as predict
import pandas as pd

def get_predictions(request):
    response = JsonResponse(predict.predict_match(request.GET.get('homeTeam', 'Man United'), request.GET.get('awayTeam', 'Chelsea')))
    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Credentials'] = 'true'
    response["Access-Control-Allow-Methods"] = "GET,HEAD,OPTIONS,POST,PUT"
    response["Access-Control-Allow-Headers"] = "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers"
    return response

def predict_season(request):

    pl_fixtures_predictions = []

    pl_fixtures = pd.read_csv("D:\Documents\AI project\PL1819Fixtures.csv")

    df = pd.DataFrame(pl_fixtures)
    for key, value in df.iterrows():
        pl_fixtures_predictions.append(predict.predict_match(homeTeam=value.HomeTeam, awayTeam=value.AwayTeam))

    return JsonResponse(pl_fixtures_predictions, safe=False)

def get_standings(request):
    # print(predict.get_standings_as_dataframe()[].to_dict(orient='records'))

    standings = predict.get_standings_as_dataframe()
    standings = standings[['Team','W','D','L','GF','GA','GD','P']]

    standings_dict = standings.to_dict(orient='records')

    print(standings)

    return JsonResponse(standings_dict, safe=False)


