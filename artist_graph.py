import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from credientials import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

cid = SPOTIPY_CLIENT_ID
secret = SPOTIPY_CLIENT_SECRET
client_credentials_manager = SpotifyClientCredentials(
    client_id=cid, client_secret=secret
)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class ArtistGraph:
    def __init__(self, artist_name: str):
        """artist_name: name of the artist"""
        self.artist_name = artist_name

        # getting artist URI from artist name
        results = spotify.search(q="artist:" + artist_name, type="artist")
        items = results["artists"]["items"]
        if len(items) > 0:
            artist = items[0]
            self.artist_uri = artist["uri"]

        self.cache = {0: {self.artist_name}}
        self.cached_artists = {self.artist_name}

    def get_collabs(self, artist_name: str):
        """Get collaborator artists and song titles"""
        for idx in range(0, 1000, 20):
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
