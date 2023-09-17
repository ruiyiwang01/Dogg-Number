# Import necessary libraries
from related_artists_graph import RelatedArtistGraph

# Import the Pyvis-related functions
from create_pyvis_graph import create_related_artist_pyvis_graph

# Test cases
related_artist_graph = RelatedArtistGraph("Snoop Dogg")

# Generate a Pyvis graph for a specific value of n (e.g., n=2)
n = 3
pyvis_graph_file = f"related_artist_graph_n_{n}.html"
create_related_artist_pyvis_graph(related_artist_graph, n, pyvis_graph_file)
