library(rsample)      # data splitting 
library(gbm)          # basic implementation
library(xgboost)      # a faster implementation of gbm
library(caret)        # an aggregator package for performing many machine learning models
library(h2o)          # a java-based platform
library(pdp)          # model visualization
library(ggplot2)      # model visualization
library(lime)         # model visualization
library(Matrix)

attach(PLTrainingData)
attach(PLTestingData)

gbm.fit <- gbm(
  formula = FTR~.,
  distribution = "gaussian",
  data = PLTrainingData[,c(1,2,5)],
  n.trees = 10000,
  interaction.depth = 1,
  shrinkage = 0.001,
  cv.folds = 5,
  n.cores = NULL, # will use all cores by default
  verbose = FALSE
)

print(gbm.fit)

PLGBMPredictions <- predict(object = gbm.fit, 
                            newdata = PLTestingData,
                            n.trees =gbm.fit$n.trees,
                            type = "link")

print(PLGBMPredictions)
