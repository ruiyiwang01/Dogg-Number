from flask import Flask, render_template, request
from related_artists_graph import RelatedArtistGraph
from vis import create_graph
import json

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer_name = request.form["singer_name"]
        degree = int(request.form["singer_num"])
        artist_data = RelatedArtistGraph(singer_name)  # Calculate artist numbers
        network_data = create_graph(artist_data, degree)  # Create Pyvis graph
        return render_template(
            "result.html", network_data_json=json.dumps(network_data)
        )
    return render_template("input.html")


if __name__ == "__main__":
    app.run(debug=True)
