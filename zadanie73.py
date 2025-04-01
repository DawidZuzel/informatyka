with open("tekst.txt") as plik:
    tekst = plik.readline()
print(tekst)
n = 0
napisy = tekst.split()
for napis in napisy:
    for i in range(len(napis)-1):
        if napis[i] == napis[i+1]:
            n += 1
            break
print(n)

slownik = {}
for znak in tekst:
    if znak!=" " and znak != "\n":
        if znak in slownik:
            slownik[znak] += 1
        else:
            slownik[znak] = 1
slownik["z"] = 0
print(slownik)
lista = list(slownik.items())
suma = slownik.values()
suma = sum(suma)
for kr in lista:
    print(kr[0], ":", kr[1], kr[1]/suma*100, "%")

samogloski = ["A", "E", "I", "O", "U", "Y"]
maks = 0
ileNpissow = 0
for napis in napisy:
    n = 0
    for litera in napis:
        if litera not in samogloski:
            n+=1
            if n > maks:
                maks = n
            else:
                n = 0
                break
print(maks)