################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def division_lenta(dividendo, divisor):
    """Funcion para la resta sucesiva """
    resto = 0
    dividendo = dividendo - divisor
    while dividendo >= 0:
        resto = resto + 1
        dividendo = dividendo - divisor
    return resto
    


def prueba():
    divid = int(input("Ingrese el dividendo: "))
    divis = int(input("Ingrese el divisor: "))
    resultado = division_lenta(divid,divis)
    print("El resto es: " ,resultado)


if __name__ == "__main__":
    prueba()