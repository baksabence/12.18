class Renszarvas:

    def __init__(self, nev: str, magassag: str, hely: str, leiras:str):
        self.nev = nev
        nevdarabolt = nev.split(" – ")
        self.nevangol = nevdarabolt[0]
        self.nevmagyar = nevdarabolt[1]
        self.magassag = int(magassag)
        self.hely = int(hely)
        self.leiras = leiras

    def kiir(self) -> str:
        return f"Rénszarvas neve: {self.nev}, Magassága: {self.magassag}."

    def __str__(self) :
        return f"Rénszarvas adatai : Angol név: {self.nevangol}, Magyar név: {self.nevmagyar}, Magasság: {self.magassag}, Sorban elfoglalt helye: {self.hely}. Leírás: {self.leiras} "