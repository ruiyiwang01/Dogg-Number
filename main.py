from artist_graph import ArtistGraph
import time

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
