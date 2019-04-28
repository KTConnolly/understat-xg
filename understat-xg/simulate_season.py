import argparse
import random
import pandas as pd
from scipy.stats import skellam


def sim_season(dataframe, iterations):
    # Create a list of team names and use them as keys in dict
    teams = dataframe['Home'].unique().tolist()
    d = dict.fromkeys(teams, 0)

    for i in range(iterations):
        for index, row in dataframe.iterrows():
            home_xg = row['Home xG']
            away_xg = row['Away xG']

            # Calculate prob of home and away winning by 1 to 25 goals
            home = 0
            for i in range(1, 25):
                home += skellam.pmf(i, home_xg, away_xg)

            away = 0
            for i in range(-1, -25, -1):
                away += skellam.pmf(i, home_xg, away_xg)

            # Supremacy of 0 is a draw
            draw = skellam.pmf(0, home_xg, away_xg)

            # Weight contains probabilities of the three outcomes
            weights = [home, draw, away]
            result = random.choices(('Home', 'Draw', 'Away'),
                                    weights=weights)[0]

            # Add 3 points for win,1 for draw
            if result == 'Home':
                d[row.Home] += 3
            elif result == 'Away':
                d[row.Away] += 3
            else:
                d[row.Home] += 1
                d[row.Away] += 1

    # Update dict with average points rather than total
    d.update((team, pts / iterations) for team, pts in d.items())

    # Create a list sorted by points
    points = sorted(((key, value) for (value, key) in d.items()), reverse=True)

    return points


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Path to CSV file')
    parser.add_argument('iterations', help='Path to CSV file', type=int)
    args = parser.parse_args()

    df = pd.read_csv(args.filename)
    points = sim_season(df, args.iterations)

    for team in points:
        print(f'{team[1]} - {team[0]}')


if __name__ == '__main__':
    main()
