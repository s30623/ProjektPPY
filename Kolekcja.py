import Film
from MyException import *

class Kolekcja:
    def __init__(self,sciezka:str=None) -> None:
        self.filmy = list()  # lista filmow
        if sciezka is not None:
            try:
                if ".csv" not in sciezka:
                    raise InvalidFileFormat
                with open(sciezka) as f:
                    for linijka in f.readlines():
                        podziel:list[str] = linijka.split(";")
                        self.dodajFilm(tytul=podziel[0],
                                       rezyser=podziel[1],
                                       rok_produkcji=int(podziel[2]),
                                       gatunek=podziel[3],
                                       status=podziel[4],
                                       ocena=int(podziel[5]),
                                       opis=podziel[6])
            except InvalidFileFormat:
                print("Lista nie jest w csv")
            except FileNotFoundError:
                print("Nie znaleziono listy")
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
            print(f"Film {film.tytul} juz istnieje w kolekcji")

    def wyswietlKolekcje(self) -> list[str]:
        print("\n-----------------------------------\n")
        for id, film in enumerate(self.filmy):
            print(f"[{id + 1}] Tytul: {film.tytul} \n-Rok: {film.rok_produkcji} \n-Gatunek: {film.gatunek} \n-Status: {film.status} \n-Ocena: {film.ocena}")
        print("\n-----------------------------------\n")
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

    def edytujFilm(self,film:Film) -> None:
        for film_z_kolekcji in self.filmy:
            pass
