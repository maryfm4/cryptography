from sympy import nextprime
from random import randint

tekst = "To jest sekret"
M = ""

for item in range(len(tekst)):
    znak = str(ord(tekst[item]))
    if len(znak) < 3:
        znak = "0" + znak
    M += znak

M = int(M)
next = nextprime(M)

with open("p.txt", "w") as plik:
    plik.write(str(next))

a = randint(0, next-1)
b = randint(0, next-1)

print(f"Sekret: {M}")
print(f"Liczba pierwsza: {next}")
print(f" f(x) = {a}x^2 + {b}x + {M}")

klucze = []

for i in range(1, 6):
    klucze.append([i, a*(i**2) + b*i + M])

for k in klucze:
    plik = str(k[0]) + ".txt"
    print(f"Klucz {k[0]}: {k}")
    with open(plik, "w") as p:
        p.write(" ".join(map(str, k)))


