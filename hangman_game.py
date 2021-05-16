import random
import os


def extract_word():
    list_word = []
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_word.append(line)
    word = list_word[random.randint(0, 171)]
    word = word[0:len(word) - 1]
    return word


def length_word(word):
    l = len(word)
    count = 0
    hidden_word = ""
    while count < l:
        hidden_word += "-"
        count += 1
    return hidden_word


def normalize(s):
    replacements = (("á", "a"),("é", "e"),("í", "i"),("ó", "o"),("ú", "u"))

    for a, b in replacements:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s


def game(word, hidden_word): 
    count = 0
    lines = list(hidden_word)
    print(hidden_word)
    while count < 1:
        i = 0
        letter = normalize(input("Escribe una letra: "))
        assert len(letter) == 1, "Ingrese solo una letra"
        while i < len(word):
            if word[i] == letter:
                lines[i] = letter
            i += 1
        word_user = "".join(lines)
        os.system("cls")
        print(word_user)
        if word == word_user:
            count = 1
    while count < 2:
        option = int(input("Quieres jugar de nuevo? \n 1. Si \n 2. No \nElige una opcion: "))
        if option == 1:
            return run()
        elif option == 2:
            return 0
        else:
            os.system("cls")
            print("Opcion incorrecta")


def run():
    os.system("cls")
    word = normalize(extract_word())
    hidden_word = length_word(word)
    game(word, hidden_word)
    
    
if __name__ == '__main__':
    run()