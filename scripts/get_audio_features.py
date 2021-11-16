import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import pandas as pd

client_credentials_manager = SpotifyClientCredentials(client_id= os.environ["cid"],client_secret= os.environ["secret"])
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


def get_audio_features(df, ids):
    keys_to_drop = [ 'type','uri', 'track_href', 'analysis_url']

    features = sp.audio_features(ids)

    for i in range(len(features)):
        for j in keys_to_drop:
            del features[i][j]

        cols = features[i].items()

        for y in cols:
            df.loc[i, y[0]] = y[1]




df = pd.read_csv("spot_test.csv")
ids = df["id"]


get_audio_features(df,ids)


def main():
    get_audio_features()

if __name__ == "__main___":
    get_audio_features()