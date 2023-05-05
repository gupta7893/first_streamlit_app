import streamlit as s

s.title('My Mom\'s New Healthy Diner')
s.header('Breakfast Favorites')
s.text('🥣 Omega 3 & Blueberry Oat meal')
s.text('🥗 Kale, Spinach & Rocket Smoothie')
s.text('🐔 Hard-bolied Free-range Egg')
s.text('🥑🍞 Avocado Toast')

s.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
# s.help()


import pandas as pd

my_fruit_list = pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
s.dataframe(my_fruit_list)
