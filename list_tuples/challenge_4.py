def run():
    """
    Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
    los almacene en una lista y los muestre por pantalla ordenados de menor a mayor
    """
    
    primitiva_Lottery = [int(input('Ingresa un número: ')) for i in range(1,7)]
    primitiva_Lottery.sort()
    print(f'Los números ganadores son: {primitiva_Lottery}')

if __name__ == '__main__':
    run()
