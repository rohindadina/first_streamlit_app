import streamlit

streamlit.title('My parents New healthy diner')
streamlit.header('Breakfast menu')
streamlit.text('🥣Omega 3 and BB oat')
streamlit.text('🥗Kale Spinach and Rocket smoothie')
streamlit.text('🐔Hard boiled free range')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list=pandas.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
streamlit.dataframe(my_fruit_list)
  
                 
