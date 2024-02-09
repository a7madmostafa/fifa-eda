import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('fifa_eda.csv')
df.dropna(inplace=True)
def interest_insights(interest):
    min_value = round(df[interest].min(), 1)
    max_value = round(df[interest].max(), 1)
    mean_value = round(df[interest].mean(), 1)
    return min_value, max_value, mean_value

def top10(interest):
    return df.nlargest(10, interest)[['Name', 'Club', interest]]

def bottom10(interest):
    return df.nsmallest(10, interest)[['Name', 'Club', interest]]

def top10_viz(interest):
    fig = px.bar(df.nlargest(10, interest)[['Name', 'Club', interest]], x='Name', y=interest, title=f' Top 10 {interest} ')
    return fig

def bottom10_viz(interest):
    fig = px.bar(df.nsmallest(10, interest)[['Name', 'Club', interest]], x='Name', y=interest)
    return fig