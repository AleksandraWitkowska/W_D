import math
#zad1
ulub_sporty = ["siatkówka", "yoga", "bieganie", "tenis ziemny"]
ulub_sporty.reverse()
print (ulub_sporty)
ulub_sporty.append("piłka nożna")
ulub_sporty.append("koszykówka")
print (ulub_sporty)

#zad2
skróty = {"np.":"na przykład",
          "dr":"doktor",
          "asap":"as soon as possible"
          }
print (skróty)

#zad3
fav_games = {
    "5/5": "League of Legends",
    "4/5":"World of Warcraft",
    "3/5":"Guild Wars 2",
    "2/5":"The Witcher"
}
print(len(fav_games))

#zad4
zdanie = input('Wpisz zdanie, w którym policzę ile razy występuje litera "a": ')
ile_a = zdanie.count('a')
print (ile_a)

# zad5
import sys as system
system.stdout.write("podaj pierwszą liczbę: ")
a = system.stdin.readline()
system.stdout.write("podaj drugą liczbę: ")
b = system.stdin.readline()
system.stdout.write("podaj trzecią liczbę: ")
c = system.stdin.readline()
a=int(a)
b=int(b)
c=int(c)

wynik_dzial=pow(a, b)+c
wynik_dzial=str(wynik_dzial)
system.stdout.write("Wynik działania a^b+c to: ")
system.stdout.write(wynik_dzial)

#zad6
a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")
c = input("Podaj trzecią liczbę: ")
a=int(a)
b=int(b)
c=int(c)

if (a>b) & (a>c):
    print(str(a) + " jest największą z liczb, które podała/eś")
elif (b>a) & (b>c):
    print(str(b) + " jest największą z liczb, które podała/eś")
elif (c>a) & (c>b):
    print(str(c) + " jest największą z liczb, które podała/eś")

#zad7
lista = [3,4,6,5.9,6.55,888.6]
for x in lista:
    x = pow(x,2)
    print (x)

# zad8
lista_parzystych= []
i = 0
while i <10:
    liczba_od_uzytkownika= int(input ("Podaj liczbę: "))
    if liczba_od_uzytkownika % 2 == 0:
        lista_parzystych.append(liczba_od_uzytkownika)
    i+=1
print ("Parzyste liczby, które zostały podane to: ", lista_parzystych)

# zad9
x = int(input("Podaj liczbę: "))
try:
    if (x<1):
        raise ValueError
    pierwiastek = math.sqrt(x)
    print("Pierwiastek z Twojej liczby to: ", pierwiastek)
except ValueError:
    print("Podaj liczbę większą od zera!")
