# Understat xG

### Season xG Data

To get xG values for every match in a season:
```
python season_data.py EPL 2015
```
League IDs are EPL, La_Liga, Bundesliga, Serie_A, Ligue_1 and RFPL.  
Available seasons are 2014 to present.

### Match Shot Data
To get data for all shots in a single match:  
```
# for https://understat.com/match/9901
python match_data.py 9091
```

### Expected Points
To calculate expected points use a CSV created by season.py and specify the number of iterations to use:
```
python sim_season.py season.csv 100
```

### Heatmaps

Using 250,000 shots.

![](figures/all_shots.png)
![](figures/head.png)
![](figures/right_foot.png)
![](figures/left_foot.png)
![](figures/freekicks.png)
![](figures/freekicks_right.png)
![](figures/freekicks_left.png)
