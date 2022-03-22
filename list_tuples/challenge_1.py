
def run():
    """Challenge 1
    Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
    en una lista y la muestre por pantalla.
    """
    
    subjects = ['Mathematics', 'Physics', 'Chemistry', 'History', 'Language']
    for idx, value in enumerate(subjects):
        print(f'{idx} : {value}')


if __name__ == '__main__':
    run()
