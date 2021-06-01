################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def suma_lenta(numero, otro_numero):
    while otro_numero > 0:
        numero = numero + 1
        otro_numero = otro_numero - 1
        return numero
            
def prueba():
    num = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingresel el segundo numero: "))
    resultado = suma_lenta(num, num2)
    print(resultado)
    
    
    

if __name__ == "__main__":
    prueba()