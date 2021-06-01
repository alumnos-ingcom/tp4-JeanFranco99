################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################


def es_primo(numero):
    for i in range(2, numero):
        if numero % i == 0:
            return False
        return True

def prueba():
    num = int(input("Ingrese el numero: "))
    resultado = es_primo(num)
    if resultado is True:
        print(resultado)
    else:
        print(resultado)

if __name__ == "__main__":
    prueba()