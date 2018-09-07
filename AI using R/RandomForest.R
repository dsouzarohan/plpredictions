library(randomForest)

PLForest <- randomForest(FTR~., data = PLTrainingData)

PLForestPredictions <- predict(object = PLForest, newdata = PLTestingData)