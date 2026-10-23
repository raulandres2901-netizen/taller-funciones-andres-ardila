"""
Ejercicio 5:
Cree las funciones necesarias para descuento seguido de impuesto ficticio. El descuento se calcula
sobre la base. El impuesto se calcula sobre el subtotal ya descontado, no sobre la base original. Son
reglas ficticias, no normas tributarias. El escenario pasa el retorno del descuento a la función de
impuesto y muestra subtotal y total. Contratos en orden de parámetros: Subtotal descontado: recibe
base real no negativa en pesos, descuento real de 0 a 100 por ciento y devuelve real no negativo en
pesos. Total con impuesto: recibe subtotal real no negativo en pesos, impuesto real no negativo por
ciento y devuelve real no negativo en pesos.
Fórmula o relación: Subtotal = base × (1 − descuento / 100); total = subtotal × (1 + impuesto / 100).
Cada porcentaje se divide por 100.

"""

def subtotal(base,descuento):
    if base >= 0 and 0 < descuento <= 100:
        subt=base*(1-descuento/100)
        return subt 
    return None

def total(subt,impuesto):
    if subt > 0 and impuesto > 0:  
        tot=subt*(1+impuesto/100)
        return tot
    return None

base=float(input("Base: "))  
descuento=float(input("Descuento: "))  
impuesto=float(input("Impuesto: "))

subt = subtotal(base, descuento)
tot = total(subt, impuesto)

if subt and tot !=None:
    print("Subtotal: ",subtotal(base,descuento))
    print("Total: ",total(subt,impuesto),str("pesos"))
else:
    print("Subtotal: 0; Total: 0")    