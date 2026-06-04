import pickle
import streamlit as st

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]

    distances = sorted(
        list(enumerate(similarity[index])),
        reverse=True,
        key=lambda x: x[1]
    )

    recommended_movies = []

    for i in distances[1:6]:
        recommended_movies.append(
            movies.iloc[i[0]]['title']
        )

    return recommended_movies

# Load data
movies = pickle.load(open('movie recommand system/movie_list.pkl', 'rb'))
similarity = pickle.load(open('movie recommand system/similarity.pkl', 'rb'))

# Streamlit UI
st.title("🎬 Movie Recommender System")

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Select a movie",
    movie_list
)

if st.button("Show Recommendations"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for movie in recommendations:
        st.write(movie)