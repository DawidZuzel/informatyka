def czy_anagramy(pierwszy, drugi):
    return len(pierwszy) == len(drugi) and sorted(pierwszy) == sorted(drugi)

def czy_jednolity(napis):
    return all(litera == napis[0] for litera in napis)

def policz_jednolite_anagramy(linie):
    licznik = 0
    for linia in linie:
        a, b = linia.split()
        if len(a) == len(b) and czy_jednolity(a) and czy_jednolity(b) and czy_anagramy(a, b):
            licznik += 1
    return licznik

def policz_pary_anagramow(linie):
    licznik = 0
    for linia in linie:
        a, b = linia.split()
        if czy_anagramy(a, b):
            licznik += 1
    return licznik

def najwieksza_grupa_anagramow(linie):
    grupy = {}
    for linia in linie:
        a, b = linia.split()
        for s in (a, b):
            klucz = ''.join(sorted(s))
            grupy[klucz] = grupy.get(klucz, 0) + 1
    max_wielkosc = 0
    for wielkosc in grupy.values():
        if wielkosc > max_wielkosc:
            max_wielkosc = wielkosc
    return max_wielkosc

with open('dane_napisy.txt', 'r') as plik:
    linie = plik.readlines()
    wynik1 = policz_jednolite_anagramy(linie)
    wynik2 = policz_pary_anagramow(linie)
    wynik3 = najwieksza_grupa_anagramow(linie)

    with open('wyniki_anagramy.txt', 'w') as wynik:
        wynik.write(str(wynik1) + "\n")
        wynik.write(str(wynik2) + "\n")
        wynik.write(str(wynik3) + "\n")