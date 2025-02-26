import os
os.environ["NUMBA_CACHE_DIR"] = "C:\\Users\\marys\\Temp"
import galois
from random import sample


def getfile(f):
    return [int(i) for i in f.read().split()]


with open("1.txt", "r") as f:
    k1 = getfile(f)

with open("2.txt", "r") as f:
    k2 = getfile(f)

with open("3.txt", "r") as f:
    k3 = getfile(f)

with open("4.txt", "r") as f:
    k4 = getfile(f)

with open("5.txt", "r") as f:
    k5 = getfile(f)

with open("p.txt", "r") as file:
    p = int(file.read())

klucze = [k1, k2, k3, k4, k5]

# ran_klucze = [k1, k2, k3]
ran_klucze = sample(klucze, 3)
print(f"Trzy dowolne klucze: {ran_klucze}")

GF = galois.GF(p)

x_vals = GF([x % p for x, _ in ran_klucze])
y_vals = GF([y % p for _, y in ran_klucze])

poly = galois.lagrange_poly(x_vals, y_vals)
print(f"Wielomian: {poly}")
M = str(poly.coeffs[2])
print(f"Sekret:{M}")

if len(M) % 3 != 0:
    M = "0" + M

sekret = []
for i in range(0, len(M), 3):
    cyfry = M[i:i+3]
    liczba = int(cyfry)
    znak = chr(liczba)
    sekret.append(znak)

print(f"Sekret w pełni odszyfrowany: {''.join(sekret)}")
