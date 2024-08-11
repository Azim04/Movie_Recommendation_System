# recommendations\views,py

import json
from .models import Movie
from django.shortcuts import render
from django.db.models import Q
import json


def preprocess_genres(movie_data):
    for movie in movie_data:
        if 'GENRES' in movie:
            movie['GENRES'] = movie['GENRES'].replace('|', ' | ')
    return movie_data

def home(request):
    with open('recommendations/templates/movies.json', encoding='utf-8') as f:
        movie_data = json.load(f)
        movie_data = preprocess_genres(movie_data)
    return render(request, 'home.html', {'movies': movie_data})


import json


def search_movies(request):
    query = request.GET.get('query')
    if query:
        # Load movie data from JSON file
        with open('recommendations/templates/movies.json', encoding='utf-8') as f:
            movie_data = json.load(f)

        # Filter movies whose titles contain the query string
        matching_movies = [movie for movie in movie_data if query.lower() in movie.get('TITLE', '').lower()]

        if matching_movies:
            preprocess_genres(movie_data)
            return render(request, 'search_results.html', {'movies': matching_movies, 'query': query})
        else:
            preprocess_genres(movie_data)
            return render(request, 'search_results.html', {'error_message': "No movies found.", 'query': query})
    else:
        # If no query string provided, return all movies
        with open('path/to/movies.json', encoding='utf-8') as f:
            movie_data = json.load(f)
            preprocess_genres(movie_data)
        return render(request, 'search_results.html', {'movies': movie_data})


def movie_detail(request, item_id):
    # Load movie data from JSON file
    with open('recommendations/templates/movies.json', encoding='utf-8') as f:
        movie_data = json.load(f)

    # Find the clicked movie
    clicked_movie = None
    for movie_entry in movie_data:
        if movie_entry['ITEM_ID'] == item_id:
            clicked_movie = movie_entry
            clicked_movie['GENRES'] = clicked_movie['GENRES'].split('|')  # Convert to list
            break

    # Find related movies (movies with at least one matching genre)
    related_movies = []
    related_genres = set()  # Using a set to avoid duplicate genres
    if clicked_movie:
        clicked_genres = set(clicked_movie['GENRES'])  # Already a list
        for movie_entry in movie_data:
            if movie_entry['ITEM_ID'] != item_id:
                movie_entry_genres = set(movie_entry['GENRES'].split('|'))
                matching_genres = clicked_genres.intersection(movie_entry_genres)
                if matching_genres:
                    related_movies.append((movie_entry, list(matching_genres)))  # Convert to list
                    related_genres.update(movie_entry_genres)

    # Sort related movies based on the number of matching genres
    related_movies.sort(key=lambda x: len(x[1]), reverse=True)

    # Convert related genres set to list before sending to the template
    related_genres_list = list(related_genres)

    # If movie found, render the movie_detail template with the movie data and related movies
    return render(request, 'movie_detail.html', {'movie': clicked_movie, 'related_movies': related_movies, 'related_genres': related_genres_list})
