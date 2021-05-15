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
    w = list_word[random.randint(1, 172)]
    return w


def run():
    word = extract_word()
    print(word)


if __name__ == '__main__':
    run()