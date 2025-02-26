def show_file(file):
    try:
        with open(file, 'r') as x:
            content = x.read()
        return content
    except FileNotFoundError:
        print("FileNotFound:", file)
        return None


def encrypt_text(text):
    encrypted_text = []
    for letter in range(len(text)):
        x = text[letter]
        # print(x)
        if x.isupper():
            en_text = (ord(x) - 65 + 26 % 26)
            encrypted_text1 = chr(90 - en_text)
            encrypted_text.append(encrypted_text1)
        else:
            encrypted_text.append(x)
    return ''.join(encrypted_text)


def decrypt_text(text):
    decrypted_text = []
    for letter in range(len(text)):
        x = text[letter]
        # print(x)
        if x.isupper():
            de_text = (ord(x) - 65 + 26 % 26)
            decrypted_text1 = chr(90 - de_text)
            decrypted_text.append(decrypted_text1)
        else:
            decrypted_text.append(x)
    return ''.join(decrypted_text)


plain = 'plain.txt'
file = show_file(plain)
result = encrypt_text(file)
print("Encrypted text:")
print(result)
result2 = decrypt_text(result)
print("Decrypted text:")
print(result2)

