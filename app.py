import pickle
import streamlit as st
import gzip

# Function to recommend movies
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
movies = pickle.load(open('movie_list.pkl', 'rb'))

with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# Streamlit UI
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="centered"
)

st.title("🎬 Movie Recommendation System")

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Choose a Movie",
    movie_list
)

if st.button("Show Recommendations"):
    recommendations = recommend(selected_movie)

    st.subheader("Recommended Movies")

    for i, movie in enumerate(recommendations, start=1):
        st.write(f"{i}. {movie}")