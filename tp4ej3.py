################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def convertir_a_fahrrenheit(centigrados):
    """Esta funcion sirve para convertir a F°"""
    fah = (9.0/5.0 * centigrados) + 32
    return(fah)
    
    
def convertir_a_celsius(fahrenheit):
    """Esta funcion convierte a C°"""
    cels = (fahrenheit - 32) * 5.0/9.0
    return(cels)
  
    
def prueba():
    aconver = input("Que es lo que desea convertir? (centigrados,fahrenheit): ")
    if aconver == "fahrenheit":
        cent = int(input("Ingrese el valor en Centigrados para convertirlo en Fahrenheit: "))
        valorfah = convertir_a_fahrrenheit(cent)
        print(f"El valor en Fahrenheit es: {valorfah}")
    else:
        aconver == "centigrados"
        fahre = int(input("Ingrese el valor en Fahrenheit para convertirlos en Centigrados: "))
        valorcent = convertir_a_celsius(fahre)
        print(f"El valor en Centigrados es: {valorcent}")
    
                    
   
    
    

if __name__ == "__main__":
    prueba()
