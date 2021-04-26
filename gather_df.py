import streamlit as st
import pandas as pd
import pickle

from sportsreference.mlb.teams import Teams
from sportsreference.mlb.schedule import Schedule


teams = Teams('2021')
df = teams.dataframes

keys = list(df['name'].values) #full_name
vals = list(df['abbreviation'].values) #abbreviation

team_dict = dict(zip(keys,vals))

# @st.cache
def schedule_df(team_name):
    team_obj = Schedule(team_name, year=2019)
    df = team_obj.dataframe
    df.reset_index(inplace=True)
    df.rename(columns={"index": "team_name"},inplace=True)
    df['team_name'] = team_name
    return df

team_list = list(team_dict.values())

schedule_dict = {team:schedule_df(team) for team in team_list}
teams_df = pd.concat(schedule_dict.values(), ignore_index=True)

pickle.dump(teams_df, open("pickle_jar/df_2019.p", "wb"))