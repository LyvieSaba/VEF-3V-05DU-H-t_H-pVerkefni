import random

class Game:

    def __init__(self, id, name, min_players, max_players, minutes, rules):
        self.id = id
        self.name = name
        self.min_players = min_players
        self.max_players = max_players
        self.minutes = minutes
        self.rules = rules  # a list of steps, one string per step

    def fits_players(self, players):
        """True if this many people can play the game."""
        return self.min_players <= players <= self.max_players

    def matches(self, text="", players=None, max_minutes=None):
        """True if the game matches the search text and filters"""
        if text and text.lower() not in self.name.lower():
            return False
        if players is not None and not self.fits_players(players):
            return False
        if max_minutes is not None and self.minutes > max_minutes:
            return False
        return True


class GameLibrary:
    """All the games with ways to search and look them up"""

    def __init__(self, games):
        self.games = games

    def search(self, text="", players=None, max_minutes=None):
        """Return a list of the games that match."""
        return [game for game in self.games if game.matches(text, players, max_minutes)]

    def get(self, game_id):
        """Return the game with this id or None if it doesnt exist"""
        for game in self.games:
            if game.id == game_id:
                return game
        return None

    def random_game(self):
        """Return one random game"""
        return random.choice(self.games)




# placeholder games until the real database is made/ready
library = GameLibrary([
    Game(1, "Ólsen ólsen", 2, 6, 15, [
        "Hver leikmaður fær 7 spil (5 ef þið eruð fleiri en 4).",
        "Eitt spil fer upp í loft, restin er bunki.",
        "Settu út spil í sömu sort eða sama gildi og efsta spilið.",
        "Áttan má fara á allt og þá velur þú nýja sort.",
        "Segðu „Ólsen“ þegar þú átt eitt spil eftir og „Ólsen ólsen“ þegar þú klárar.",
    ]),
    Game(2, "Kani", 2, 4, 10, ["Reglur koma síðar."]),
    Game(3, "Rommí", 2, 6, 45, ["Reglur koma síðar."]),
    Game(4, "Kapall", 1, 1, 10, ["Reglur koma síðar."]),
])