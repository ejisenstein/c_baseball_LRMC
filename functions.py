import numpy as np
import pandas as pd
import collections


def home_and_away(df, team):
    """find all home and home games, spits out a df"""
    home_df = df[df['team'] == team]
    c = collections.Counter(home_df['opponent_abbr'])
    result = {key: val for key, val in c.items() if val >=2}
    l = list(result.keys())
    hd_df = home_df[home_df['opponent_abbr'].isin(l)]
    
    h_home = hd_df[hd_df['location'] == 'Home']
    h_away = hd_df[hd_df['location'] == 'Away']
    
    h_home.sort_values(by='opponent_abbr', inplace=True)
    h_away.sort_values(by='opponent_abbr', inplace=True)
    h_away['win'] = np.where(h_away['result'] == 'Win', 1, 0)
  
    filt_h_home = h_home[['team', 'opponent_abbr', 'conference', 'diff']]
    filt_h_away = h_away[['opponent_abbr', 'win']]
    
    merge_df = filt_h_home.merge(filt_h_away, how='inner', on='opponent_abbr')
    
    return merge_df.rename(columns={'diff':'home_diff', 'win':'away_win'})
    