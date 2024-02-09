import streamlit as st
import pandas as pd
import plotly.express as px
from helper import interest_insights, top10, bottom10, top10_viz

df = pd.read_csv('../FIFA19_APP/fifa_eda.csv')
df.dropna(inplace=True)

interest = st.selectbox('Select Your Interest ', ['Age', 'Overall', 'Potential', 'Value', 'Wage', 'Height', 'Weight', 'Release Clause'])

mydf= df.nlargest(10, interest)[['Name', 'Club', interest]]
st.plotly_chart(px.bar(mydf, x='Name', y=interest, title=f' Top 10 {interest} '), use_container_width=True)

st.dataframe(mydf)
st.markdown(mydf.to_markdown(index=False))

# Visualizations
st.plotly_chart(top10_viz(interest))

max_value = df[interest].max()
min_value = df[interest].min()
avg_value = round(df[interest].mean(),1)
col1, col2, col3 = st.columns(3)

col1.metric(label=f'Max {interest}', value=max_value)
col2.metric(label=f'Min {interest}', value=min_value)
col3.metric(label=f'Avg {interest}', value=avg_value)

c1, c2, c3 = st.columns(3)
with c1 :
    st.container(border=1).metric(label=f'Max {interest}', value=max_value)

with c2 :
    card = st.container(border=1)
    card.metric(label=f'Min {interest}', value=min_value)

with c3 :
    card = st.container(border=1)
    card.metric(label=f'Avg {interest}', value=avg_value)


# Statistics Metrics
st.markdown(f'<h1 style="text-align: center; color: #191970 ;">{interest} Insights</h1>', unsafe_allow_html=True)
min_value, max_value, mean_value = interest_insights(interest)

col1, col2, col3 =st.columns(3)

card1 = col1.container(border=1)
card1.metric(label=f'Max {interest}', value=max_value)

card2 = col2.container(border=1)
card2.metric(label=f'Min {interest}', value=min_value)

card3 = col3.container(border=1)
card3.metric(label=f'Mean {interest}', value=mean_value)  

# Top and Bottom 10
col1, col2 =st.columns(2)
col1.markdown(f'<h2 style="text-align: center; color: #191970 ;">Top 10 Players</h2>', unsafe_allow_html=True)
top = top10(interest)
col1.markdown(top.to_markdown(index=False))

col2.markdown(f'<h2 style="text-align: center; color: #191970 ;">Bottom 10 Players</h2>', unsafe_allow_html=True)
bottom = bottom10(interest)
col2.markdown(bottom.to_markdown(index=False))




