"""
Ejercicio 2:
Cree una función para precio unitario comparable. Dos paquetes pueden tener tamaños distintos;
no compare solo sus precios totales. Llame para dos paquetes y use los retornos para indicar el más
económico por gramo; si coinciden indique igualdad. Contrato: Precio unitario comparable: recibe
precio total real no negativo en pesos y cantidad real positiva en gramos y devuelve el precio real de un
gramo en pesos.
Fórmula o relación: Precio por gramo = precio total / cantidad de gramos.

"""

def precioconv(p,g):
    if p<0 or g<0:
        return None
    preciogramo= p/g
    return preciogramo

def conviene(precio1,precio2):
    if precio1>precio2:
        return "paquete 2"
    elif precio2>precio1:
        return "paquete 1"
    else:
        return "no hay diferencia en los paquetes"

while True:
    for i in range(2):
        p=float(input("Ingrese el precio total: "))
        g=float(input("Ingrese los gramos: "))  

        if i==0:
            precio1=precioconv(p,g)  
        else:
            precio2=precioconv(p,g)
    break            


print("Precios por gramo: ",precio1,";",precio2, "pesos")
print("conviene: ", conviene(precio1,precio2))