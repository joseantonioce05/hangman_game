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
    w = list_word[random.randint(1, 171)]
    return w


def length_word(word):
    l = len(word)
    contador = 1
    len_word = ""
    while contador < l:
        len_word += "-"
        contador += 1
    return len_word


def run():
    word = extract_word()
    len_word = length_word(word)

    print(word)
    print(len_word)


if __name__ == '__main__':
    run()


