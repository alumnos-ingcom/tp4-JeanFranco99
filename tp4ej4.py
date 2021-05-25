################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def compara(numero, otro_numero):
    numero = float(input())
    otro_numero = float(input())
    if numero > otro_numero:
        print("1")
    else:
        if numero == otro_numero:
            print("0")
        else:
            print("-1")

def prueba():
    num = compara("Ingrese los numeros")
    print(num)
    
if __name__ == "__main__":
    prueba()
        
        