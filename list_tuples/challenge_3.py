def run():
    """
    Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
    en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
    En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas 
    de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
    """
    
    subjects = ['Mathematics', 'Physics', 'Chemistry', 'History', 'Language']
    reticula = {}
    for subject in subjects:
        calification = int(input(f'Pleaser enter you califications for {subject}: '))
        reticula = reticula | {subject: calification}
    
    for key, value in reticula.items():
        print(f'In {key} I got a {value}')


if __name__ == '__main__':
    run()
