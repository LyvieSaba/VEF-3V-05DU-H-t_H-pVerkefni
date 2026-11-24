import random

class Game:

    def __init__(self, id, name, min_players, max_players, minutes, rules):
        self.id = id
        self.name = name
        self.min_players = min_players
        self.max_players = max_players
        self.minutes = minutes
        self.rules = rules  # a list of steps, one string per step

    def to_dict(self):
        """The game as a dictionary, so Flask can send it as JSON."""
        return {
            "id": self.id,
            "name": self.name,
            "min_players": self.min_players,
            "max_players": self.max_players,
            "minutes": self.minutes,
            "rules": self.rules,
        }

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


# The starting games. They are copied into the database the first time the app runs.
SAMPLE_GAMES = [
    Game(1, "Ólsen ólsen", 2, 6, 15, [
        "Hver leikmaður fær 7 spil (5 ef þið eruð fleiri en 4).",
        "Eitt spil fer upp í loft, restin er bunki.",
        "Settu út spil í sömu sort eða sama gildi og efsta spilið.",
        "Áttan má fara á allt og þá velur þú nýja sort.",
        "Segðu „Ólsen“ þegar þú átt eitt spil eftir og „Ólsen ólsen“ þegar þú klárar.",
    ]),
    Game(2, "Kani", 2, 4, 10, ["Reglur koma síðar."]),
    Game(3, "Rommí", 2, 6, 45, [
        "Hver leikmaður fær 7 spil (10 ef þið eruð bara 2).",
        "Eitt spil fer upp í loft í kastbunka, restin er dráttarbunki.",
        "Í hverri umferð dregur þú eitt spil, annaðhvort úr bunkanum eða kastbunkanum.",
        "Leggðu niður sett: þrjú eða fjögur spil með sama gildi, eða röð í sömu sort (t.d. 5-6-7 í hjarta).",
        "Þú mátt líka bæta spilum við sett sem eru þegar á borðinu.",
        "Endaðu umferðina á því að kasta einu spili í kastbunkann.",
        "Sá sem losnar fyrst við öll spilin sín vinnur.",
    ]),
    Game(4, "Kapall", 1, 1, 10, [
        "Leggðu 7 bunka á borðið: 1 spil í þann fyrsta, 2 í næsta og svo framvegis upp í 7. Efsta spilið í hverjum bunka snýr upp.",
        "Restin af spilunum er dráttarbunki.",
        "Markmiðið er að raða öllum spilunum í 4 bunka, einn fyrir hverja sort, frá ás upp í kóng.",
        "Á borðinu má setja spil á spil sem er einu hærra og í öðrum lit (t.d. rauða 6 á svarta 7).",
        "Aðeins kóngur má fara á autt pláss.",
        "Þegar þú kemst ekki lengra, dragðu spil úr bunkanum.",
    ]),
    Game(5, "Svarti Pétur", 2, 6, 15, [
        "Takið eina laufadrottningu úr stokknum. Spaðadrottningin er Svarti Pétur.",
        "Gefið öll spilin. Leggið niður öll pör sem þið eigið.",
        "Í hverri umferð dregur þú eitt spil af hendi leikmannsins við hliðina á þér, án þess að sjá það.",
        "Ef þú færð par leggur þú það niður.",
        "Sá sem situr uppi með Svarta Pétur í lokin tapar.",
    ]),
    Game(6, "Veiðimaður", 2, 6, 15, [
        "Hver leikmaður fær 5 spil (7 ef þið eruð bara 2). Restin er bunki í miðjunni.",
        "Spyrðu einhvern um gildi sem þú átt sjálf/ur, t.d. „Áttu sjöu?“",
        "Ef viðkomandi á það þarf að láta þig fá öll þau spil og þú mátt spyrja aftur.",
        "Ef ekki er sagt „Veiddu!“ og þú dregur spil úr bunkanum.",
        "Þegar þú átt öll fjögur spilin af einu gildi leggur þú þau niður.",
        "Sá sem á flest fjögurra spila sett í lokin vinnur.",
    ]),
    Game(7, "Stríð", 2, 2, 20, [
        "Skiptið stokknum jafnt á milli ykkar. Enginn má skoða spilin sín.",
        "Báðir snúa efsta spilinu sínu upp á sama tíma.",
        "Sá sem á hærra spil tekur bæði spilin og setur þau undir bunkann sinn.",
        "Ef spilin eru jafn há er stríð: hvor leggur 3 spil á hvolf og snýr því fjórða upp. Hærra spilið vinnur allt.",
        "Sá sem eignast öll spilin vinnur.",
    ]),
]

# Used by the tests, and as a backup if there is no database
library = GameLibrary(SAMPLE_GAMES)