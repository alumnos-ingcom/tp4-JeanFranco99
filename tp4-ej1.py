################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

class IngresoIncorrecto(Exception):
    """Esta es la Excepcion para el ingreso incorrecto"""
    pass

def ingreso_entero(mensaje):
    """
    Esta funcion muestra un mensaje y agrega la # para indicar el ingreso
    de un número entero.
    """
    ingreso = input(mensaje + " #")
    try:
        entero = int(ingreso)
    except ValueError as err:
        raise IngresoIncorrecto("No era un número!") from err
    return entero

def ingreso_entero_reintento(mensaje, cantidad_reintentos=5):
    intentos = cantidad_reintentos
    while cantidad_reintentos > 0:
        try:
            return ingreso_incorrecto(mensaje)
        except IngresoIncorrecto as err:
            cantidad_reintentos = cantidad_reintentos - 1
    raise IngresoIncorrecto("Luego de {intentos}")
   
def ingreso_entero_restringido(mensaje,valor_minimo=0, valor_maximo=10):
    pass
        
    


def prueba():
    numero = ingreso_entero("Ingrese un numero ")
    print(f"El numero es {numero}")

 
if __name__ == "__main__":
    prueba()



