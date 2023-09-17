from pyvis.network import Network

def create_related_artist_pyvis_graph(related_artist_graph, n, output_file):
    net = Network()
    net.add_node(related_artist_graph.artist_name)

    related_artists = related_artist_graph.get_n_related_artists(n)
    for artist_info in related_artists:
        artist_name = artist_info  # No need to unpack, as it's a single value
        net.add_node(artist_name)
        net.add_edge(related_artist_graph.artist_name, artist_name)

    net.save_graph(output_file)
