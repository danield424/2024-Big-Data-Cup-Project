# Possession: each event is showing that a team performed an action.
# VISUALIZE ON AN ICE SURFACE whenever possible.

import pandas as pd
import numpy as np
df = pd.read_csv('https://github.com/bigdatacup/Big-Data-Cup-2024/blob/main/BDC_2024_Womens_Data.csv?raw=true')
# print(df.head())

# TODO: add control time (rink-tilt) as a variable.

# df['new_controller'] = np.where
# df['control_time'] =

# TODO: get the rolling average over the last 3? 4? 5? minutes as a ratio of the two, and as a percentage for teams

# TODO: show goals vs rink-tilt time, and add the rink tilt scores up for each game?

# TODO: show goals vs shots? and above

# TODO: show goals vs penalties and above


# df['team'] = np.where(df['Team'] == df['Home Team'], 'home', 'away')
# # this is setting the team that performed the action to be named home and away for simplicity.
#
# # print(df.query("Event == 'Shot'").groupby('team')['X Coordinate'].describe())
# # checks shot locations
#
# df['new_possession'] = df['team'].shift(1) != df['team']  # - this shifts 1 down
# table1 = df[['Event', 'team', 'new_possession']].head(20)
# print(table1)
# # create a new variable "new_possession'" to track possession switch.
#
# df['poss_id'] = df['new_possession'].cumsum()
# table2 = df[['Event', 'team', 'new_possession', 'poss_id']].head(20)
# print(table2)
# # df.cumsum (cumulative sum, that accumulates values).
# # assign 1's to true, 0's to no. "possession id"
# # could be useful for seeing possession changes, total possession
#
# table3 = df.groupby(['team', 'poss_id'])['Event'].value_counts()
# print(table3)
# # filters events and groups by the possession.
