"""
Ejercicio 3:
Cree las funciones necesarias para tolerancia de una medición. Debe reutilizar una función de
valor absoluto que recibe un real y devuelve su distancia al cero. Los extremos de tolerancia se aceptan.
La función de aceptación utiliza el retorno de valor absoluto. El escenario consulta dos mediciones por
separado. Contratos en orden de parámetros: Valor absoluto: recibe real finito y devuelve real no
negativo. Aceptación: recibe medición y objetivo reales, tolerancia real no negativa y devuelve lógico.
Fórmula o relación: Error = valor absoluto de (medición − objetivo); aceptable cuando error ≤
tolerancia.

"""
def valorabs(x):
    if x < 0:
        return -x
    return x

def verif(medicion,objetivo,tolerancia):
    error=valorabs(medicion-objetivo)
    return error <= tolerancia

objetivo=float(input("objetivo: "))
tolerancia=float(input("tolerancia:"))

for m in range(2):
    medicion=float(input("medicion:"))
    if m==0:
        m1=medicion
    else:
        m2=medicion

r1 = verif(m1, objetivo, tolerancia)
r2 = verif(m2, objetivo, tolerancia)

print("Aceptables:", r1, ";", r2)