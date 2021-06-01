# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def factores_primos(numero):
    """funcion para determinar los numeros primos de un numero ingresado por el usuario"""
    primos = list()
    for i in range(2,numero):
        while numero % i == 0:
            primos.append(i)
            numero = numero/i
    return primos
            
    
def prueba():
    num = int(input("Ingrese el numero para buscar sus factores primos: "))
    evaluar = factores_primos(num)
    print(evaluar)
    

if __name__ == "__main__":
    prueba()