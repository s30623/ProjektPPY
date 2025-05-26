class Film:
    def __init__(self, tytul, rezyser, rok_produkcji, gatunek, status, ocena, opis, komentarze='brak') -> None:
        self.tytul: str = tytul
        self.rezyser: str = rezyser
        self.rok_produkcji: int = rok_produkcji
        self.gatunek: str = gatunek
        self.status: str = status
        self.ocena: float = ocena
        self.opis: str = opis
        self.komentarze: str = komentarze

    gatunki = ("horror", "bajka", "science-fiction",
               "kreskówka", "komedia", "akcji",
               "dramat","musical", "przyrodniczy",
               "melodramat", "fantasy", "kryminał",
               "thriller", "historyczny", "psychologiczny",
               "anime", "inny")

    def __str__(self):
        return (
            f"Tytuł: {self.tytul}\n"
            f"Reżyser: {self.rezyser}\n"
            f"Rok produkcji: {self.rok_produkcji}\n"
            f"Gatunek: {self.gatunek}\n"
            f"Status: {self.status}\n"
            f"Ocena: {self.ocena}\n"
            f"Opis: {self.opis}\n"
            f"Komentarz: {self.komentarze}\n"
        )