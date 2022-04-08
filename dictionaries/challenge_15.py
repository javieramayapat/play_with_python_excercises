def run():
    """Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
    Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
    """
    name: str = input("Please enter your name: ")
    age: int = int(input("Please enter your age: "))
    address: str = input("Please enter your address: ")
    cellphone: int = int(input("Please enter your cellphone: "))

    persona = {
        "name": name,
        "age": age,
        "address": address,
        "cellphone": cellphone,
    }

    print(
        persona["name"]
        + " Tiene "
        + str(persona["age"])
        + " años, vive en "
        + persona["address"]
        + " y su número de teléfono es "
        + str(persona["cellphone"])
    )


if __name__ == "__main__":
    run()
