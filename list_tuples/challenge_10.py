def run():
    """
    Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
    y muestre por pantalla el menor y el mayor de los precios.
    """
    numbers = [50, 75, 46, 22, 80, 65, 8]
    max_number = max(numbers)
    min_number = min(numbers)

    message = f"The min number is {min_number} and the max number is {max_number} "
    print(message)


if __name__ == "__main__":
    run()
