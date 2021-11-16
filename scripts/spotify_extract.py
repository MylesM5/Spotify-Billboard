import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os




client_credentials_manager = SpotifyClientCredentials(client_id= os.environ["cid"],client_secret= os.environ["secret"])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Pulls playlist ID
plist = sp.search(q='top+songs+global', type='playlist', limit=50, offset=0)
playlist_id = plist['playlists']['items'][0]['id']

# Get playlist track id's
offset = 0
data = []
track_ids = None
while True:
    response = sp.playlist_items(playlist_id,
                                    offset=offset,
                                    fields="items.track.id,playlist.tracks"
                                    )

    if len(response["items"]) == 0:
        break

    data.append(response['items'])

    offset = offset + len(response["items"])

    ids = []
    for track in data[0]:
        ids.append(track['track']['id'])
    track_ids = pd.Series(ids)



#Final data frame for track data - ID, Artist, and popularity
playlist = pd.DataFrame()
playlist['id'] = track_ids

track_data = sp.tracks(track_ids)

for i in range(len(track_data['tracks'])):

    if track_data['tracks'][i]['id'] == playlist.loc[i, 'id']:
        playlist.loc[i, 'artist-name'] = track_data['tracks'][i].get("artists")[0]['name']
        playlist.loc[i, 'track-name'] = track_data['tracks'][i].get("name")
        playlist.loc[i, 'popularity'] = track_data['tracks'][i].get('popularity')



# Drop keys from JSON response.

keys_to_drop = ['type', 'id', 'uri', 'track_href', 'analysis_url']
features = sp.audio_features(track_ids)

for i in range(len(features)):
    for j in keys_to_drop:
        del features[i][j]

        cols = features[i].items()

    for y in cols:
        playlist.loc[i, y[0]] = y[1]





playlist.to_csv("spot.csv")

