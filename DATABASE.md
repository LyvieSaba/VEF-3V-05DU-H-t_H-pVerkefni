# Gagnagrunnur – SQLite + Flask-SQLAlchemy

## Af hverju SQLite?
SQLite er mælt með í námskeiðinu fyrir einfaldar gagnagrunnstengdar veflausnir.
- Enginn aukahugbúnaður þarf að setja upp
- Gagnagrunnurinn er ein skrá (`cardgames.db`)
- Fullkomlega samhæft við Flask og OOP (klasarnir eru módel)

## Módel
- **Player** – leikmenn
- **Game** – leikir
- **GamePlayer** – tenging milli leikmanns og leiks
- **Move** – skrá yfir hreyfingar í leik

## Hvernig á að keyra
```bash
pip install -r requirements.txt
python app.py