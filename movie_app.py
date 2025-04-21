import streamlit as st
import pickle
import os


# Load movie list and similarity matrix (use relative paths)
movie_list_path = os.path.join(os.getcwd(), 'movie_list.pkl')
similarity_path = os.path.join(os.getcwd(), 'similarity.pkl')

# Function to load pickle files
def load_pickle(file_path):
    with open(file_path, 'rb') as f:
        return pickle.load(f)

# Load the movie data and similarity matrix
movies = load_pickle(movie_list_path)
similarity = load_pickle(similarity_path)

# Function to recommend movies
def recommend(movie_name):
    try:
        # Find the index of the movie from the movie list
        movie_index = movies[movies['title'] == movie_name].index[0]
    except IndexError:
        return "Movie not found!"

    # Get similarity scores
    similarity_scores = list(enumerate(similarity[movie_index]))

    # Sort movies based on similarity scores
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get the top 5 similar movies
    recommended_movies = []
    for i in similarity_scores[1:6]:  # [1:6] to avoid recommending the movie itself
        movie_index = i[0]
        recommended_movies.append(movies.iloc[movie_index]['title'])

    return recommended_movies

# Streamlit UI
st.title("Movie Recommendation System")
st.header("Enter a movie name to get recommendations")

# Movie input from user
movie_input = st.text_input("Movie Name")

if movie_input:
    st.write(f"Recommended movies similar to **{movie_input}**:")
    
    # Call the recommend function and display results
    recommended_movies = recommend(movie_input)
    
    if isinstance(recommended_movies, list):
        for movie in recommended_movies:
            st.write(f"- {movie}")
    else:
        st.write(recommended_movies)  # Display error message if movie not found
