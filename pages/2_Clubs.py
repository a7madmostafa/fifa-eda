import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide", page_title="Club Insights", page_icon=":soccer:")

df = pd.read_csv('../FIFA19_APP/fifa_eda.csv')
df.dropna(inplace=True)

club = st.selectbox('Select Your Club ', df['Club'].unique())

mydf= df[df['Club'] == club][['Name', 'Value', 'Wage', 'Age', 'Overall', 'Release Clause']]

most_valuable_player = df[df['Club'] == club].nlargest(1, 'Value').head(1)

# st.dataframe(most_valuable_player)
col1, col2 = st.columns(2)
# col1.write(most_valuable_player['Name'].iloc[0])
col1.subheader('Most Valuable Player')
col1.metric(most_valuable_player['Name'].iloc[0], most_valuable_player['Value'].iloc[0])

col2.subheader('Wage')
col2.metric(most_valuable_player['Name'].iloc[0], most_valuable_player['Wage'].iloc[0])



interest = st.selectbox('Select Your Interest ', ['Age', 'Overall', 'Potential', 'Value', 'Wage', 'Height', 'Weight', 'Release Clause'])

mean_val= df.groupby('Club').mean()[interest].nlargest(5).reset_index()
mean_val[interest]= mean_val[interest].apply(lambda x: round(x, 1))
mean_val.rename(columns={interest: f'Mean {interest}'}, inplace=True)
total_val = df.groupby('Club').sum()[interest].nlargest(5).reset_index()
total_val[interest]= total_val[interest].apply(lambda x: round(x, 1))
total_val.rename(columns={interest: f'Total {interest}'}, inplace=True)

st.markdown(f'<h1 style="text-align: center; color: #191970 ;">{interest} Top Averages</h1>', unsafe_allow_html=True)
st.plotly_chart(px.bar(mean_val, x='Club', y=f'Mean {interest}'), use_container_width=True)

st.markdown(f'<h1 style="text-align: center; color: #191970 ;">{interest} Top Totals</h1>', unsafe_allow_html=True)
st.plotly_chart(px.bar(total_val, x='Club', y=f'Total {interest}'), use_container_width=True)


