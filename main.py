from artist_graph import ArtistGraph
from related_artists_graph import RelatedArtistGraph
import time

# test cases
related_artist_graph = RelatedArtistGraph("Snoop Dogg")
t1 = time.time()
print(related_artist_graph.get_n_related_artists(1))
t2 = time.time()
print(f"Time taken: {t2-t1}")

t1 = time.time()
print(related_artist_graph.get_n_related_artists(2))
t2 = time.time()
print(f"Time taken: {t2-t1}")

t1 = time.time()
print(related_artist_graph.get_n_related_artists(3))
t2 = time.time()
print(f"Time taken: {t2-t1}")

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
