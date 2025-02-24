#!/usr/bin/R

# Adapted from https://github.com/JamesStimson/transcluster/blob/master/vignettes/how-to-guide.Rmd

# Start by loading the libraries:
library(transcluster)
library(stats)
library(clue)
library(igraph)

# Then create some data. This is the same as the first example in the paper.
ids <- c('A', 'B', 'C', 'D')
dates <- c(2018, 2014, 2016, 2016)
snpMatrix <- matrix(c(0,5,7,7,5,0,8,8,7,8,0,6,7,8,6,0), nrow=4, ncol=4)

# Set up the model:
myModel <- createModel(ids, dates, snpMatrix)
myModel <- setParams(myModel, lambda=1.5, beta=2.3)
myModel <- setSNPThresholds(myModel, c(5,6,7))
myModel <- setTransThresholds(myModel, c(7,8,9))

# Create the clusters:
mySNPClusters <- makeSNPClusters(myModel, 'test')
myTransClusters <- makeTransClusters(myModel, 'test')

# Examine the results using igraph:
myModel <- setCutoffs(myModel)
plotTransClusters(myModel, vSize=20, vFontSize=2, level=7, thick=3, labelOffset=0)
plotTransClusters(myModel, vSize=20, vFontSize=2, level=8, thick=3, labelOffset=0)
plotTransClusters(myModel, vSize=20, vFontSize=2, level=9, thick=3, labelOffset=0)

# And compare these to the clusters obtained with SNP-based clustering:
plotSNPClusters(myModel, vColor='orange', vSize=20, vFontSize=2, level=5, thick=3, labelOffset=0)
plotSNPClusters(myModel, vColor='orange', vSize=20, vFontSize=2, level=6, thick=3, labelOffset=0)
plotSNPClusters(myModel, vColor='orange', vSize=20, vFontSize=2, level=7, thick=3, labelOffset=0)

# Test directly whether two cases are in the same cluster:
withinCluster(N = 3, k_cutoff = 5, t1 = 2012.13, t2 = 2015.76, lambda = 0.7, beta = 1.3, perc_cutoff = 0.2)