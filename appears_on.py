# mel fucking around

# WIP .... to be cleaned + integrated + file will be deleted once integrated

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from typing import Tuple

cid = "4b7803f7994c463e9b7143eeafc2d3ee"
secret = "6eda60dc39b04d2c9c39e5c4beb58963"
client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

ARTIST = "spotify:artist:1McMsnEElThX1knmY4oliG" 
artistname = spotify.artist(ARTIST)['name']

albums = spotify.artist_albums(ARTIST)
collab = set()
for album in albums['items']:
    if album['album_group'] == 'appears_on':
        uri = album['uri']
        tracks = spotify.album_tracks(uri)['items'] # need to fix offset
                                                    # working for smaller artists
        for track in tracks:
            artists = [artist["name"] for artist in track["artists"]]
            if len(artists) > 1 and artistname in artists:
                collab.update(artists)
                collab.remove(artistname)

print(collab)
