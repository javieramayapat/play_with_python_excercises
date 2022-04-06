def remove_accents_from_a_word(word: str) -> str:
    """Remove the acents from the word
    Args:
        word (str): Word selected

    Returns:
        str: Word with accents removed
    """
    word_without_accent = word.maketrans("áéíóú", "aeiou")
    return word.translate(word_without_accent)


def is_palindrome(string: str) -> bool:

    if type(string) != str:
        raise TypeError("The value must be a string")

    if len(string) < 1:
        raise ValueError("A empty string is not acceptable")

    string = string.lower()
    string = remove_accents_from_a_word(string)
    string = string.replace(" ", "")

    return string == string[::-1]


def run():
    """
    Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
    """
    palindrome_words = [
        "Amó la paloma",
        "ana",
        "jose",
        "Ojo",
        "perro",
        "Yo hago yoga hoy",
        "Sé verlas al revés",
        1,
        True,
        None,
    ]
    message = "The word {word_to_check} is a palindrome? - {result}"
    for word in palindrome_words:
        result = is_palindrome(word)
        print(message.format(word_to_check=word, result=result))


if __name__ == "__main__":
    run()
