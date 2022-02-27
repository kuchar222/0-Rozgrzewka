'''Ile muszę wydać żeby wygrać w lotka?'''

import random
import sys
from datetime import datetime
import colorama
from colorama import Fore

colorama.init(autoreset=True)

CENA_LOSU = 3
# sumych wygranych
WYGRANA_SZOSTKA = 2500000
WYGRANA_PIATKA = 5486
WYGRANA_CZWORKA = 171
WYGRANA_TROJKA = 24

def pobierz_liczby():
    """przyjmuje od użytkownika 6 liczb

    Returns:
        set: podane przez użytkownika liczby
    """
    liczby_gracza = set()
    i = 1
    while i < 7:
        liczba = int(input(f'Podaj {i} z 6 liczb zawierających się w przedzial od 1 do 49: '))
        if liczba in list(range(1, 50)):
            liczby_gracza.add(liczba)
            i += 1
        else:
            print('Podana liczba nie mieści się w zakresie 1 - 49, spróbuj jeszcze raz')

    return liczby_gracza

def pobierz_wiek():
    """przyjmuje wiek od użytkownika

    Returns:
        int: wiek użytkownika w latach
    """
    wiek_gracza = int(input('Podaj wiek, a odpowiem Ci, czy dożyjesz wygranej szóstki w lotka :) '))
    if wiek < 18:
        print("Jesteś za młody/a żeby grać w lotto")
        sys.exit()
    if wiek > 60:
        print('W tym wieku szkoda tracić pieniędzy na lotka, kup wnukom po lodzie')
        sys.exit()
    return wiek_gracza

def losuj_liczbe(zbior_liczb):
    """losuje (wyciąga) liczbę ze zbioru liczb,
    a następnie usuwa ją ze zbioru

    Args:
        zbior_liczb (list): zbiór liczb
    Returns:
        int: wylosowana liczba
        list: zbiór liczb bez wylosowanej liczby
    """
    wylosowana_liczba = random.choice(zbior_liczb)
    zbior_liczb.remove(wylosowana_liczba)
    return wylosowana_liczba, zbior_liczb

def dodaj_liczbe_do_wylosowanych(wylosowana_liczba, liczby_wylosowane):
    """dodaje wylosowaną liczbę do zbioru liczb wylosowanych

    Args:
        wylosowana_liczba (int): liczba wylosowana
        liczby_wylosowane (set): zbiór liczb wylosowanych
    Returns:
        set: zbiór liczb wylosowanych po dodaniu kolejnej liczby
    """
    liczby_wylosowane.add(wylosowana_liczba)
    return liczby_wylosowane

def wylosuj_liczby(liczby_w_maszynie_losujacej, ilosc_losowanych_liczb=6):
    """losuje zadaną ilość liczb tak jak w TV

    Args:
        liczby_w_maszynie_losującej (set): zbiór liczb,
        z których dokonuje się losowania kolejnych liczb

        ilosc_losowanych_liczb (int, optional): liczba losowanych liczb (domyślnie 6)
    Returns:
        set: zbiór wylosowanych liczb
    """
    liczby_wylosowane = set()
    i = 0
    while i < ilosc_losowanych_liczb:
        wylosowana_liczba, liczby_w_maszynie_losujacej = losuj_liczbe(liczby_w_maszynie_losujacej)
        liczby_wylosowane = dodaj_liczbe_do_wylosowanych(wylosowana_liczba, liczby_wylosowane)
        i += 1

    return liczby_wylosowane

def sprawdz_liczbe_trafien(liczby_po_losowaniu, podane_liczby):
    """zwraca liczbę trafień po losowaniu liczb

    Args:
        liczby_po_losowaniu (set): zbiór liczb wylosowanych
        podane_liczby (set): zbiór wybranych liczb
    Returns:
        int: ilość trafionych liczb
    """
    liczba_trafien = liczby_po_losowaniu.intersection(podane_liczby)
    return len(liczba_trafien)

def oblicz_wartosc_losow():
    """wylicza zainwestowane środki na zakup losów

    Returns:
        int: calkowite koszty zakupu losów
    """
    return LICZBA_PROB*CENA_LOSU

def oblicz_wiek(wiek_gracza):
    """oblicza wiek gracza w momencie wygrania przy założeniu,
    że kupowano trzy los na tygodniowo (156 losów w roku)

    Args:
        wiek (int): wiek gracza w latach podczas rozpoczęcia gry w lotka
    Returns:
        int:wiek gracza w latach w momencie wygrania
    """
    wiek_w_chwili_zwyciestwa = int(wiek_gracza + LICZBA_PROB/156)
    return wiek_w_chwili_zwyciestwa

def oblicz_wygrana():
    """oblicza całkowitą wygraną za wszystkie trafienia do momentu trafnienia szóstki

    Returns:
        int: całkowita wartość wygranej
    """
    wygrana = WYGRANA_SZOSTKA + WYGRANA_PIATKA*TRAFIONO_5 + WYGRANA_CZWORKA*TRAFIONO_4 \
        + WYGRANA_TROJKA*TRAFIONO_3
    return wygrana

def podaj_czas_liczenia(czas_start, czas_koniec):
    """oblicza całkowity czas obliczania liczby losowań

    Args:
        czas_start (datetime): start obliczeń
        czas_koniec (datetime): koniec obliczeń
    Returns:
        str: czas obliczania w formacie H:MM:SS
    """
    return str(czas_koniec - czas_start)

def podaj_podsumowanie():
    """podaje podsumowanie obliczeń:
    liczbę losowań
    liczbę trafień: piątek, czwórek, trójek
    całkowitą wygraną
    poniesione koszty
    czas obliczania
    wiek w chwili wygranej
    """
    print('---'*10)
    print(f'{Fore.YELLOW}BRAWO udało się trafić szóstkę po {LICZBA_PROB:,} losowaniach')
    print('Ponadto trafiłeś jeszcze:')
    print(f'piątek:  {TRAFIONO_5:,}')
    print(f'czwórek: {TRAFIONO_4:,}')
    print(f'trójek:  {TRAFIONO_3:,}')
    print('---'*10)
    wygrana = oblicz_wygrana()
    wydano = oblicz_wartosc_losow()
    print(f'{Fore.BLUE}Łącznie wygrałeś {wygrana:,}zł, a wydałeś na losy {wydano:,}zł')
    print(f'Twój komputer wykonał te obliczenia w {CZAS}, a Ty miałbyś {oblicz_wiek(wiek):,}\
         lat w dniu wygranej')
    print('Chyba trzeba brać się do kodowania, a nie czekać na wygraną :)')
    print()

if __name__ == "__main__":
    wiek = pobierz_wiek()
    moje_liczby = pobierz_liczby()
    start = datetime.now()

    LICZBA_PROB = 0
    TRAFIONO_5 = 0
    TRAFIONO_4 = 0
    TRAFIONO_3 = 0

    while True:
        LICZBA_PROB += 1
        print(f'Losowanie nr {LICZBA_PROB:,}', end='\r')

        # losowanie liczb
        liczby_w_maszynie = list(range(1,50))
        wylosowane_liczby = set()
        wylosowane_liczby = wylosuj_liczby(liczby_w_maszynie, wylosowane_liczby)

        # sprawdzanie liczby trafień
        trafienia = sprawdz_liczbe_trafien(wylosowane_liczby, moje_liczby)
        if trafienia == 6:
            CZAS = podaj_czas_liczenia(start, datetime.now())
            podaj_podsumowanie()
            break
        if trafienia == 5:
            if TRAFIONO_5 == 0:
                print(f'{Fore.GREEN}Pierwsza trafiona piątka po {LICZBA_PROB:,} losowaniach')
            TRAFIONO_5 += 1
        elif trafienia == 4:
            if TRAFIONO_4 == 0:
                print(f'{Fore.GREEN}Pierwsza trafiona czwórka po {LICZBA_PROB:,} losowaniach')
            TRAFIONO_4 += 1
        elif trafienia == 3:
            if TRAFIONO_3 == 0:
                print(f'{Fore.GREEN}Pierwsza trafiona trójka po {LICZBA_PROB:,} losowaniach')
            TRAFIONO_3 += 1
