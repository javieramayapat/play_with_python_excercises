def run():
    """
    Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
    en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas.

    Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
    """

    subjects = ["Mathematics", "Physics", "Chemistry", "History", "Language"]

    califications = []
    for subject in subjects:
        calification = int(input(f"type your calification for {subject}: "))
        califications.append(calification)

    subject_to_repeat = []
    for idx, value in enumerate(califications):
        if value < 6:
            subject_to_repeat.append(subjects[idx])

    # You must repeat ['History', 'Language']
    print(f"You must repeat {subject_to_repeat}")


if __name__ == "__main__":
    run()
