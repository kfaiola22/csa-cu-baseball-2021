indoor<-read.csv('indoor_scrimmages-feb.16.csv',as.is=TRUE)

player_names<- unique(indoor$Name)
n_players<-length(player_names)

swing_pct<-rep(NA, n_players)
chase_pct<-rep(NA, n_players)

strike<-indoor$SZone.Location %in% c('7','8','9','12','13','14','17','18','19')

for (i in 1:n_players) {
  #vector of T and F when player i's name matches
  inds <- indoor$Name == player_names[i]
  
  #number of swings player i takes
  swings<-sum(indoor$Action[inds] %in% c("s","f"))
  
  #number of pitches player i takes
  pitches<-sum(inds)
  
  #swing%
  swing_pct[i]<-swings/pitches
  print(swing_pct[i])
  
  #sum of strikes player i faces (counts the no. of T's)
  strikes_player<-sum(strike[inds])
  
  #sum of balls player i faces
  balls_player<-sum(!strike[inds])
  
  #vector of T and F for player i's actions, T when player i swings, F when player i takes
  swing<-indoor$Action[inds] %in% c("s","f")
  
  #vector (length of pitches seen by player i) of T and F, T when player i faces a strike
  strike_p <- strike[inds]
  
  #vector of T and F, T when strike_p is F
  ball_p<- !strike_p
  
  #logic vector, T when player i swung and it was a ball
  swing_ball<- swing & ball_p
  
  #logic vector, T when player i swung and it was a strike
  swing_strike<- swing & strike_p
  
  #chase%
  chase_pct[i]<- sum(swing_ball)/sum(ball_p)
  print(chase_pct[i])
}

swing_stats<-data.frame(player_names, swing_pct, chase_pct, stringsAsFactors = TRUE)

write.csv(swing_stats,"/Users/katherinefaiola/Documents/STSCI_BASEBALL/Swing_Stats_Feb.16.csv", row.names = TRUE)


barrel_pct<-rep(NA, n_players)

for (j in 1:n_players) {
  indivs<-indoor$Name == player_names[j]
  barrels<-sum(indoor$Barrel.Y.N[indivs] %in% c("Y"))
  at_bats<-sum(indoor$Result.Has.Data[indivs] %in% c("1"))
  barrel_pct[j]<-barrels/at_bats
  print(barrel_pct[j])
}

barrel_stats<-data.frame(player_names, barrel_pct, stringsAsFactors = TRUE)

write.csv(barrel_stats,"/Users/katherinefaiola/Documents/STSCI_BASEBALL/Barrel_Stats_Feb.16.csv", row.names = TRUE)
