from artist_graph import ArtistGraph
import time
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = "4b7803f7994c463e9b7143eeafc2d3ee"
secret = "6eda60dc39b04d2c9c39e5c4beb58963"
client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

artist_graph = ArtistGraph("Taylor Swift")
# test cases
t1 = time.time()
print(artist_graph.get_n_artists(1))
t2 = time.time()
print(f"Time taken: {t2-t1}")

t1 = time.time()
print(artist_graph.get_n_artists(2))
t2 = time.time()
print(f"Time taken: {t2-t1}")

t1 = time.time()
print(artist_graph.get_n_artists(1))
t2 = time.time()
print(f"Time taken: {t2-t1}")
