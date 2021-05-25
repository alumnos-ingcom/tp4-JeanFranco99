################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero, otro_numero):
    numero = int(input())
    otro_numero = int(input())
        while otro_numero > 0:
            numero = numero + 1
            otro_numero = otro_numero - 1
            print(numero)
            
def prueba():
    num = suma_lenta("Ingrese los numeros")
    print(num)
    

if __main__ == "__main__":
    prueba():