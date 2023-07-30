import streamlit as st
from recommendation import recommend

st.title("MovieMuse")


user_input = st.text_input("Enter the kind of movie you want to watch (You can also enter the kind of mood you are in):")


if st.button("Search"):
    movies = recommend(user_input=user_input)

    for movie in movies:
        st.write(movie)