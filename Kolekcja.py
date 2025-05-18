import Film
class Kolekcja:
    def __init__(self) -> None:
        self.filmy = set()
    def dodajFilm(self,tytul,rezyser,rok_produkcji,gatunek,status,ocena,opis) -> None:
        film = Film.Film(tytul=tytul,rezyser=rezyser,rok_produkcji=rok_produkcji,gatunek=gatunek,status=status,ocena=ocena,opis=opis)
        if film not in self.filmy:
            self.filmy.add(film)
        else:
            print("Film juz istnieje")