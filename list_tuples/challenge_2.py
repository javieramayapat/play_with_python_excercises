def run():
    """
    Escribir un programa que almacene las asignaturas de un curso 
    (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
    en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, 
    donde <asignatura> es cada una de las asignaturas de la lista.
    """

    subjects = ['Mathematics', 'Physics', 'Chemistry', 'History', 'Language']
    for subject in subjects:
        print(f'Yo estudio {subject}')


if __name__ == '__main__':
    run()
