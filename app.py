from flask import Flask, render_template, request, redirect, url_for, session
from related_artists_graph import RelatedArtistGraph
from vis import create_graph
import json
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer_name = request.form["singer_name"]
        degree = int(request.form["singer_num"])
        artist_data = RelatedArtistGraph(singer_name)  # Calculate artist numbers
        network_data = create_graph(artist_data, degree)  # Create Pyvis graph
        session["network_data_json"] = json.dumps(network_data)
        return redirect(url_for("get_graph"))
    return render_template("input.html")


@app.route("/network", methods=["GET"])
def get_graph():
    network_data_json = session.get("network_data_json", None)
    if network_data_json is not None:
        return render_template("result.html", network_data_json=network_data_json)
    else:
        # Handle the case where network_data is not provided
        return "Network data not found"


if __name__ == "__main__":
    app.run(debug=True)
