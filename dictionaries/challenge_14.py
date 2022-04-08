def run():
    """
    Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'},
    pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
    """

    COINS = {"Euro": "€", "Dollar": "$", "Yen": "¥"}
    currency_selected = input(
        "Please enter a currency's name that you want to see the simbol: "
    )
    # Receives as parameter a key, returns the value of the key. If not found, returns a none object.
    print(COINS.get(currency_selected, "The currency does't exist"))


if __name__ == "__main__":
    run()
