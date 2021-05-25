################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_fahrrenheit(centigrados):
    """Esta funcion sirve para convertir a F°"""
    centigrados = int(input("Ingrese la temperatura en centigrados"))
    fah = 9.0/5.0 * centigrados + 32
    return("{centigrados} grados Centigrados son {fah} a grados Fahrrenheit")
    
def convertir_a_celsius(fahrenheit):
    """Esta funcion convierte a C°"""
    fahrenheit = int(input("Ingrese la temperatura en Fahrenheit"))
    cels = (fahrenheit - 32) * 5.0/9.0
    return("{fahrenheit} grados Fahrenheit son {cels} a grados Celsius")
    
def prueba():
    celsius = convertir_a_celsius()
    fahre = convertir_a_fahrrenheit()
    
    

if __name__ == "__main__":
    prueba()
