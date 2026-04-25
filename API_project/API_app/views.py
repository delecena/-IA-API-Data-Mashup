import requests

from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def movie_mashup(request):
    movie_title = request.GET.get('title') 
    
    if not movie_title:
        return Response({"message": "Please search for a movie title to see results."}, status=404)

    tmdb_url = f"https://api.themoviedb.org/3/search/movie?api_key=6a41d049f39e24d8da449d9f2976dae4&query={movie_title}"
    
    
    try:
        tmdb_resp = requests.get(tmdb_url, timeout=5)
        all_results = tmdb_resp.json().get('results', [])
        
        sorted_results = sorted(all_results, key=lambda x: x.get('popularity', 0), reverse=True)
        
        raw_results = sorted_results[:10]

        mashup_list = []
        
        for item in raw_results:
            
            title = item.get('title')

            omdb_url = f"http://www.omdbapi.com/?apikey=b9948957&t={title}"
            omdb_data = requests.get(omdb_url, timeout=5).json()
            
            poster_path = item.get('poster_path')
            
            if poster_path:
                poster_url = f"https://image.tmdb.org/t/p/w200{poster_path}"
            else:
                poster_url = "https://via.placeholder.com/200x300?text=No+Poster"
            
            unified_item = {
                "title": title,
                "poster": poster_url,
                "release_date": item.get('release_date'),
                "popularity": item.get('popularity'),
                "awards": omdb_data.get('Awards', 'N/A'),
                "box_office": omdb_data.get('BoxOffice', 'N/A'),
                "status": "Blockbuster" if item.get('popularity', 0) > 9 else "Indie/Niche",
                "status_class": "blockbuster" if item.get('popularity', 0) > 9 else "indie"
            }
            mashup_list.append(unified_item)

        return render(request, 'API_app/results.html', {
            'results': mashup_list,
            'query': movie_title
        })

    except requests.exceptions.RequestException:
        return Response({"error": "Network timeout. Please retry."}, status=504)
    
    
def home(request):
    return render(request, 'API_app/home.html')