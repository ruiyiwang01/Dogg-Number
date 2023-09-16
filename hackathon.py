import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = "4b7803f7994c463e9b7143eeafc2d3ee"
secret = "6eda60dc39b04d2c9c39e5c4beb58963"
client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

snoopdogg_uri = "spotify:artist:7hJcb9fa4alzcOq3EaNPoG"

collaborators = set()
for idx in range(0, 10000, 50):
    try:
        track_results = spotify.search(
            q="artist:Snoop Dogg", limit=50, type="track", offset=idx
        )
    except:
        break
    for i, t in enumerate(track_results["tracks"]["items"]):
        if len(t["artists"]) > 1:
            for artist in t["artists"]:
                if artist["name"] != "Snoop Dogg":
                    collaborators.add(artist["name"])
print(collaborators)
