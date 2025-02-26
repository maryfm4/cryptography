def show_file(file):
    try:
        with open(file, 'r') as x:
            content = x.read()
        return content
    except FileNotFoundError:
        print("FileNotFound:", file)
        return None


def define_size(text):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
               29, 30]
    for item in numbers:
        if len(text) <= item ** 2:
            if item % 2 == 0:
                return item + 1
            else:
                return item
    else:
        return "Your text is too long"


def create_matrix(text, size):
    matrix1 = []
    for i in range(size):
        row = ['X' for _ in range(size)]
        matrix1.append(row)

    index = 0
    pointY = 0
    pointX = 0
    rows = size
    columns = size
    direction = "R"

    while index < len(text):
        # for m in matrix1:
        #     print(m)
        # print('\n')

        matrix1[pointY][pointX] = text[index]

        if direction == "R":
            if pointX == columns - 1:
                direction = "D"
                pointY += 1
            else:
                pointX += 1
        elif direction == "D":
            if pointY == rows - 1:
                direction = "L"
                pointX -= 1
            else:
                pointY += 1
        elif direction == "L":
            if pointX == size - columns:
                direction = "U"
                rows -= 1
                pointY -= 1
            else:
                pointX -= 1
        elif direction == "U":
            if pointY == size - rows:
                direction = "R"
                columns -= 1
                pointX += 1
            else:
                pointY -= 1

        index += 1
    return matrix1


def encrypt_matrix(matrix):
    text = []
    for cols in range(size):
        for rows in range(size):
            text.append(matrix[rows][cols])
    return "".join(text)


def create_matrix2(text, size):
    matrix2 = []
    for i in range(size):
        row = ['X' for _ in range(size)]
        matrix2.append(row)

    index = 0
    for cols in range(size):
        for rows in range(size):
            if index < len(text):
                matrix2[rows][cols] = text[index]
            index += 1
    return matrix2


def create_matrix3(text, size):
    matrix4 = []
    for i in range(size):
        row = ['X' for _ in range(size)]
        matrix4.append(row)

    index = 0
    for rows in range(size):
        for cols in range(size):
            if index < len(text):
                matrix4[rows][cols] = text[index]
            index += 1
    return matrix4


def decrypt_matrix(matrix):
    text2 = []
    index = 0
    pointY = 0
    pointX = 0
    rows = size
    columns = size
    direction = "R"
    de_text = []

    while index < len(result):
        text2.append(matrix[pointY][pointX])
        if direction == "R":
            if pointX == columns - 1:
                direction = "D"
                pointY += 1
            else:
                pointX += 1
        elif direction == "D":
            if pointY == rows - 1:
                direction = "L"
                pointX -= 1
            else:
                pointY += 1
        elif direction == "L":
            if pointX == size - columns:
                direction = "U"
                rows -= 1
                pointY -= 1
            else:
                pointX -= 1
        elif direction == "U":
            if pointY == size - rows:
                direction = "R"
                columns -= 1
                pointX += 1
            else:
                pointY -= 1

        index += 1
    for letter in text2:
        if letter != "X":
            de_text.append(letter)
    return "".join(de_text)


plain = 'plain1.txt'
file = show_file(plain)
size = define_size(file)
matrix = create_matrix(file, size)
result = encrypt_matrix(matrix)
print("Encrypted text:")
print(result)
matrix2 = create_matrix2(result, size)
# for m in matrix2:
#     print(m)
# print('\n')
result2 = decrypt_matrix(matrix2)
print("Decrypted text:")
print(result2)
text = "fe oio bwjps   czacfgdoepan nmk iaia ip idszawzeeiyeaeaayzenrjnljjwaiittkso wnzoaiarwna tcaztwdewzmxrzr o izsao tidnaeer"
size1 = define_size(text)
result3 = create_matrix2(text, size1)
result4 = create_matrix3(text, size1)
for m in result3:
    print(m)
print('\n')
for m in result4:
    print(m)
print('\n')

# print(result4)
