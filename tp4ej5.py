################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def signo(numero):
       if numero > 0:
            return(f"{numero} es positivo")
        else:
            if numero == 0:
                return(f"{numero} es cero")
            else:
                return(f"{numero} es negativo")
          

def prueba():
    num = int(input("ingrese un numero")
    resultado = signo(num)
     print(f"El {num} es {resultado}")

if __name__ == "__main__":
    prueba()