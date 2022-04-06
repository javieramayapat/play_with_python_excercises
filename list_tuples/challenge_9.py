def count_amount_of_vowels_in_text(string: str) -> dict:

    if len(string) < 1:
        raise ValueError("the leng of the wprd must be grather than cero")

    VOWELS = ["a", "e", "i", "o", "u"]

    numbers_of_repetitions_of_vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    word = list(string)
    for vowel in VOWELS:
        for letter in word:
            if vowel == letter:
                value = numbers_of_repetitions_of_vowels.get(vowel)
                numbers_of_repetitions_of_vowels[vowel] = value + 1

    return numbers_of_repetitions_of_vowels


def run():
    """Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que contiene cada vocal."""

    """algoritmo para el problema    
    
    ¿cómo lo resolveria?
    1.- Como voy a comparar con vocales debo crear un array donde almacene ['a','e','i','o','u']
    2.- Debo convertir separar la palabra en letras para pode comparar con las letras vocales
    3.- debo tomar una letra de las vocales y recorrer si existe en la palabra si esta existe hacer una sumatoria y aumentar el numero de repeticones por esa letra
    4.- Una vez que termine de recorrer la ultima letra de la palbra debo poder contabilizado el numero de repeteciones de la mismatch
    """

    word = input("Enter a word please: ")
    print(count_amount_of_vowels_in_text(word))

    # message = "with the input {input} the result is result: {result}"
    # inputs = ["ana", "maría", 58, True, 58.9, None, "", "j"]
    # for input in inputs:
    #     result = count_amount_of_vowels_in_text(input)
    #     print(message.format(input=input, result=result))


if __name__ == "__main__":
    run()
