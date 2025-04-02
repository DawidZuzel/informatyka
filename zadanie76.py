def szyfruj_tekst(tekst, klucz):
    n = len(klucz)
    tekst = list(tekst)
    for i in range(len(tekst)):
        poz_zamiany = klucz[i % n] - 1
        tekst[i], tekst[poz_zamiany] = tekst[poz_zamiany], tekst[i]
    return "".join(tekst)

def odszyfruj_tekst(tekst, klucz):
    n = len(klucz)
    tekst = list(tekst)
    oryginalny = tekst[:]
    for i in range(len(tekst)):
        poz_zamiany = klucz[i % n] - 1
        oryginalny[poz_zamiany], oryginalny[i] = oryginalny[i], oryginalny[poz_zamiany]
    return "".join(oryginalny)

def wczytaj_plik(nazwa_pliku):
    with open(nazwa_pliku, "r") as plik:
        linie = plik.readlines()
    return [linia.strip() for linia in linie]

def zapisz_plik(nazwa_pliku, dane):
    with open(nazwa_pliku, "w") as plik:
        for linia in dane:
            plik.write(linia + "\n")

dane = wczytaj_plik("szyfr1.txt")
napisy = dane[:6]
klucz = list(map(int, dane[6].split()))
wyniki = [szyfruj_tekst(napis, klucz) for napis in napisy]
zapisz_plik("wyniki_szyfr1.txt", wyniki)

dane = wczytaj_plik("szyfr2.txt")
napis = dane[0]
klucz = list(map(int, dane[1].split()))
wynik = szyfruj_tekst(napis, klucz)
zapisz_plik("wyniki_szyfr2.txt", [wynik])

dane = wczytaj_plik("szyfr3.txt")
zapisany_tekst = dane[0]
klucz = [6, 2, 4, 1, 5, 3]
odkodowany_tekst = odszyfruj_tekst(zapisany_tekst, klucz)
zapisz_plik("wyniki_szyfr3.txt", [odkodowany_tekst])