import Kolekcja
from Film import Film
from MyException import *
from datetime import date


def main() -> None:
    print("Witaj w WatchList")
    print("1. Wczytaj Kolekcje")
    print("2. Utworz Kolekcje")
    inputUser = input()
    try:
        match inputUser:
            case "1":
                mainloop()
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
            print("Dostępne gatunki do wyboru: \n" + Film.gatunki)

        status = input("Wybierz status: {obejrzany/nieobejrzany} \n")
        if not (status.lower().strip() == "obejrzany" or status.lower().strip() == "nieobejrzany"):
            raise WrongStatus
        ocena = int(input("Podaj ocene: (1-10)\n"))
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

    return wynik


def mainloop():
    kolekcja = Kolekcja.Kolekcja()
    while True:
        print("1. Dodaj Film")
        print("2. Edytuj Film")
        print("3. Usun Film")
        print("4. Wyswietl Kolekcje")
        print("5. Komentuj")
        userInput = input()
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
                kolekcja.edytujFilm()
            case "3":
                kolekcja.usunFilm()
            case "4":
                kolekcja.wyswietlKolekcje()


if __name__ == '__main__':
    main()
