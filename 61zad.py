ciagi=[]
with open("ciagi.txt","r") as plik:
    for linia in plik.readlines():
        liczby=[]
        for liczba in linia.split():
            liczby.append(int(liczba))
        if len(liczby)>1:
            ciagi.append(liczby)
print(ciagi)
max = 0
liczbyarytmetyczne = 0
for c in ciagi:
    roznica = c[1]-c[0]
    for i in range(2,len(c)):
        if c[i]-c[i-1] != roznica:
            break
    else:
        liczbyarytmetyczne+=1
        if roznica > max:
            max=roznica
print(liczbyarytmetyczne,max)

n=1
szesciany = []
while n**3 <1000000:
    szesciany.append(n**3)
    n+=1
print(szesciany)