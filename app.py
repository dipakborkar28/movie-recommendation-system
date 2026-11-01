
import streamlit as st
import joblib

@st.cache_resource
def load_data():
    return joblib.load("movie_recommender.pkl")

data = load_data()

movies = data["movies"]
vectors = data["vectors"]
nn = data["nn"]

st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬"
)

st.title("🎬 Movie Recommendation System")
st.write("Select a movie to discover five similar movies.")

movie_titles = movies["title"].dropna().tolist()
selected_movie = st.selectbox("Choose a movie", movie_titles)

if st.button("Recommend Movies"):
    movie_index = movies.index[
        movies["title"] == selected_movie
    ][0]

    distances, indices = nn.kneighbors(
        vectors[movie_index],
        n_neighbors=min(6, len(movies))
    )

    st.subheader("Recommended Movies")

    count = 0
    for index in indices[0]:
        if index == movie_index:
            continue

        st.write(f"{count + 1}. {movies.iloc[index]['title']}")
        count += 1

        if count == 5:
            break
