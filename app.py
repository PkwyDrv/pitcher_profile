# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: -all
#     custom_cell_magics: kql
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.11.2
# ---

# %% [markdown]
# # Pitcher Profile

# %% [markdown]
# ### This app analyzes MLB pitcher arsenals based on metrics such as pitch type, pitch usage, whiff percent, and strike percent during the 2023 MLB regular season.

# %%
import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from pybaseball import statcast_pitcher_arsenal_stats

# %% [markdown]
# ### Get pitcher data

# %%

pitch_data = statcast_pitcher_arsenal_stats(2023, minPA=0, )
pitch_csv = pitch_data.to_csv('pitch_data.csv', sep=',')
pitch_2023 = pd.read_csv('pitch_data.csv')

# %%
@st.cache_data
def load_data():
    return pitch_2023
df = load_data()

# %% [markdown]
# ### Titles and description

# %%
st.title('MLB Pitcher By The Pitch')

st.markdown = ("""This app analyzes MLB pitcher arsenals based on metrics such as pitch type, pitch usage, whiff percent, and strike percent during the 2023 MLB regular season.
    * **Python libraries:** streamlit, pandas, plotly.express, numpy, pybaseball, and seaborn
    * **Data source:** [baseballsavant.mlb.com](https://baseballsavant.mlb.com/)
    """)

# %% [markdown]
# ### View the data in streamlit

# %%
st.write('### Overview of the Data')

st.dataframe(df, use_container_width=True)

# %%
if st.checkbox("Show Summary of Pitch Data"):
    st.write(df.describe())

# %% [markdown]
# ### Scatterplot of comparing put-away, hard hit percent, and whiff percent to strike percent

# %%
st.write('### Overall Metrics Scatterplot Based on Strike Percent')

st.scatter_chart(data=df, x='k_percent', y=['put_away', 'hard_hit_percent', 'whiff_percent'], color=['#fc1d47', '#1f84e4', '#4fe255'], size=None, width=0, height=0, use_container_width=True)

# %% [markdown]
# ### Format sidebar dropdown menus

# %%

st.sidebar.header('Please select each:')
team = st.sidebar.selectbox('Team', df['team_name_alt'].sort_values().unique())
pitcher_choice = df['last_name, first_name'].drop_duplicates().loc[df['team_name_alt'] == team]
pitcher = st.sidebar.selectbox('Pitcher', pitcher_choice)


# %% [markdown]
#  ### Define selected pitcher data to use

# %%
results_df = df.loc[df['last_name, first_name'] == pitcher].drop('Unnamed: 0', axis=1).reset_index(drop=True)
filtered_df = results_df.filter(items=['pitch_name', 'pitches', 'pitch_usage', 'whiff_percent', 'k_percent', 'put_away', 'hard_hit_percent'])
columns = ['pitches', 'pitch_usage', 'whiff_percent', 'k_percent', 'put_away', 'hard_hit_percent']

# %% [markdown]
# ### Create a histogram for each metric

# %%
if st.sidebar.button('Get Data'): 
    st.header(f'{pitcher}')
    for col in columns:
    
        fig = px.histogram(filtered_df[f'{col}'], x=filtered_df['pitch_name'], y=filtered_df[f'{col}'], labels={'x': 'Pitch'})  
        fig.update_layout(yaxis_title=f'{col}')
        st.plotly_chart(fig, use_container_width=True)

# %%

# %%
