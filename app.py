from flask import Flask, jsonify, request, abort, render_template
from models import db, Player, Game, GamePlayer, Move

app = Flask(__name__)
app.json.ensure_ascii = False

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cardgames.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

# Sample games until the real database is ready.
GAMES = [
    {"id": 1, "name": "Ólsen ólsen", "min_players": 2, "max_players": 6, "minutes": 15},
    {"id": 2, "name": "Kani", "min_players": 2, "max_players": 4, "minutes": 10},
    {"id": 3, "name": "Rommí", "min_players": 2, "max_players": 6, "minutes": 45},
    {"id": 4, "name": "Kapall", "min_players": 1, "max_players": 1, "minutes": 10},
]

def find_games(text="", players=None, max_minutes=None):
    results = []
    for game in GAMES:
        if text and text.lower() not in game["name"].lower():
            continue
        if players is not None and not (game["min_players"] <= players <= game["max_players"]):
            continue
        if max_minutes is not None and game["minutes"] > max_minutes:
            continue
        results.append(game)
    return results

@app.route("/")
def index():
    return render_template("example.html")

@app.route("/leit")
def search():
    text = request.args.get("q", "")
    players = request.args.get("players", type=int)
    max_minutes = request.args.get("time", type=int)

    query = Game.query
    if text:
        query = query.filter(Game.name.ilike(f"%{text}%"))

    games = query.all()
    return jsonify([
        {"id": g.id, "name": g.name, "game_type": g.game_type, "status": g.status}
        for g in games
    ])

@app.route("/spil/<int:game_id>")
def game(game_id):
    for g in GAMES:
        if g["id"] == game_id:
            return jsonify(g)
    abort(404)

@app.route('/api/add-dummy-data')
def add_dummy_data():
    player = Player(username="alice", email="alice@example.com")
    game = Game(name="Test Game", game_type="poker")
    db.session.add(player)
    db.session.add(game)
    db.session.commit()
    return {"message": "Dummy data added"}

@app.route('/api/games')
def get_games():
    games = Game.query.all()
    return [{"id": g.id, "name": g.name, "status": g.status} for g in games]

@app.route('/api/create-game', methods=['POST'])
def create_game():
    data = request.get_json() or {}
    game = Game(
        name=data.get('name', 'Nýr leikur'),
        game_type=data.get('game_type', 'poker')
    )
    db.session.add(game)
    db.session.commit()
    return {"message": "Leikur búinn til", "id": game.id}

@app.route('/api/join-game', methods=['POST'])
def join_game():
    data = request.get_json() or {}
    gp = GamePlayer(
        game_id=data.get('game_id'),
        player_id=data.get('player_id'),
        seat=data.get('seat', 1),
        chips=1000
    )
    db.session.add(gp)
    db.session.commit()
    return {"message": "Leikmaður bætt við leik"}

@app.route('/api/add-move', methods=['POST'])
def add_move():
    data = request.get_json() or {}
    move = Move(
        game_id=data.get('game_id'),
        player_id=data.get('player_id'),
        card=data.get('card'),
        action=data.get('action', 'play')
    )
    db.session.add(move)
    db.session.commit()
    return {"message": "Hreyfing skráð", "card": move.card}

if __name__ == "__main__":
    app.run(debug=True)