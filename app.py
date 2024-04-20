import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from pybaseball import statcast_pitcher_arsenal_stats

#get pitcher data
pitch_data = statcast_pitcher_arsenal_stats(2023, minPA=0, )
pitch_csv = pitch_data.to_csv('pitch_data.csv', sep=',')
pitch_2023 = pd.read_csv('pitch_data.csv')

@st.cache_data
def load_data():
    return pitch_2023
df = load_data()
#titles and description
st.title('MLB Pitcher By The Pitch')

st.markdown = ("""This app analyzes MLB pitcher arsenals based on metrics such as pitch type, pitch usage, whiff percent, and strike percent during the 2023 MLB regular season.
    * **Python libraries:** streamlit, pandas, plotly.express, numpy, pybaseball, and seaborn
    * **Data source:** [baseballsavant.mlb.com](https://baseballsavant.mlb.com/)
    """)

st.write('### Overview of the Data')
# view the data in streamlit
st.dataframe(df, use_container_width=True)

if st.checkbox("Show Summary of Pitch Data"):
    st.write(df.describe())
    
st.write('### Overall Metrics Scatterplot Based on Strike Percent')
# Scatterplot of comparing put-away, hard hit percent, and whiff percent to strike percent
st.scatter_chart(data=df, x='k_percent', y=['put_away', 'hard_hit_percent', 'whiff_percent'], color=['#fc1d47', '#1f84e4', '#4fe255'], size=None, width=0, height=0, use_container_width=True)
 
#format sidebar dropdown menus
st.sidebar.header('Please select each:')
team = st.sidebar.selectbox('Team', df['team_name_alt'].sort_values().unique())
pitcher_choice = df['last_name, first_name'].drop_duplicates().loc[df['team_name_alt'] == team]
pitcher = st.sidebar.selectbox('Pitcher', pitcher_choice)

if st.sidebar.button("**Get Data**"):
    
    st.header(f'{pitcher}')
    #define selected pitcher data to use
    pitches = df['pitch_name'].unique()
    thrown = df['pitches'].loc[df['last_name, first_name'] == pitcher]
    percent_pitched = df['pitch_usage'].loc[df['last_name, first_name'] == pitcher]
    strike_percent = df['k_percent'].loc[df['last_name, first_name'] == pitcher]
    whiff_percent = df['whiff_percent'].loc[df['last_name, first_name'] == pitcher]
    put_away_percent = df['put_away'].loc[df['last_name, first_name'] == pitcher]
    hard_hit_percent = df['hard_hit_percent'].loc[df['last_name, first_name'] == pitcher]


#create a histogram for each metric
    fig_thrown = px.histogram(thrown, x=pitches, title="Number of Pitches Thrown MLB 2023", nbins=11, width=600, height=400)
    fig_thrown.show()
    fig_percent_pitched = px.histogram(percent_pitched, x=pitches, title="Pitched Percent MLB 2023", nbins=11, width=600, height=400)
    fig_percent_pitched.show()
    fig_strike = px.histogram(strike_percent, x=pitches, title="Strike Percent MLB 2023", nbins=11, width=600, height=400)
    fig_strike.show()
    fig_whiff = px.histogram(whiff_percent, x=pitches, title="Percent of Whiffs per Pitch MLB 2023", nbins=11, width=600, height=400)
    fig_whiff.show()
    fig_put_away = px.histogram(put_away_percent, x=pitches, title="Percent Punch Out Pitches MLB 2023", nbins=11, width=600, height=400)
    fig_put_away.show()
    fig_hard_hit = px.histogram(hard_hit_percent, x=pitches, title="Percent Pitches for Hard Hits MLB 2023", nbins=11, width=600, height=400)
    fig_hard_hit.show()
    

