lista =[]
with open("liczby.txt","r") as plik:
    for linia in plik.readlines():
        lista.append(int(linia))
print(lista)
# 60.1
licznik=0
l1=0
l2=0
for i in lista:
    if i<1000:
        licznik+=1
        l1=l2
        l2=i
print(licznik,l1,l2)

# 60.2
for number in lista:
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    if len(divisors) == 18:
        print(f"Liczba {number} ma 18 dzielników: {divisors}")

# 60.3
def nwd(a, b):
    while b:
        a, b = b, a % b
    return a

def czy_wzglednie_pierwsza(liczba, liczby):
    for l in liczby:
        if nwd(liczba, l) != 1:
            return False
    return True

max_wzglednie_pierwsza = None
for liczba in lista:
    if czy_wzglednie_pierwsza(liczba, [l for l in lista if l != liczba]):
        if max_wzglednie_pierwsza is None or liczba > max_wzglednie_pierwsza:
            max_wzglednie_pierwsza = liczba

if max_wzglednie_pierwsza is not None:
    print(f"Największa liczba względnie pierwsza ze wszystkimi pozostałymi to: {max_wzglednie_pierwsza}")
else:
    print("Nie znaleziono takiej liczby.")
        