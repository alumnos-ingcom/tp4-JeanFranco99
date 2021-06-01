################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    """Funcion para determinar el signo del numero ingresado"""
    if numero > 0:
        return("positivo")
    elif numero == 0:
        return("cero")
    else:
        return("negativo")
            
        
def prueba():
    num = int(input("ingrese un numero: "))
    resultado = signo(num)
    print(f"El numero {num} es {resultado}")

if __name__ == "__main__":
    prueba()