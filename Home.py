import streamlit as st
import pandas as pd

st.markdown("<h1 style='text-align: center; color: #191970 ;'>Fifa 19 Data Analysis Dashboard</h1>", unsafe_allow_html=True)

st.image('home.jpg', use_column_width=True)
st.markdown(''' 
            * This App presents Data Analysis and Insights of Fifa 19 Dataset.  
            * The Data is obtained from [Kaggle](https://www.kaggle.com/datasets/winterbreeze/fifa19eda)
            * You can select one of the options from the sidebar to Explore the data.''')


# Show Sample Data
df = pd.read_csv('fifa_eda.csv')
df.dropna(inplace=True)
st.subheader('Sample Dataset')
if st.checkbox('Show Dataset'):
    st.dataframe(df.head(5))