################
# Jean Favreau - @JeanFranco99
# Plantilla de ejercicio
# UNRN Andina - Introducción a la Ingenieria en Computación
################

def ordenar_mayor_a_menor(uno,dos,tres):
    """Funcion para ordenar los numeros de mayor a menor"""
    if uno<dos and uno<tres:
        menor =  uno
        if dos<tres:
            medio = dos
            mayor = tres
        else:
            medio = tres
            mayor = dos
    elif dos<uno and dos<tres:
        menor = dos
        if uno<tres:
            medio = uno
            mayor = tres
        else:
            medio = tres
            mayor = uno
    else:
        menor = tres
        if uno<dos:
            medio = uno
            mayor = dos
        else:
            medio = dos
            mayor = uno
    listama = (mayor, medio, menor)
    listatu = tuple(listama)
    return listatu
    

def ordenar_menor_a_mayor(uno,dos,tres):
    """Funcion para ordenar los numeros de menor a mayor"""
    if uno<dos and uno<tres:
        menor =  uno
        if dos<tres:
            medio = dos
            mayor = tres
        else:
            medio = tres
            mayor = dos
    elif dos<uno and dos<tres:
        menor = dos
        if uno<tres:
            medio = uno
            mayor = tres
        else:
            medio = tres
            mayor = uno
    else:
        menor = tres
        if uno<dos:
            medio = uno
            mayor = dos
        else:
            medio = dos
            mayor = uno
    listame = (menor, medio, mayor)
    listametu = tuple(listame)
    return listametu



def prueba():
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    num3 = int(input("Ingrese el tercer numero: "))
    mayor_menor = ordenar_mayor_a_menor(num1,num2,num3)
    menor_mayor = ordenar_menor_a_mayor(num1,num2,num3)
    print("Numeros ordenados de mayor a menor: ", mayor_menor)
    print("Numeros ordenados de menor a mayor: ", menor_mayor)

if __name__ == "__main__":
    prueba()