import streamlit as st
import pandas as pd
import pickle

from sportsreference.mlb.teams import Teams
from sportsreference.mlb.schedule import Schedule
from divisions import div_dict

st.title("LRMC for Baseball")

df = pickle.load(open("pickle_jar/df_2019.p", "rb"))
team_dict = pickle.load(open("pickle_jar/team_dict.p", "rb"))

cleaned_df = df[['team_name', 'opponent_abbr', 'location', 'result', 'runs_allowed', 'runs_scored']]

cleaned_df['team_name_conference'] = cleaned_df['team_name'].map(div_dict)
cleaned_df['opponent_conference'] = cleaned_df['opponent_abbr'].map(div_dict)
cleaned_df['diff'] = cleaned_df['runs_scored'] - cleaned_df['runs_allowed']

st.dataframe(cleaned_df)