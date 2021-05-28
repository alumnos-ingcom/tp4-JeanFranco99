################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_palindromo(texto):
    """Funcion para determinar si lo ingresado por el usuario es palindromo o no"""
    return texto == texto[::-1]

def prueba():
    frase = input("Ingrese la palabra o numero a evaluar: ")
    evaluar = es_palindromo(frase)
    print(evaluar)
    
        

if __name__ == "__main__":
    prueba()