import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from typing import Optional

cid = "4b7803f7994c463e9b7143eeafc2d3ee"
secret = "6eda60dc39b04d2c9c39e5c4beb58963"
client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class ArtistGraph:
    def __init__(self, artist: str, n: Optional[int] = None):
        """artist: name of the artist
        n: the 'Bacon' number you want, defaults to None"""
        self.artist = artist
        self.n = n
        self.collaborators, self.collab_songs = self.get_collabs()

    def get_collabs(self):
        """Get collaborator artists and song titles"""
        collaborators = set()
        collab_songs = set()
        for idx in range(0, 10000, 50):
            try:
                track_results = spotify.search(
                    q=f"artist:{self.artist}", limit=50, type="track", offset=idx
                )
            except:
                break
            for i, t in enumerate(track_results["tracks"]["items"]):
                if len(t["artists"]) > 1:
                    for artist in t["artists"]:
                        collaborators.add(artist["name"])
                    collab_songs.add(t["name"])
        collaborators.remove(self.artist)
        return collaborators, collab_songs
