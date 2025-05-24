import Kolekcja
from Film import Film
from MyException import *
from datetime import date

def wyczyscEkran(n = 100) -> None:
    print("\n"*n)
def main() -> None:
    print("Witaj w WatchList")
    print("1. Wczytaj Kolekcje")
    print("2. Utworz Kolekcje")
    inputUser = input()
    try:
        match inputUser:
            case "1":
                mainloop(input("Podaj sciezke do pliku .csv\n"))
            case "2":
                mainloop()
            case _:
                raise InvalidUserChoice

    except InvalidUserChoice:
        print("Wybierz 1 albo 2")


def dodajFilm() -> list[str]:
    wynik = list()
    try:
        tytul = input("Podaj tytul filmu: \n")
        rezyser = input("Podaj rezysera: \n")

        rok_produkcji = int(input("Podaj rok produkcji \n"))
        today = int(date.today().strftime("%Y"))
        if rok_produkcji < 1895 or rok_produkcji > today:
            raise InvalidMovieYear

        gatunek = input("Podaj gatunek: \n")
        if gatunek not in Film.gatunki :
            raise InvalidMovieType

        status = input("Wybierz status: {obejrzany/nieobejrzany} \n")
        if not (status.lower().strip() == "obejrzany" or status.lower().strip() == "nieobejrzany"):
            raise WrongStatus
        ocena = int(input("Podaj ocene: (1-10)\n"))
        if ocena < 1 or ocena > 10:
            raise InvalidRatingScale
        opis = input("Podaj opis:\n")

        wynik.append(tytul)
        wynik.append(rezyser)
        wynik.append(rok_produkcji)
        wynik.append(gatunek)
        wynik.append(status)
        wynik.append(ocena)
        wynik.append(opis)

        return wynik

    except InvalidMovieYear:
        print("Podano zly rok dla filmu")
    except WrongStatus:
        print("Podano zly status wybierz: {obejrzany/nieobejrzany}")
    except InvalidMovieType:
        print("Nie ma takiego gatunku do wyboru, wybierz gatunek poniżej.")
        print("Dostępne gatunki do wyboru: \n", Film.gatunki)
    except InvalidRatingScale:
        print("Ocena nie jest w zakresie od 1 do 10")

    return wynik


def mainloop(sciezka = None):
    kolekcja: Kolekcja = Kolekcja.Kolekcja(sciezka=sciezka)
    while True:
        print("1. Dodaj Film")
        print("2. Edytuj Film")
        print("3. Usun Film")
        print("4. Wyswietl Kolekcje")
        print("5. Komentuj")
        print("6. Sortuj")
        print("7. Filtruj")
        print("8. Statystyki")
        print("9. Exportuj do pliku")
        userInput = input()
        wyczyscEkran()
        try:
            match userInput:
                case "1":
                    wynik = dodajFilm()
                    if len(wynik) == 7:
                        kolekcja.dodajFilm(tytul=wynik[0],
                                   rezyser=wynik[1],
                                   rok_produkcji=wynik[2],
                                   gatunek=wynik[3],
                                   status=wynik[4],
                                   ocena=wynik[5],
                                   opis=wynik[6])
                case "2":
                    kolekcja.wyswietlKolekcje()
                    indeks = int(input("Podaj numer:"))
                    kolekcja.edytujFilm(kolekcja.filmy[indeks-1])
                case "3":
                    kolekcja.wyswietlKolekcje()
                    indeks = int(input("Podaj numer:"))
                    kolekcja.usunFilm(kolekcja.filmy[indeks-1])
                case "4":
                    kolekcja.wyswietlKolekcje()
                case "5":
                    kolekcja.dodajKomentarz()
                case "6":
                    pass
                case "7":
                    kolekcja.filtruj()
                case "8":
                    pass
                case "9":
                    kolekcja.exportujDoPliku()
        except IndexError:
            print("Podaj cyfre w zakresie filmów")
        except NameError:
            print("Podaj cyfre")

if __name__ == '__main__':
    main()
