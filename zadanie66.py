def suma_cyfr(liczba):
    suma = 0
    for i in liczba:
        suma += int(i)
    return suma

def pierwsza(liczba):
    if liczba < 2:
        return False
    if liczba == 2:
        return True
    if liczba % 2 == 0:
        return False
    for i in range(3,int(liczba**0.5)+1,2):
        if liczba % i == 0:
            return False
    return True

lista_trojek = []
with open("trojki.txt") as plik:
    for linia in plik:
        lista_trojek.append(linia.split())
print(lista_trojek)
for trojka in lista_trojek:
    if suma_cyfr(trojka[0])+suma_cyfr(trojka[1]) == int(trojka[2]):
        print(trojka)

for trojka in lista_trojek:
    if pierwsza(int(trojka[0])) and pierwsza (int(trojka[1])) and int(trojka[0])*int(trojka[1])==int(trojka[2]):
        print(trojka)