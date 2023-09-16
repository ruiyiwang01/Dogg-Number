import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = "4b7803f7994c463e9b7143eeafc2d3ee"
secret = "6eda60dc39b04d2c9c39e5c4beb58963"
client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class ArtistGraph:
    def __init__(self, artist_name: str):
        """artist_name: name of the artist"""
        self.artist_name = artist_name
        self.cache = {0: {self.artist_name}}
        self.cached_artists = {self.artist_name}

    def get_collabs(self, artist_name: str):
        """Get collaborator artists"""
        for idx in range(0, 1000, 50):
            try:
                track_results = spotify.search(
                    q=f"artist:{artist_name}", limit=50, type="track", offset=idx
                )
            except:
                break
            for t in track_results["tracks"]["items"]:
                if len(t["artists"]) > 1:
                    for artist in t["artists"]:
                        collab_artist_name = artist.get("name", "")
                        if collab_artist_name not in self.cached_artists:
                            self.cached_artists.add(collab_artist_name)
                            yield collab_artist_name

    def get_n_artists(self, n: int) -> set:
        """Get collaborators that are n away from main artist"""
        if n in self.cache:
            return self.cache[n]
        layer_num = max(self.cache.keys())
        cur_layer = self.cache[layer_num]
        while cur_layer:
            if n in self.cache:
                return self.cache[n]
            layer_num += 1
            next_layer = set()
            for artist in cur_layer:
                for collab_artist in self.get_collabs(artist):
                    next_layer.add(collab_artist)
            self.cache[layer_num] = next_layer
            cur_layer = next_layer
        self.cache[layer_num] = set()
        return self.cache[layer_num]
