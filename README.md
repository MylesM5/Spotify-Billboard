# Spotify-Billboard
Hello!

  This project uses Apache Airflow, Docker, Spotipy, and the Spotify API to pull the top 50 songs from Spotify's top 50.
This is the core of the project; Running Airflow in Docker to schedule batch processing on a daily basis.

  The script 'spotify_extract' pulls the track id's and begins constructing the dataset, including artist, track and 
track features not available on the spotify platform. All using the spotipy API, Once the JSON is parsed and 
the csv is finished, the data is pushed to google cloud bucket. 

As I become more familiar with the Google Cloud Platfrom I hope to build a visual dashboard to represent this data. 
