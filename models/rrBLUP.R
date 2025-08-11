library(BGLR)
library(stringr)
library(data.table)
library(dplyr)


rrBLUP <- function(train,test,params){
  
  params <- unlist(params)
  nIter <- params[1]
  burnIn <-  params[2]
  
  data <- rbind(train,test)
  data_qtl <- data.frame(lapply(data[,1:(ncol(data)-1)], as.numeric))
  data_pheno <- data[,ncol(data):ncol(data)]
  
  X <- scale(data_qtl)/sqrt(ncol(data_qtl))
  #X <- X[ , colSums(is.na(X)) == 0]
  X[is.na(X)] <- -1
  y <- as.numeric(unlist(data_pheno))
  
  y_test <- y
  y_test[(nrow(data)-nrow(test)+1):nrow(data)] <- NA
  
  fm <- BGLR(y=y_test,ETA=list(mrk=list(X=X,model='BRR')),
             nIter=nIter,burnIn=burnIn,verbose=FALSE,saveAt='./Result/brr_')
  
  y_predicted <- fm$yHat[(nrow(data)-nrow(test)+1):nrow(data)]
  y_actual <- y[(nrow(data)-nrow(test)+1):nrow(data)]

  pearson <- cor(y_predicted, y_actual, method = c("pearson"))
  MSE <- mean((y_predicted - y_actual)^2)
  
  y_predicted_train <- fm$yHat[1:nrow(train)]
  y_actual_train <- y[1:nrow(train)] 
  
  effect <- data.frame(t(fm[["ETA"]][["mrk"]][["b"]]))

  return(list(pearson,MSE,effect,y_predicted,y_predicted_train))
  
}