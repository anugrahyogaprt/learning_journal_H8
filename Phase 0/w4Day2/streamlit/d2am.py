from click import option
import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import plotly.express as px

st.title('My First App')
st.write('string')

df= pd.DataFrame({'a':[4, 5, 6, 3, 6, 8], 'b':[3, 6, 4, 7, 4, 6]})
st.dataframe(df)
st.table(df)

st.write(df)
#------------------------------------------
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
#------------------------------------------
map_data = pd.DataFrame(
    np.random.randn(100, 2) / [100, 100] + [-6.244, 106.828],
    columns=['lat', 'lon'])

st.map(map_data)
#---------------------------------------------
if st.button('Say hello'):
    st.write('Clicked')
else:
    st.write('Not Clicked')
#-------------------------------------------
st.header('This is checkbox')
if st.checkbox('Show data'):
    st.write('Checked')
#----------------------------------------
select_radio = st.radio('Select One :', ('Music', 'Art', 'Games'), 2)
if select_radio == 'Art':
    st.write('Art is beautiful')
elif select_radio == 'Games':
    st.write('Games are relax')
else:
    st.write('Music are awesome')
#-------------------------------------------
st.selectbox('Which one do you like:', options=('Vanilla', 'Coklat', 'Keju'), index=0)
#---------------------------------------
multi = st.multiselect('You can choose more than one :', options=('One', 'Two', 'Three'))
multi
if len(multi) > 1:
    st.write(multi[-1])
#----------------------------)
val= st.slider('Select range', min_value=0.0, max_value=100.0, step=0.1)
st.write(val)
#---------------------------
val1= st.slider('Select range', 0.0, 100.0, (25.0, 75.0))
st.write(val1)
#----------------------------
start_color, end_color = st.select_slider(
    'Select a range of color wavelength',
    options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    value=('red', 'blue'))
st.write('You selected wavelengths between', start_color, 'and', end_color)
#-----------------------
date = st.date_input('Select Date')
t = st.time_input('Set an alarm for', datetime.time(8, 45))
st.write('Alarm is set for', t)
#----------------------------------
title = st.text_input('Movie title', 'Life of Brian')
st.write('The current movie title is', title)
#-------------------------------
txt = st.text_area('Text to analyze', '''
    It was the best of times, it was the worst of times, it was
    the age of wisdom, it was the age of foolishness, it was
    the epoch of belief, it was the epoch of incredulity, it
    was the season of Light, it was the season of Darkness, it
    was the spring of hope, it was the winter of despair, (
    ''')
#-----------------------------
st.sidebar.header('This is sidebar header')
st.sidebar.selectbox('sidebar select', options=('sidebar1', 'siderbar2'))
text_sidebar = st.sidebar.text_input('Input your text')
st.sidebar.write(text_sidebar)
#-----------------------------------------
left_column, right_column = st.columns(2)
pressed = left_column.button('Press me?')
if pressed:
  right_column.write("Woohoo!")

expander = st.expander("FAQ")
expander.write("Here you could put in some really, really long explanations...")

#--------------------------
st.subheader('Matplotlib')
arr = np.random.normal(0, 1, size=1000)
arr
fig, ax = plt.subplots()
ax.hist(arr, bins=25)
st.pyplot(fig)
#---------------------------
st.subheader('Seaborn')
fig1, ax1 = plt.subplots(figsize=(12, 7))
sns.histplot(arr, bins=25)
st.pyplot(fig1)
#--------------------------------------
st.subheader('plotly') 
df = px.data.gapminder().query("country=='Canada'") 
fig3 = px.bar(df, x="year", y="lifeExp", title='Life expectancy in Canada') 
st.plotly_chart(fig3) 
#---------------------------------------------
st.subheader('pokemon')
df= pd.read_csv('Pokemon.csv')
#-----------------------------------------
@st.cache
def load_data():
    df1 = pd.read_csv('Pokemon.csv')
    return(df1)

df = load_data()
st.write(df)
#-----------------------------------------------
fig, ax = plt.subplots(figsize=(12 ,7))
sns.histplot(df['Attack'])
st.pyplot(fig)
#-----------------------------------------
st.subheader('Callback')
gen  = st.selectbox('Select Generation :', options=(1, 2, 3, 4, 5, 6), index=4)
fig, ax = plt.subplots(figsize=(12 ,7))
sns.histplot(df[df['Generation']==gen]['Attack'])
st.pyplot(fig)
#-----------------------------------------
st.subheader('Callback paitplot')
fig, ax = plt.subplots(figsize=(12 ,7))
selec_type = st.radio(label='Choose Type', options=df['Type 1'].unique())
sns.scatterplot(df[df['Type 1'] == selec_type]['Attack'], df[df['Type 1'] == selec_type]['Speed'])
st.pyplot(fig)