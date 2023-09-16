from artist_graph import ArtistGraph

artist_graph = ArtistGraph("Snoop Dogg")
collaborators = artist_graph.collaborators
collabs = artist_graph.get_n_artists(2)
