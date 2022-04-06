import numpy as np


def run():
    """Escribir un programa que almacene las matrices

                      -1 0
    A =  1 2 3    B =  0 1
         4 5 6         1 1

    en una lista y muestre por pantalla su producto.
    Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
    """
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[-1, 0], [0, 1], [1, 1]])

    product = A.dot(B)
    print(product)


if __name__ == "__main__":
    run()
