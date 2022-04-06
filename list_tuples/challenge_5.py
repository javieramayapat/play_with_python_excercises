def run():
    """
    Escribir un programa que almacene en una lista los números del 1 al 10
    y los muestre por pantalla en orden inverso separados por comas.
    """

    numbers = [number for number in range(1, 11)]
    [print(f"{number}", end=", ") for number in numbers[::-1]]


if __name__ == "__main__":
    run()
