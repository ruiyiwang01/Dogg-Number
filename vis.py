import pyvis as pv
from pyvis.network import Network
import networkx as nx

from artist_graph import ArtistGraph

def create_graph(artist_data, n):
    pvNet = Network(height="100%", width="100%")
    netxG = nx.Graph()
    pvNet.add_node(artist_data.artist_name)

    related_artists = artist_data.get_n_related_artists(n)
    for artist_info in related_artists:
        artist_name = artist_info  # No need to unpack, as it's a single value
        pvNet.add_node(artist_name)
        pvNet.add_edge(artist_data.artist_name, artist_name)

    # print(pvNet.generate_html())
    pvNet.from_nx(netxG)

    network_data = {"nodes": pvNet.nodes, "edges": pvNet.edges}

    # pvNet.set_options(
    #     physics=True,
    #     layout={"improvedLayout": True},
    #     edges={
    #         "color": "gray",
    #         "width": 1,
    #     },
    #     inherit_edge_colors=True,
    #     toggle_hide_nodes_on_drag=True,
    # )

    return network_data
