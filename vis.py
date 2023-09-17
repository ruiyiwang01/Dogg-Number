from pyvis.network import Network


def create_graph(artist_data, n):
    pvNet = Network(height="100%", width="100%")

    artist_data.get_n_related_artists(n)
    for layer_num in artist_data.cache:
        for artist_name, _ in artist_data.cache[layer_num]:
            pvNet.add_node(artist_name)
            if artist_data.parents[artist_name]:
                pvNet.add_edge(artist_name, artist_data.parents[artist_name])

    network_data = {"nodes": pvNet.nodes, "edges": pvNet.edges}

    return network_data
