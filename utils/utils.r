library(sits)
library(sitsdata)
library(dplyr)
library(ggplot2)
library(ggrepel)
library(tidyverse)
library(plotly)
library(stars)
library(leaflet)
library(stats)
library(dendextend)
library(caret)
library(dplyr)
library(magrittr)
library(readr)
library(keras)
library(randomForest)
library(rpart)
library(rpart.plot)

read_file <- function(file, ext) {
  data.tb <- NULL
  if (ext == "csv") {
    data.tb <- read.csv(file)
  }
  if (ext == "rds") {
    data.tb <- readRDS(file)
  }
  if (ext == "rda") {
    data.tb <- get(load(file))
  }
  return(data.tb)
}

getMode <- function(v) {
   uniqv <- unique(v)
   uniqv[which.max(tabulate(match(v, uniqv)))]
}

getRange <- function(v) {
    return(max(v) - min(v))
}