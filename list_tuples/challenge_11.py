def calculate_scalar_product(vector_a, vector_b):

    scalar = 0
    for i in range(len(vector_a)):
        scalar += vector_a[i] * vector_b[i]

    return scalar


def run():
    """
    Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.
    """
    vector_1 = [1, 2, 3]
    vector_2 = [-1, 0, 2]
    result = calculate_scalar_product(vector_1, vector_2)

    message = f"The product of the vector {vector_1} and {vector_2} is a scalar with the value: {result}"
    print(message)


if __name__ == "__main__":
    run()
