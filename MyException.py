class MovieAlreadyExists(Exception):
    '''Wyjątek wyrzucający błąd, jeśli podany film już istnieję'''

class MovieDoesNotExist(Exception):
    '''Wyjątek gdzie nie mamy takiego filmu w bazie'''

class InvalidMovieYear(Exception):
    '''Zwraca wyjątek, jeśli film ma wartość mniejszą niż 0'''

class InvalidUserChoice(Exception):
    '''Zwraca błąd gdy brak danego użytkownika w bazie'''

class WrongStatus(Exception):
    '''Zły status obejrzenia filmu'''

class InvalidMovieType(Exception):
    '''Brak gatunku w bazie'''
class InvalidFileFormat(Exception):
    '''Zly format pliku'''
class InvalidRatingScale(Exception):
    '''Ocena nie jest w zakresie 1-10'''

class NoWatchedMovies(Exception):
    '''Brak obejrzanych filmów'''

class NoData(Exception):
    '''Brak danych'''