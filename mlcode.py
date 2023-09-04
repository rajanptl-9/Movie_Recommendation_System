import pandas as pd
import requests
from io import StringIO
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# google_drive_link = "https://drive.google.com/file/d/1gM0Nx5NNOu7NSkramPkZbhwk0qQPYC7A/view?usp=sharing"
# response = requests.get(google_drive_link)
# csv_file = response.text
# print(StringIO(csv_file))
# df_movies = pd.read_csv(StringIO(csv_file))
df_movies = pd.read_csv("./movies.csv")
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']

for feature in selected_features:
    df_movies[feature] = df_movies[feature].fillna("")

collecting_useful_features = df_movies['genres']+" "+df_movies['keywords']+" "+df_movies['tagline']+" "+df_movies['cast']+" "+df_movies['director']

vectorizor = TfidfVectorizer()

numerical_features = vectorizor.fit_transform(collecting_useful_features)

movies_similarity = cosine_similarity(numerical_features)

list_of_all_titles = df_movies['title'].tolist()

def search_movie(movie_name):
    find_similar_movies_name = difflib.get_close_matches(movie_name, list_of_all_titles)
    closest_match = find_similar_movies_name[0]
    index_of_closest_match = df_movies[df_movies.title == closest_match]['index'].values[0]
    similar_match_score = list(enumerate(movies_similarity[index_of_closest_match]))
    sorted_similar_movies = sorted(similar_match_score, key = lambda x: x[1], reverse = True)
    return sorted_similar_movies, df_movies





