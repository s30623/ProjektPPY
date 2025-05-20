class Film:
    def __init__(self, tytul, rezyser, rok_produkcji, gatunek, status, ocena, opis) -> None:
        self.tytul: str = tytul
        self.rezyser: str = rezyser
        self.rok_produkcji: int = rok_produkcji
        self.gatunek: str = gatunek
        self.status: str = status
        self.ocena: float = ocena
        self.opis: str = opis

    gatunki = ("horror", "bajka", "science-fiction",
               "kreskówka", "komedia", "akcji",
               "dramat","musical", "przyrodniczy",
               "melodramat", "fantasy", "kryminał",
               "thriller", "historyczny", "psychologiczny",
               "anime", "inny")
