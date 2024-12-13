def schemat_hornera(wspolczynniki, x):
    wynik = wspolczynniki[0]
    for wspolczynnik in wspolczynniki[1:]:
        wynik = wynik * x + wspolczynnik
    return wynik


wspolczynniki = [2, -6, 2, -1]  
x = 3
print(schemat_hornera(wspolczynniki, x)) 

def zamiana_na_dziesietny(liczba, podstawa):
    cyfry = list(map(int, str(liczba)))
    return schemat_hornera(cyfry, podstawa)

def dziesietny_na_inny(liczba, podstawa):
    if liczba == 0:
        return "0"
    cyfry = []
    while liczba:
        cyfry.append(int(liczba % podstawa))
        liczba //= podstawa
    return ''.join(str(x) for x in cyfry[::-1])


liczba_w_podstawie_5 = 432
podstawa = 5
print(zamiana_na_dziesietny(liczba_w_podstawie_5, podstawa)) 

liczba_dziesietna = 117
docelowa_podstawa = 5
print(dziesietny_na_inny(liczba_dziesietna, docelowa_podstawa))

