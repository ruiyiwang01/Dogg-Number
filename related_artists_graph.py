import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

cid = "4b7803f7994c463e9b7143eeafc2d3ee"
secret = "6eda60dc39b04d2c9c39e5c4beb58963"
client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class RelatedArtistGraph:
    def __init__(self, artist_name: str):
        """artist_name: name of the artist"""
        self.artist_name = artist_name
        self.artist_uri = spotify.search(
            q=f"artist:{self.artist_name}", limit=1, type="artist"
        )["artists"]["items"][0]["uri"]
        self.cache = {0: {(self.artist_name, self.artist_uri)}}
        self.cached_artists = {self.artist_name}
        self.parents = {self.artist_name: None}

    def get_related_artists(self, artist_uri: str):
        """Get related artists"""
        related_artists = spotify.artist_related_artists(artist_uri)
        for related_artist in related_artists["artists"]:
            if related_artist["name"] not in self.cached_artists:
                self.cached_artists.add(related_artist["name"])
                yield related_artist["name"], related_artist["uri"]

    def get_n_related_artists(self, n: int) -> set:
        """Get related artists that are n away from main artist"""
        if n in self.cache:
            return [name for name, _ in self.cache[n]]
        layer_num = max(self.cache.keys())
        cur_layer = self.cache[layer_num]
        while cur_layer:
            if n in self.cache:
                return [name for name, _ in self.cache[n]]
            layer_num += 1
            next_layer = set()
            for artist_name, artist_uri in cur_layer:
                for related_artist_name, related_artist_uri in self.get_related_artists(
                    artist_uri
                ):
                    self.parents[related_artist_name] = artist_name
                    next_layer.add((related_artist_name, related_artist_uri))
            self.cache[layer_num] = next_layer
            cur_layer = next_layer
        self.cache[layer_num] = set()
        return self.cache[layer_num]
