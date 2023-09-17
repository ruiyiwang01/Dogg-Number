import pyvis as pv
from pyvis.network import Network
import networkx as nx

from artist_graph import ArtistGraph

def create_graph(artist_data):
    query_artist = artist_data.artist_name

    pvNet = Network(height="800px", width="100%")
    netxG = nx.Graph()

    connections = []

    for layer in artist_data.cache.keys():
        for collab_artist in artist_data.cache[layer]:
            netxG.add_node(collab_artist, label=f"{query_artist} Number: {layer}")
            connections.append((query_artist, collab_artist))

    netxG.add_edges_from(connections)
    pvNet.from_nx(netxG)

    pvNet.set_options(
        physics=True,
        layout={"improvedLayout": True},
        edges={
            "color": "gray",
            "width": 1,
        },
        inherit_edge_colors=True,
        toggle_hide_nodes_on_drag=True,
    )

    return pvNet