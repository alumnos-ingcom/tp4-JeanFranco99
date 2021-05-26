################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

from random import randint

def lista_random(cantidad, minimo, maximo):
    milista = list()
    for i in range(cantidad):
        milista.append(randint(minimo,maximo))
    return milista

def minimo(lista):
    n = 0
    lista = milista
    mini = 0
    for i in range(len(lista)):
        if n < mini:
            mini = n 
    return(f"{min}")
        
        
def maximo(lista):
      lista = milista
      n = 0
    maxi = 0
    for i in range(len(lista)):
        if n > maxi:
        maxi= n 
    return(f"{maxi}")


def prueba():
    cant = int(input("Ingrese la cantidad de la lista"))
    mini_list = int(input("Ingrese el minimo de la lista"))
    max_list = int(input("Ingrese el maximo de la lista"))
     lis = lista_random(cant, mini_list, max_list)
     print(f"{lista_random}")
     

if __name__ == "__main__":
    prueba()