import Film
from MyException import *
class Kolekcja:
    def __init__(self) -> None:
        self.filmy = list() #lista filmow

    def sprawdzCzyFilmIstnieje(self,film:Film) -> True | False:
        for film_z_kolekcji in self.filmy:
            tytul_ten_sam = film.tytul.lower().strip() == film_z_kolekcji.tytul.lower().strip()
            rezyser_ten_sam = film.rezyser.lower().strip() == film_z_kolekcji.rezyser.lower().strip()
            rok_ten_sam = film.rok_produkcji == film_z_kolekcji.rok_produkcji

            if tytul_ten_sam and rezyser_ten_sam and rok_ten_sam:
                return True
        return False
    def dodajFilm(self,tytul,rezyser,rok_produkcji,gatunek,status,ocena,opis) -> None:
        try:
            film = Film.Film(tytul=tytul,rezyser=rezyser,rok_produkcji=rok_produkcji,gatunek=gatunek,status=status,ocena=ocena,opis=opis)
            if self.sprawdzCzyFilmIstnieje(film):
                raise MovieAlreadyExists
            self.filmy.append(film)
        except MovieAlreadyExists:
            print("Film juz istnieje w kolekcji")

    def wyswietlKolekcje(self) -> list[str]:
        for id, film in enumerate(self.filmy):
            print(f"[{id + 1}] Tytul: {film.tytul} \n-Rok: {film.rok_produkcji} \n-Gatunek: {film.gatunek} \n-Status: {film.status} \n-Ocena: {film.ocena}")
        return self.filmy

    def usunFilm(self,film:Film) -> str:
        try:
            for film_z_kolekcji in self.filmy:
                if(film_z_kolekcji.tytul.lower().strip() == film.tytul.lower().strip()):
                    self.filmy.remove(film_z_kolekcji)
                    return "Udało usunąc się film z kolekcji"
                else :
                    raise MovieDoesNotExist

        except MovieDoesNotExist:
            print("Nie udało się usunąć filmu z ")

    def editFilm(self,film:Film) -> None:
        for film_z_kolekcji in self.filmy:
            pass
