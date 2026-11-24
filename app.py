from flask import Flask, request, abort, render_template, redirect, url_for, jsonify

from games import library

app = Flask(__name__)
app.json.ensure_ascii = False  # show Icelandic letters properly


@app.route("/")
def index():
    # The home page our HTML/CSS teammates made
    return render_template("base.html")


@app.route("/leit")
def search():
    # Example: /leit?q=kan&players=3&time=20
    # Returns JSON until the HTML team makes templates/leit.html
    text = request.args.get("q", "")
    players = request.args.get("players", type=int)
    max_minutes = request.args.get("time", type=int)
    games = library.search(text, players, max_minutes)
    return jsonify([game.to_dict() for game in games])


@app.route("/spil/<int:game_id>")
def game_page(game_id):
    # Example: /spil/1 shows the game with id 1
    # Returns JSON until the HTML team makes templates/spil.html
    found = library.get(game_id)
    if found is None:
        abort(404)
    return jsonify(found.to_dict())


@app.route("/handahof")
def random_game():
    # Picks a random game and sends the user to its page
    picked = library.random_game()
    return redirect(url_for("game_page", game_id=picked.id))


if __name__ == "__main__":
    app.run(debug=True)