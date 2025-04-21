import pickle
import streamlit as st
import requests


movies = pickle.load(open(r'C:\Users\balas\OneDrive\Desktop\Balu\Myprojects\vs\MovieRecommendation\movie_list.pkl', 'rb'))
similary = pickle.load(open(r'C:\Users\balas\OneDrive\Desktop\Balu\Myprojects\vs\MovieRecommendation\similarity.pkl', 'rb'))


API_KEY = "a9204764eefbcd199d54b946975251db"  


def get_movie_id(movie_name):
    url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    data = requests.get(url).json()
    if data['results']:
        return data['results'][0]['id']
    return None


def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return "https://image.tmdb.org/t/p/w500/" + poster_path
    else:
        return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similary[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movies = []
    recommended_posters = []
    for i in distances[1:6]:
        movie_title = movies.iloc[i[0]].title
        movie_id = get_movie_id(movie_title)
        poster_url = fetch_poster(movie_id)
        recommended_movies.append(movie_title)
        recommended_posters.append(poster_url)
    
    return recommended_movies, recommended_posters

st.title("🎬 Movie Recommendation System")

selected_movie_name = st.selectbox(
    "Search for a movie", 
    movies['title'].values
)

if st.button("Recommend"):
    names, posters = recommend(selected_movie_name)
    
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
