# Premier league predictions using AI

Our project idea was to make predictions of football matches, so we decided to
predict the English Premier League matches, one of the most followed leagues in the world!
Any prediction model requires a good amount of data to train it and some data to test it. To
train our model, we collected all match data from the last 18 seasons of the English Premier
League. Using this, we made three training data sets. One was with all the 18 seasons, the
second one was based on the last 10 years and the last one was based on the last 5 years.
The reason we have different time periods is due to the fact that many teams have changed
over the past 18 years in terms of their players, managers, style of football, etc. and hence a
relatively small dataset would be more relevant. We used the Poisson distribution as our
model. It is a discrete probability distribution that expresses the probability of a given number
of events occurring in a fixed interval of time or space if these events occur with a known
constant rate and independently of the time since the last event. The model is based on the
number of goals scored or conceded by each team. Teams that have been higher scorers in
the past have a greater chance of scoring goals in the future.
The whole project was implemented using Python. We imported our entire dataset as
a csv file using pandas (a Python package) as a pandas dataframe. Based on our data on
average, the home team scores more goals than the away team. This is where we used the
Poisson Distribution which is, as mentioned above a discrete probability of the number of
events within a specific time period with a known average rate of occurrence. Here the
specific time period is the match period and the average rate of occurrence is the average
number of goals scored by a home team or the away team. The number of goals is
expressed purely as function an average rate of goals. We treat the number of goals scored
by the home and away team as two independent Poisson distributions. For predicting the
score between any two teams the Skellam distribution comes in use. The Skellam
distribution is the difference of two Poisson Distribution.
All of the above functionality was added to a package called PLPredictions which we
imported in our Django app (a Python web framework). We set up specific URLs that
returned data according to the client’s request. In this way we created a Python prediction
API that returns results, a season prediction and final standings depending on the URL the
user goes to. The response would be in JSON which can then be used in any other API or
application.
We predicted the first 30 matches of this season and according to the actual results
17 out of 30 predictions came correct which is a success rate of 56.67%, which is not bad
given the fact that football is a very unpredictable game. In addition to this, we had the
fixtures for the entire season we predicted the results of all the 380 matches. With the help of
all these predicted results we came up with the final League Table Standings. We had
Manchester United as the winner with Chelsea and Arsenal as number two and number
three respectively due to the fact that these teams have been strong performers over the last
18 years which is why they are most likely to win matches against other teams.
The only drawback of this model is that it does not take into account many
parameters that can affect the result of a match. Players, manager, referees, form, league
position, rival opponent, number of goal scored in the first half, tactics, style of football,
weather, etc are just few parameters that affect a match. Obviously implementing a model
with all of these players is beyond the scope of the syllabus but will definitely yield better
predictions.
