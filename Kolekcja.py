import statistics
from collections import defaultdict

from matplotlib import pyplot as plt

import Film
from MyException import *


class Kolekcja:
    def __init__(self, sciezka: str = None) -> None:
        self.filmy = list()  # lista filmow
        self.filtrTytul: str = None
        self.filtrGatunek: str = None
        self.filtrRok: int = None
        self.filtrStatus: str = None
        self.sortujAtrybut: str = None
        self.sortujKolejnosc:bool = False
        if sciezka is not None:
            try:
                if ".csv" not in sciezka:
                    raise InvalidFileFormat
                with open(sciezka, encoding="utf8") as f:
                    for linijka in f.readlines():
                        if linijka.count(";") != 6:
                            raise InvalidFileFormat
                        podziel: list[str] = linijka.split(";")
                        if not (podziel[2].isdigit() and podziel[5].isdigit()):
                            raise InvalidFileFormat
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
            except Exception as e:
                print(e)

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
        wyswietl_filmy = self.filmy[:]
        if self.sortujAtrybut is not None:
            key = None
            match self.sortujAtrybut:
                case "TYTUL":
                    key = lambda x: x.tytul
                case "ROK":
                    key = lambda x: x.rok_produkcji
                case "GATUNEK":
                    key = lambda x: x.gatunek
                case "OCENA":
                    key = lambda x: x.ocena
            wyswietl_filmy = sorted(self.filmy,key=key,reverse=self.sortujKolejnosc)
        print("\n-----------------------------------\n")
        for id, film in enumerate(wyswietl_filmy):
            filtrujTytul = self.filtrTytul is None or self.filtrTytul.lower().strip() in film.tytul.lower().strip()
            filtrujGatunek = self.filtrGatunek is None or self.filtrGatunek == film.gatunek
            filtrujRok = self.filtrRok is None or self.filtrRok == film.rok_produkcji
            filtrujStatus = self.filtrStatus is None or self.filtrStatus == film.status
            if filtrujTytul and filtrujGatunek and filtrujRok and filtrujStatus:
                print(f"[{id + 1}] {str(film)}")
                #print(f"[{id + 1}] Tytul: {film.tytul} \n-Rok: {film.rok_produkcji} \n-Gatunek: {film.gatunek} \n-Status: {film.status} \n-Ocena: {film.ocena}")
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
        print(str(film))
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
                except InvalidMovieType:
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
                    linijka = f"{film.tytul};{film.rezyser};{film.rok_produkcji};{film.gatunek};{film.status};{film.ocena};{film.opis.strip()}"
                    w.write(linijka + '\n')
        except Exception as e:
            print(e)

    def filtruj(self):
        print("Podaj na czym chcesz ustawic filtr")
        print(f"Zastosowane filtry: Tytul: {self.filtrTytul}, Gatunek: {self.filtrGatunek}, Rok produkcji: {self.filtrRok}")
        print("1. Tytul")
        print("2. Gatunek")
        print("3. Rok produkcji")
        print("4. Status")
        print("5. Wyczyść filtry")
        try:
            wybor = input("Podaj liczbe 1-5:\n")
            match wybor:
                case "1":
                    self.filtrTytul = input("Podaj tytul filmu (moze byc niepelny):\n")
                case "2":
                    print(f"Istniejace gatunki {Film.Film.gatunki}")
                    gatunek = input("Podaj gatunek filmu:\n")
                    if gatunek.lower().strip() not in Film.Film.gatunki:
                        raise InvalidMovieType
                    self.filtrGatunek = gatunek
                case "3":
                    try:
                        rok_produkcji = int(input("Podaj rok produkcji:\n"))
                        self.filtrRok = rok_produkcji
                    except ValueError:
                        print("Nie podano liczby")
                    except Exception as e:
                        print(e)
                case "4.":
                    status = input("Podaj status (obejrzany/nieobejrzany):\n")
                    try:
                        if not (status.lower().strip() == "obejrzany" or status.lower().strip() == "nieobejrzany"):
                            raise WrongStatus
                        self.filtrStatus = status
                    except WrongStatus:
                        print("Podano zly status:")
                case "5":
                    self.filtrTytul = None
                    self.filtrGatunek = None
                    self.filtrRok = None
                    self.filtrStatus = None
                case _:
                    raise InvalidUserChoice
        except InvalidUserChoice:
            print("Podano zla liczbe")
        except Exception as e:
            print(e)

    def dodajKomentarz(self, film) -> None:
        komentarz = input("Podaj komentarz:\n").strip()
        try:
            for film_z_kolekcji in self.filmy:
                if (film_z_kolekcji.tytul.lower().strip() == film.tytul.lower().strip()):
                    film.komentarze.append(komentarz)
                    print("Komentarz dodany poprawnie.")
                    return
            raise MovieDoesNotExist
        except MovieDoesNotExist:
            print("Nie znaleziono filmu o podanych danych.")
        except Exception as e:
            print(e)

    def sortuj(self):
        print("Podaj po jakim atrybucie chcesz sortowac")
        print(f"Obecny filtr: {self.sortujAtrybut}, Kolejnosc: {'malejaca' if self.sortujKolejnosc else 'rosnaca'}")
        print("1. Tytul")
        print("2. Rok produkcji")
        print("3. Gatunek")
        print("4. Ocena")
        print("5. Resetuj")
        wybor = input("Podaj liczbe od 1-5:\n")
        try:
            match wybor:
                case "1":
                    self.sortujAtrybut = "TYTUL"
                case "2":
                    self.sortujAtrybut = "ROK"
                case "3":
                    self.sortujAtrybut = "GATUNEK"
                case "4":
                    self.sortujAtrybut = "OCENA"
                case "5":
                    self.sortujAtrybut = None
                    self.sortujKolejnosc = False
                case _:
                    raise InvalidUserChoice
            print("Wybierz kolejnosc sortowania:")
            print("1. Malejaca")
            print("2. Rosnaca")
            wybor = input()
            match wybor:
                case "1":
                    self.sortujKolejnosc = True
                case "2":
                    self.sortujKolejnosc = False
                case _:
                    raise InvalidUserChoice
        except InvalidUserChoice:
            print("Podaj liczbe w odpowiednim zakresie")
        except Exception as e:
            print(e)

##nie wiem gdzie to dodac, myslsalam zeby moze do tego pierwszego case'a ale nie wiem
    def hisotriaObjerzanych(self):
        print("\n### Historia obejrzanych filmów ###\n")

        try:
            obejrzane = [film for film in self.filmy if film.status.strip().lower() == "watched"]
            if not obejrzane:
                raise NoWatchedMovies

            for film in obejrzane:
                print(str(film))
                print("-" * 40)

        except NoWatchedMovies:
            print("Brak obejrzanych filmów w danej kolekcji")

    def generujStatystyki(self):
        print("\n### Statystyki ###\n")

        try:
            if not self.filmy:
                raise NoData
        except NoData:
            print("Brak danych do wygenerowania statystyk")

        gatunki_counter = defaultdict(int)
        for film in self.filmy:
            gatunki_counter[film.gatunek] += 1

        plt.figure(figsize=(12, 8))
        plt.bar(gatunki_counter.keys(), gatunki_counter.values())
        plt.title("Liczba filmów o poszczególnych gatunkach")
        plt.xlabel("Gatunek")
        plt.ylabel("Liczba filmów")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        gatunki_Grades = defaultdict(list)
        for film in self.filmy:
            gatunki_Grades[film.gatunek].append(film.ocena)


        meanGrades = {gatunek: statistics.mean(oceny) for gatunek, oceny in gatunki_Grades.items()}

        plt.figure(figsize=(12, 8))
        plt.bar(meanGrades.keys(), meanGrades.values())
        plt.title("Średnia ocena filmów o poszczególnych gatunkach")
        plt.xlabel("Gatunek")
        plt.ylabel("Średnia ocena")
        plt.ylim(0, 10)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        best_movies = sorted(self.filmy, key=lambda x: x.ocena, reverse=True)[:5]

        plt.figure(figsize=(12, 8))
        plt.bar([film.tytul for film in best_movies], [film.ocena for film in best_movies])
        plt.title("Top 5 filmów")
        plt.ylabel("Ocena")
        plt.ylim(0, 10)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()