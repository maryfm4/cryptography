import random


def tekst_na_binarne(znak):
    wartosc_znaku = ord(znak)
    binarna_rep = ""
    for i in range(7, -1, -1):
        if wartosc_znaku - 2 ** i >= 0:
            binarna_rep += '1'
            wartosc_znaku = wartosc_znaku - 2 ** i
        else:
            binarna_rep += "0"
    return binarna_rep


def gen_klucz(tekst_bin):
    key = ""
    for _ in range(len(tekst_bin)):
        key += str(random.choice([0, 1]))
    return key


def xor(klucz1, klucz2):
    xor_klucz = ""
    for i in range(len(klucz1)):
        xor_klucz += str(int(klucz1[i] != klucz2[i]))
    return xor_klucz


with open("tekstjawny.txt", "w") as plik:
    plik.write("To zdanie jest sekretem")

with open("tekstjawny.txt", "r") as plik:
    tekst = plik.read()

tekst_binarnie = ""

for znak in tekst:
    tekst_binarnie += tekst_na_binarne(znak)

print(f"Tekst jawny: {tekst}")
print(f"Tekst binarnie: {tekst_binarnie}")

klucz1 = gen_klucz(tekst_binarnie)
klucz2 = gen_klucz(tekst_binarnie)

print(f"Klucz1:{klucz1}")
print(f"Klucz2:{klucz2}")

klucz3 = xor(tekst_binarnie, xor(klucz1, klucz2))
print(f"Klucz3:{klucz3}")

with open("k1.txt", "w") as k1:
    k1.write(klucz1)
with open("k2.txt", "w") as k2:
    k2.write(klucz2)
with open("k3.txt", "w") as k3:
    k3.write(klucz3)
with open("tekstjawny_bin.txt", "w") as plik:
    plik.write(tekst_binarnie)
