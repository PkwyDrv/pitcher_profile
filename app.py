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


 #define selected pitcher data to use
results_df = df.loc[df['last_name, first_name'] == pitcher].drop('Unnamed: 0', axis=1).reset_index(drop=True)

columns = ['pitches', 'pitch_usage', 'whiff_percent', 'k_percent', 'put_away', 'hard_hit_percent']

if st.sidebar.button('Get Data'): 
    st.header(f'{pitcher}')
    for col in columns:
    # create a histogram for each metric
        plot_df = results_df.groupby('last_name, first_name')[['pitch_name', f'{col}']]
        fig = px.histogram(plot_df, x='pitch_name', y=f'{col}')  
        st.plotly_chart(fig, use_container_width=True)




