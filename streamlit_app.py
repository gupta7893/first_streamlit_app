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
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
s.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
s.dataframe(my_fruit_list)
