################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
    numero = int(input("ingrese un numero"))
    if numero > 0:
        print(f"{numero} es positivo")
    else:
        if numero == 0:
             print(f"{numero} es cero")
         else:
              print(f"{numero} es negativo")

def prueba():
    num = signo("Ingrese un numero")
    print(f"El signo del num es {num}")

if __name__ == "__main__":
    prueba()