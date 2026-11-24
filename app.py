from flask import Flask, request, abort, render_template, redirect, url_for, jsonify

from games import library

app = Flask(__name__)
app.json.ensure_ascii = False  # show Icelandic letters properly


@app.route("/")
def index():
    # For now the home page sends you to my test page
    return redirect(url_for("test_page"))


@app.route("/leit")
def search():
    # Example: /leit?q=kan&players=3&time=20&flokkur=Fjölskylduspil
    # Returns JSON until the HTML team makes templates/leit.html
    text = request.args.get("q", "")
    players = request.args.get("players", type=int)
    max_minutes = request.args.get("time", type=int)
    category = request.args.get("flokkur")
    games = library.search(text, players, max_minutes, category)
    return jsonify([game.to_dict() for game in games])


@app.route("/flokkar")
def categories():
    # Lists all categories, e.g. for the category cards on the home page
    return jsonify(library.categories())


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

@app.route("/test")
def test_page():
    # My test copy of base.html: the home page and search results on one page
    # Example: /test?q=kan&players=3&time=20&flokkur=Fjölskylduspil
    text = request.args.get("q", "")
    players = request.args.get("players", type=int)
    max_minutes = request.args.get("time", type=int)
    category = request.args.get("flokkur")
    games = library.search(text, players, max_minutes, category)
    return render_template("test.html", categories=library.categories(), games=games)

if __name__ == "__main__":
    app.run(debug=True)