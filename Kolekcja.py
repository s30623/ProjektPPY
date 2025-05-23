import Film
from MyException import *


class Kolekcja:
    def __init__(self, sciezka: str = None) -> None:
        self.filmy = list()  # lista filmow
        if sciezka is not None:
            try:
                if ".csv" not in sciezka:
                    raise InvalidFileFormat
                with open(sciezka) as f:
                    for linijka in f.readlines():
                        podziel: list[str] = linijka.split(";")
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

    def sprawdzCzyFilmIstnieje(self, film: Film) -> True | False:
        for film_z_kolekcji in self.filmy:
            tytul_ten_sam = film.tytul.lower().strip() == film_z_kolekcji.tytul.lower().strip()
            rezyser_ten_sam = film.rezyser.lower().strip() == film_z_kolekcji.rezyser.lower().strip()
            rok_ten_sam = film.rok_produkcji == film_z_kolekcji.rok_produkcji

            if tytul_ten_sam and rezyser_ten_sam and rok_ten_sam:
                return True
        return False

    def dodajFilm(self, tytul, rezyser, rok_produkcji, gatunek, status, ocena, opis) -> None:
        try:
            film = Film.Film(tytul=tytul, rezyser=rezyser, rok_produkcji=rok_produkcji, gatunek=gatunek, status=status,
                             ocena=ocena, opis=opis)
            if self.sprawdzCzyFilmIstnieje(film):
                raise MovieAlreadyExists
            self.filmy.append(film)
        except MovieAlreadyExists:
            print(f"Film {film.tytul} juz istnieje w kolekcji")

    def wyswietlKolekcje(self) -> None:
        print("\n-----------------------------------\n")
        for id, film in enumerate(self.filmy):
            print(
                f"[{id + 1}] Tytul: {film.tytul} \n-Rok: {film.rok_produkcji} \n-Gatunek: {film.gatunek} \n-Status: {film.status} \n-Ocena: {film.ocena}")
        print("\n-----------------------------------\n")
        #return self.filmy

    def usunFilm(self, film: Film) -> str:
        try:
            for film_z_kolekcji in self.filmy:
                if (film_z_kolekcji.tytul.lower().strip() == film.tytul.lower().strip()):
                    self.filmy.remove(film_z_kolekcji)
                    return "Udało usunąc się film z kolekcji"

            raise MovieDoesNotExist

        except MovieDoesNotExist:
            print("Nie udało się usunąć filmu z ")

    def edytujFilm(self, film: Film) -> None:
        print(f"Co chcesz zedytowac w filmie: {film.tytul}")
        print("1. Tytul")
        print("2. Rezyser")
        print("3. Rok produkcji")
        print("4. Gatunek")
        print("5. Status")
        print("6. Ocena")
        print("7. Opis")
        match input():
            case "1":
                print(f"Obecny tytul: {film.tytul}")
                kopia_tytulu = film.tytul
                try:
                    film.tytul = input("Podaj nowy tutyl filmu:\n")
                    if self.sprawdzCzyFilmIstnieje(film):
                        raise MovieAlreadyExists
                except MovieAlreadyExists:
                    print(f"Film {film.tytul} juz istnieje w kolekcji, podaj inny tutul")
                    film.tytul = kopia_tytulu
            case "2":
                print(f"Obecny rezyser: {film.rezyser}")
                film.rezyser = input("Podaj nowego rezysera:\n")
            case "3":
                print(f"Obecny rok produkcji: {film.rok_produkcji}")
                film.rok_produkcji = input("Podaj nowy rok produkcji")
            case "4":
                print(f"Obecny Gatunek: {film.gatunek}")
                kopia_gatunku = film.gatunek
                try:
                    nowy_gatunek = input("Podaj nowy gatunek:\n")
                    if nowy_gatunek not in Film.Film.gatunki:
                        raise InvalidMovieType
                    film.gatunek = nowy_gatunek
                except:
                    print(f"Podany gatunek nie istnieje")
                    print("Gatunki: ", Film.Film.gatunki)
                    film.gatunek = kopia_gatunku
            case "5":
                print(f"Obecny status: {film.status}")
                status = input("Podaj nowy status: obejrzany/nieobejrzany\n")
                try:
                    if not (status.lower().strip() == "obejrzany" or status.lower().strip() == "nieobejrzany"):
                        raise WrongStatus
                    film.status = status
                except WrongStatus:
                    print("Podano zly status:")
            case "6":
                print(f"Obecna ocena {film.ocena}")
                try:
                    nowa_ocena = int(input("Podaj nową ocenę"))
                    if nowa_ocena < 1 or nowa_ocena > 10:
                        raise InvalidRatingScale
                    film.ocena = nowa_ocena
                except InvalidRatingScale:
                    print("Ocena nie jest w zakresie od 1 do 10")
                except Exception as e:
                    print(e)
            case "7":
                print(f"Obecny opis: {film.opis}")
                film.opis = input("\nPodaj nowy opis:\n")

    def exportujDoPliku(self):
        try:
            with open(input("Podaj nazwe pliku:\n") + ".csv","w") as w:
                for film in self.filmy:
                    linijka = f"{film.tytul};{film.rezyser};{film.rok_produkcji};{film.gatunek};{film.status};{film.ocena};{film.opis}"
                    w.write(linijka)
        except Exception as e:
            print(e)