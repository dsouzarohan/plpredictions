#Libraries

library(e1071)
library(naivebayes)

#Premier league data - master, training and testing

PLMasterData <- read.csv(file.choose(), header = TRUE)
PLTrainingData <- read.csv(file.choose(), header = TRUE)
PLTestingData <- read.csv(file.choose(), header = TRUE)
PLTestingData <- PLTestingData[,-3]


PLNaiveBayesModel <- naiveBayes(FTR~., data = PLTrainingData[,c(1,2,5)])
PLPredictions <- predict(PLNaiveBayesModel, PLTestingData)

PLLast20 <- as.character(PLMasterData[6841:6860,"FTR"])
PLPredictions <- as.vector(PLPredictions)

class(PredictionResults)

print(PLPredictions)
print(PLLast20)

PLPredictionResults <- PLLast20 == PLPredictions

print(PLPredictionResults)

summary(PLPredictionResults)