"""
Ejercicio 1:
Cree una función para área de un triángulo por base y altura. La altura es perpendicular a la base.
Use dos llamadas y muestre las dos áreas y su suma, calculada con los retornos. Contrato: Área de un
triángulo por base y altura: recibe base y altura, reales positivos expresados en centímetros y devuelve
el área real en centímetros cuadrados.
Fórmula o relación: Área = base × altura / 2. La división entre 2 obtiene la mitad del rectángulo de
igual base y altura.

"""
areas=0
def area(b,a):
    if b<0 or a<0:
        return None
    area (b*a)/2
    return area 

while True:
    for i in range(2):
        b=float(input("Ingrese el valor de base: "))
        a=float(input("Ingrese el valor de altura: "))
    
        if i==0:
            area1=area(b,a)
        else:    
            area2=area(b,a)
    break     

print("Areas: ",area1,",",area2)
print("suma: ",area1+area2)
