"[IA] API Data Mashup" from the MIS track
IA by Dallax Earth Leceña

## What the application does
The application is used to demonstrate how a system can gather data from different sources to provide one coherent output. In this case, the code utilized two APIs, TMDB and OMDb, which are very famous for their data regarding movies. Essentially, this application is about searching for a movie using keywords and gathering data from the mentioned APIs.

## APIs Used

Integrated APIs
TMDb (The Movie Database): https://www.themoviedb.org/documentation/api.
Description: This API is used as the primary search engine for the application. It retrieves core movie details including the official title, release date, popularity scores, and poster images.

OMDb (Open Movie Database): https://www.omdbapi.com/.
Description: The application uses it to fetch specific metadata that TMDb might not prioritize in a search result, such as detailed award history and box office earnings.


## How the data join works:
The application uses a common link between the two APIS, most likely the movie title. It retrieves a list of movies from both APIs using this keyword alongside the details requested by the program. 

Example:
If a user searches for "The Batman", the application creates a combined entry like this:
From TMDb: Title ("The Batman"), Release Date ("2022-03-01"), and Popularity ("18.748").
From OMDb: Awards ("Nominated for 3 Oscars. 40 wins & 176 nominations total") and Box Office ("$369,801,546").
Result: One unified "Movie Card" displayed to the user containing all five data points simultaneously.

## Setup
"Virtual Environment First Setup"
source venv/bin/activate
cd API_project
pip install djangorestframework
python manage.py runserver

"How to Run"
cd API_project
python manage.py runserver

## Known Limitations
Missing Features
Poster Integration: While the logic for fetching posters exists in the backend, the frontend currently focuses on text-based production data and critical insights.
Detailed Plot Summaries: The application prioritizes high-level metadata (awards and box office) over long-form narrative descriptions from the APIs.

API Constraints
Rate Limiting: Both TMDb and OMDb enforce request limits; searching for very broad terms may occasionally hit these caps due to the "loop-based" fetch logic.
Latency: Because the app performs a secondary OMDb request for every movie found by TMDb, loading times increase with the number of results fetched.

Edge Cases
Title Mismatches: Since the join depends on title strings, movies with common names or those that exist in one database but not the other may show "N/A" for critical insights.
Missing Popularity Data: If TMDb does not provide a popularity score for a specific entry, the application defaults the value to 0 to prevent a system crash.

## AI Disclosure
- Helped with css
- Helped with explaining APIs. How it's used and how it works
- Defined most of the limitations 
