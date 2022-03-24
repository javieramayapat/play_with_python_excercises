import string


def alphabet():
    return list(string.ascii_lowercase)


def run():
    """
    Escribir un programa que almacene el abecedario en una lista, 
    elimine de la lista las letras que ocupen posiciones múltiplos de 3, 
    y muestre por pantalla la lista resultante.

    ['a', 'b', 'd', 'e', 'g', 'h', 'j', 'k', 'm', 'n', 'o', 'p', 'r', 's', 'u', 'v', 'x', 'y']

    """


ALPHABET = alphabet()
for i in range(len(ALPHABET), 1, -1):
    if i % 3 == 0:
        ALPHABET.pop(i-1)
print(ALPHABET)


if __name__ == '__main__':
    run()
