#getwd() and setwd() to documents-->STSCI_BASEBALL
#read csv into R

rap<-read.csv("Rapsodo_data.csv")

rap2<-subset(rap, Exit.Velocity!="NA")

#descending order of exit velocity
rap2[order(-rap2$Exit.Velocity),1:2]

#barrels (exit velocity>=90mph)
bar<-rap2[rap2$Exit.Velocity>=90,1:2]


#farthest hits
rapD<-subset(rap, Distance!="NA")
rapD[order(-rapD$Distance),c(TRUE,FALSE,FALSE,FALSE,FALSE,FALSE,TRUE,FALSE,FALSE)]




