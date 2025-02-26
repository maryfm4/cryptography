def xor(klucz1, klucz2):
    xor_klucz = ""
    for i in range(len(klucz1)):
        xor_klucz += str(int(klucz1[i] != klucz2[i]))
    return xor_klucz


def bin_tekst(tekst):
    string = [chr(int(tekst[i:i + 8], 2)) for i in range(0, len(tekst_jawny_bin), 8)]
    return "".join(string)


klucz1 = ""
klucz2 = ""
klucz3 = ""

with open("k1.txt", "r") as k1:
    klucz1 = k1.read()

with open("k2.txt", "r") as k2:
    klucz2 = k2.read()

with open("k3.txt", "r") as k3:
    klucz3 = k3.read()

tekst_jawny_bin = xor(klucz1, xor(klucz2, klucz3))
print(f"Tekst jawny zapisany binarnie: {tekst_jawny_bin}")

tekst_jawny = bin_tekst(tekst_jawny_bin)
print(f"Tekst jawny: {tekst_jawny}")

