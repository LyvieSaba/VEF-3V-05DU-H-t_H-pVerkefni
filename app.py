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