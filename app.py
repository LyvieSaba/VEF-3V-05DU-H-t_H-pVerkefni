from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
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