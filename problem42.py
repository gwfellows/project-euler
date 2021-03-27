tris = [1]
for i in range(2, 25 * 3 + 1):
    tris.append(tris[-1] + i)
tris = set(tris)


def is_tri(num):
    return num in tris


def word_value(word):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum(alphabet.index(letter) + 1 for letter in word)


def is_triangle_word(word):
    return is_tri(word_value(word))


with open("resources/p042_words.txt") as file:
    words = file.read().replace('"', "").split(",")
    num = 0
    for word in words:
        if is_triangle_word(word):
            num += 1
    print(num)
