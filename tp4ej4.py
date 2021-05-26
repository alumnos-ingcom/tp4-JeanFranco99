################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def compara(numero, otro_numero):
    
    if numero > otro_numero:
        return("1")
    else:
        if numero == otro_numero:
            return("0")
        else:
            return("-1")

def prueba():
    num1 = float(input("Ingrese el primer numero"))
    num2 = float(input("Ingrese el segundo numero"))
    resultado = compara(num1, num2)
    print(f"{resultado}")
    
if __name__ == "__main__":
    prueba()
        
        