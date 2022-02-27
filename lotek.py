'''Ile muszę wydać żeby wygrać w lotka?'''

import random, sys, colorama
from datetime import datetime
from colorama import Fore, Back, Style

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
    moje_liczby = set()
    i = 1
    while i < 7:
        liczba = int(input(f'Podaj {i} z 6 liczb zawierających się w przedzial od 1 do 49: '))
        if liczba in list(range(1, 50)):
            moje_liczby.add(liczba)
            i += 1
        else:
            print('Podana liczba nie mieści się w zakresie 1 - 49, spróbuj jeszcze raz')

    return moje_liczby

def pobierz_wiek():
    """przyjmuje wiek od użytkownika

    Returns:
        int: wiek użytkownika w latach
    """
  
    wiek = int(input('Podaj wiek, a odpowiem Ci, czy dożyjesz wygranej szóstki w lotka :) '))
    if wiek < 18:
        print("Jesteś za młody/a żeby grać w lotto")
        sys.exit()
    if wiek > 60:
        print('W tym wieku szkoda tracić pieniędzy na lotka, kup wnukom po lodzie')
        sys.exit()
        
    return wiek

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

def dodaj_liczbe_do_wylosowanych(wylosowana_liczba, wylosowane_liczby):
    """dodaje wylosowaną liczbę do zbioru liczb wylosowanych

    Args:
        wylosowana_liczba (int): liczba wylosowana
        wylosowane_liczby (set): zbiór liczb wylosowanych
    Returns:
        set: zbiór liczb wylosowanych po dodaniu kolejnej liczby
    """
    wylosowane_liczby.add(wylosowana_liczba)
    return wylosowane_liczby

def wylosuj_liczby(liczby_w_maszynie, wylosowane_liczby, ilosc_losowanych_liczb=6):
    """losuje zadaną ilość liczb tak jak w TV

    Args:
        ilosc_losowanych_liczb (int, optional): liczba losowanych liczb (domyślnie 6)
    Returns:
        set: zbiór wylosowanych liczb
    """
        
    i = 0
    while i < ilosc_losowanych_liczb:
        wylosowana_liczba, liczby_w_maszynie = losuj_liczbe(liczby_w_maszynie)
        wylosowane_liczby = dodaj_liczbe_do_wylosowanych(wylosowana_liczba, wylosowane_liczby)
        i += 1

    return wylosowane_liczby

def sprawdz_liczbe_trafien(wylosowane_liczby, moje_liczby):
    """zwraca liczbę trafień po losowaniu liczb

    Args:
        wylosowane_liczby (set): zbiór liczb wylosowanych
        moje_liczby (set): zbiór wybranych liczb
    Returns:
        int: ilość trafionych liczb
    """
    liczba_trafien = wylosowane_liczby.intersection(moje_liczby)
    return len(liczba_trafien)

def oblicz_wartosc_losow(liczba_losow):
    """wylicza zainwestowane środki na zakup losów

    Args:
        liczba_losow (int): liczba kupionych losow
        CENA_LOSU (int): cena jednego losu
    Returns:
        int: calkowite koszty zakupu losów
    """
    return liczba_losow*CENA_LOSU

def oblicz_wiek(wiek, liczba_losowan):
    """oblicza wiek gracza w momencie wygrania przy założeniu,
    że kupowano trzy los na tygodniowo (156 losów w roku)

    Args:
        wiek (int): wiek gracza w latach podczas rozpoczęcia gry w lotka
        liczba_losowan (int): całkowita liczba losowań (3 losowania na tydzień) do wygranej
    Returns:
        int:wiek gracza w latach w momencie wygrania
    """
    wiek_zwyciezcy = int(wiek + liczba_losowan/156)
    return wiek_zwyciezcy

def oblicz_wygrana(trafiono_5, trafiono_4, trafiono_3):
    """oblicza całkowitą wygraną za wszystkie trafienia do momentu trafnienia szóstki

    Args:
        trafiono_5 (int): liczba trafionych piątek
        trafiono_4 (int): liczba trafionych czwórek
        trafiono_3 (int): liczba trafionych trójek
        WYGRANA_SZ (int): wartość wygranej za szóstkę
        WYGRANA_PI (int): wartość wygranej za piątkę
        WYGRANA_CZW (int): wartość wygranej za czwórkę
        WYGRANA_TR int): wartość wygranej za trójkę
    Returns:
        int: całkowita wartość wygranej
    """
    wygrana = WYGRANA_SZOSTKA + WYGRANA_PIATKA*trafiono_5 + WYGRANA_CZWORKA*trafiono_4 + WYGRANA_TROJKA*trafiono_3
    return wygrana

def podaj_czas_liczenia(start, koniec):
    """oblicza całkowity czas obliczania liczby losowań

    Args:
        start (datetime): start obliczeń
        koniec (datetime): koniec obliczeń
    Returns:
        str: czas obliczania w formacie H:MM:SS
    """
    return str(koniec - start)

def podaj_podsumowanie(liczba_prob, trafiono_5, trafiono_4, trafiono_3, czas):
    """podaje podsumowanie obliczeń:
    liczbę losowań
    liczbę trafień: piątek, czwórek, trójek
    całkowitą wygraną
    poniesione koszty
    czas obliczania
    wiek w chwili wygranej

    Args:
        liczba_prob (int): całkowita liczba losowań
        trafiono_5 (int): liczba trafionych piątek
        trafiono_4 (int): liczba trafionych czwórek
        trafiono_3 (int): liczba trafionych trójek
        czas (str): całkowity czas obliczania
    """
    print('---'*10)
    print(f'{Fore.YELLOW}BRAWO udało się trafić szóstkę po {liczba_prob:,} losowaniach')
    print('Ponadto trafiłeś jeszcze:')
    print(f'piątek:  {trafiono_5:,}')
    print(f'czwórek: {trafiono_4:,}')
    print(f'trójek:  {trafiono_3:,}')
    print('---'*10)
    wygrana = oblicz_wygrana(trafiono_5, trafiono_4, trafiono_3)
    wydano = oblicz_wartosc_losow(liczba_prob)
    print(f'{Fore.BLUE}Łącznie wygrałeś {wygrana:,}zł, a wydałeś na losy {wydano:,}zł')
    print(f'Twój komputer wykonał te obliczenia w {czas}, a Ty miałbyś {oblicz_wiek(wiek, liczba_prob):,} lat w dniu wygranej')
    print('Chyba trzeba brać się do kodowania, a nie czekać na wygraną :)')
    print()

if __name__ == "__main__":
    wiek = pobierz_wiek()
    moje_liczby = pobierz_liczby()   
    start = datetime.now()

    liczba_prob = 0
    trafiono_5 = 0
    trafiono_4 = 0
    trafiono_3 = 0

    while True:
        liczba_prob += 1
        print(f'Losowanie nr {liczba_prob:,}', end='\r')

        # losowanie liczb
        liczby_w_maszynie = list(range(1,50))
        wylosowane_liczby = set()
        wylosowane_liczby = wylosuj_liczby(liczby_w_maszynie, wylosowane_liczby)

        # sprawdzanie liczby trafień
        trafienia = sprawdz_liczbe_trafien(wylosowane_liczby, moje_liczby)
        if trafienia == 6:
            czas = podaj_czas_liczenia(start, datetime.now())
            podaj_podsumowanie(liczba_prob, trafiono_5, trafiono_4, trafiono_3, czas)
            break
        elif trafienia == 5:
            if trafiono_5 == 0:
                print(f'{Fore.GREEN}Pierwsza trafiona piątka po {liczba_prob:,} losowaniach')
            trafiono_5 += 1
        elif trafienia == 4:
            if trafiono_4 == 0:
                print(f'{Fore.GREEN}Pierwsza trafiona czwórka po {liczba_prob:,} losowaniach')
            trafiono_4 += 1
        elif trafienia == 3:
            if trafiono_3 == 0:
                print(f'{Fore.GREEN}Pierwsza trafiona trójka po {liczba_prob:,} losowaniach')
            trafiono_3 += 1
