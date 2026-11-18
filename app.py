from flask import Flask, request, abort, render_template, redirect, url_for
from games import library

app = Flask(__name__)


@app.route("/")
def index():
    # Shows the page your teammates made in templates/example.html
    return render_template("example.html")


@app.route("/leit")
def search():
    # Example: /leit?q=kan&players=3&time=20
    text = request.args.get("q", "")
    players = request.args.get("players", type=int)
    max_minutes = request.args.get("time", type=int)
    games = library.search(text, players, max_minutes)
    return render_template("leit.html", games=games, q=text, players=players, time=max_minutes)


@app.route("/spil/<int:game_id>")
def games(game_id):
    # Example: /spil/1 shows the games with id 1
    found = library.get(game_id)
    if found is None:
        abort(404)
    return render_template("example.html", games=found)


@app.route("/handahof")
def random_game():
    # Picks a random game and sends the user to its page
    picked = library.random_game()
    return redirect(url_for("games", game_id=picked.id))


if __name__ == "__main__":
    app.run(debug=True)