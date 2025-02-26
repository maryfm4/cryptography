def lsfr(seed, wielomian, dlugosc):
    xor = 0
    output = []
    rejestr = seed
    for _ in range(dlugosc):
        for item in wielomian:
            xor += int(rejestr[item - 1])
        xor = xor % 2

        output.append(rejestr[-1])
        # print(output)

        rejestr = str(xor) + rejestr[:-1]
        # print(rejestr)
        xor = 0
    return output


seed = "110011"  # Początkowy stan rejestru
wielomian = (6, 5, 2)  # Wielomian x^6 + x^5 + x^2 + 1
# wielomian = (6, 5)  # Wielomian x^6 + x^5 + 1

i = 0
bit = 1
plain_text = []
x = int((2 ** len(seed) - 1) * 3)
# x = int(2**len(seed) - 1)
print(x)
while i < x:
    plain_text.append(bit)
    i += 1

plain_text_str = ''.join(map(str, plain_text))

output = lsfr(seed, wielomian, x)

cipher_text = []
for i in range(len(plain_text)):
    # print(int(plain_text[i]), int(output[i]))
    # print(int(plain_text[i]) != int(output[i]))
    cipher_text.append(int(int(plain_text[i]) != int(output[i])))

cipher_text_str = ''.join(map(str, cipher_text))
# cipher_text_str_zmiana = "100110010101000000111110111100111010110000101110001101101001000"

decrypted_text = []
for i in range(len(cipher_text)):
    decrypted_text.append(int(int(cipher_text[i]) != int(output[i])))


decrypted_text_str = ''.join(map(str, decrypted_text))
output_str = ''.join(map(str, output))
with open("Gen2.txt", "w") as plik:
    plik.write(str(output_str))

# print(output_str[:63])
# print(output_str[63:126])
# print(output_str[126:189])
print(f"Tekst jawny: {plain_text_str}")
print(f"Wygenerowany klucz: {output_str}")
print(f"Szyfrogram: {cipher_text_str}")
print(f"Odszyfrowany tekst: {decrypted_text_str}")
