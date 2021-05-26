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
    cent = int(input("ingrese el valor en centigrados para convertirlo en Fahrenheit"))
        valorfah = convertir_a_fahrrenheit(cent)
        return(valorfah)
    fahre = int(input("Ingrese el valor en fahrenheit para convertirlos en Centigrados"))
        valorcent = convertir_a_celsius(fahre)
        return(valorcent)
    
                    
   
    
    

if __name__ == "__main__":
    prueba()
