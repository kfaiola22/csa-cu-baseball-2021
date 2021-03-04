rapNul<-read.csv("Baseball_Data_Rapsodo_Feb - Cleaned Null Fields.csv")
x<-matrix(rapNul$Exit.Velocity)
heatmap(x, Rowv= rapNul$S.Zone.X, colv="Rowv", na.rm=TRUE)

rapNul$Exit.Velocity

frequency(bar$Name=="Collins")
for (i in bar$Name) {
  f<-frequency(bar$Name=="i")
  print(f)
}
