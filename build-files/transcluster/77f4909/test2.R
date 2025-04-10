#!/usr/bin/R

# Adapted from https://github.com/JamesStimson/transcluster/blob/master/vignettes/how-to-guide.Rmd

library(transcluster)
library(stats)
library(clue)
library(igraph)

## British Columbia example

# This time we load sample date and SNP distance data from file.
bcModel <- createModel()
fileName <- system.file("extdata", "mclust12_dates_R.csv", package = "transcluster", mustWork = TRUE)
bcModel <- setDatesFromFile(bcModel, fileName)
fileName <- system.file("extdata", "bc_snp_matrix_R.csv", package = "transcluster", mustWork = TRUE)
bcModel <- setSNPFromFile(bcModel, fileName)

# And we set up the other parameters.
bcModel <- setParams(bcModel, lambda=1.5, beta=2.0)
bcModel <- setCutoffs(bcModel)   #takes a few seconds
bcModel <- setSNPThresholds(bcModel, c(4))
bcModel <- setTransThresholds(bcModel, c(3))

# Create and plot.
bcSNPClusters <- makeSNPClusters(bcModel, nameBase='test', writeFile=F)
bcTClusters <- makeTransClusters(bcModel, nameBase='test', writeFile=F)

plotSNPClusters(bcModel, level=4, vColor='orange',vSize=4, thick = 1.25)
plotTransClusters(bcModel, level=3, vColor='lightblue',vSize=4, thick = 2, vFontSize=1)

# Add region data to inform the clustering.
regFileName <- system.file("extdata", "example_region_data.csv", package = "transcluster", mustWork = TRUE)
bcModel <- setRegionsFromFile(bcModel, regFileName)
bcModel <- setCutoffsSpatial(bcModel)
plotTransClustersSpatial(bcModel, level=3, vSize=4, thick=2, vFontSize=1)