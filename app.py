from flask import Flask, render_template, request
from artist_graph import ArtistGraph
from vis import create_graph

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        singer_name = request.form["singer_name"]
        degree = request.form.get("singer_num")
        artist_data = ArtistGraph(singer_name) # Calculate artist numbers
        for i in range(1, degree):
            artist_data.get_n_artists(i)
        graph = create_graph(artist_data)    # Create Pyvis graph
        return render_template("result.html", graph=graph)
    return render_template("input.html")

if __name__ == "__main__":
    app.run(debug=True)
