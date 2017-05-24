# LoL-Champion-Suggester

Inputs:
  Prefered playable champions
  Role
  
Output:
  a champion suggestion to pickup


Constraints:
Current champion WR (Based on your elo? Based on Diamond+?)
Should we include history?
What about storage so we don't have to pull the API each time?
Need a machine-learning algorithm?
Should we take into account which champions act similarly to each other? (Poppy Q, Maokai Q, Illaoi Q?)


Current manual method:
Pick your current champs/comfort picks
Look at lolking.net for most played champions at Elo
Look at lolalytics.com Diamond+ games for WR of champions
Compare lolking champs with lolalytic WR
Rate your pick champions 1-X at beating given champion
List any champions that have negative WR against given champion
Suggest Stretch champ to counter given champion
