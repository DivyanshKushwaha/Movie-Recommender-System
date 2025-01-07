from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import requests

app = Flask(__name__)

# Load the movie data and similarity matrix
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    """Fetch the movie poster using TMDB API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    return "https://via.placeholder.com/500x750?text=No+Poster+Available"


def recommend(movie):
    """Recommend movies based on the selected movie."""
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(
            list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_movie_names = []
        recommended_movie_posters = []

        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_posters.append(fetch_poster(movie_id))
            recommended_movie_names.append(movies.iloc[i[0]].title)

        return recommended_movie_names, recommended_movie_posters
    except IndexError:
        return [], []


@app.route('/')
def index():
    """Render the homepage with the list of movies."""
    return render_template('index.html', movies=list(movies['title'].values))


@app.route('/recommend', methods=['POST'])
def get_recommendations():
    """Handle the recommendation request."""
    movie_name = request.form['movie_name']
    recommended_names, recommended_posters = recommend(movie_name)
    return jsonify({'names': recommended_names, 'posters': recommended_posters})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
