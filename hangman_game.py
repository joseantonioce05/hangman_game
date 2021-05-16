# Incorpora comprehensions, manejos de errores y manejo de archivos
# Utiliza el archivo data.txt y leelo para obtener las palabras
# enumarate
# get en diccionario
# La sentencia os.system("cls") o os.system("clear") para limpiar la terminal
import random


def extract_word():
    list_word = []
    with open("./files/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            list_word.append(line)
    w = list_word[random.randint(0, 171)]
    w = w[0:len(w) - 1]
    return w


def length_word(word):
    l = len(word)
    contador = 0
    hidden_word = ""
    while contador < l:
        hidden_word += "-"
        contador += 1
    return hidden_word


def game(word, hidden_word): 
    c = 0
    rayas = list(hidden_word)
    while c < 1:
        i = 0
        letter = input("Escribe una letra: ")
        assert letter == 1, "Ingrese solo una letra"
        while i < len(word):
            if word[i] == letter:
                print(word[i])
                print(rayas)
                rayas[i] = letter
                print(rayas)
            i += 1
        word_user = "".join(rayas)
        print(word_user)
        if word == word_user:
            c = 1

def run():
    word = extract_word()
    print(len(word))
    print(word)
    hidden_word = length_word(word)
    print(hidden_word)
    game(word, hidden_word)
    
    
if __name__ == '__main__':
    run()