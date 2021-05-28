################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################



def minimo(lista):
    """Funcion para determinar el minimo de la lista"""
    mini = 100
    for numero in lista:
        if numero < mini:
          mini = numero
    return mini
        
def maximo(lista):
    """Funcion para determinar el maximo de la lista"""
    maxi = 0
    for numero in lista:
        if numero > maxi:
            maxi = numero
    return maxi
    

import random
def prueba():
    print("Cuantos numeros aleatorios desea en la lista?")
    ale = int(input())
    aleatorios = [random.randint(0,100) for _ in range(ale)]
    print(aleatorios)
    masgrande = maximo(aleatorios)
    maschico = minimo(aleatorios)
    print("El maximo: ",masgrande)
    print("El minimo: ",maschico)

   
   
     

if __name__ == "__main__":
    prueba()