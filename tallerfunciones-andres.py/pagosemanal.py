"""
Ejercicio 4:
Cree una función para pago semanal con horas extra. Es un modelo ficticio: las primeras 40 horas
se pagan a la tarifa ordinaria; solo las horas que exceden 40 se pagan a 1,5 veces esa tarifa. Llame para
dos personas y sume los retornos, sin redondearlos antes de sumar. Contrato: Pago semanal con horas
extra: recibe horas semanales reales no negativas y tarifa real no negativa en pesos por hora y devuelve
el pago real semanal en pesos.
Fórmula o relación: Pago = horas × tarifa si horas ≤ 40; si horas > 40, pago = 40 × tarifa + (horas −
40) × tarifa × 1,5.

"""

def pagos(horas,tarifa):
    if horas > 40:
        pago=40*tarifa+(horas-40)*tarifa*1.5
    elif horas <= 40:
        pago=horas*tarifa
    return pago

for i in range(2):
    horas=float(input("horas: "))
    tarifa=float(input("tarifa: "))
    if i==0:
        hora1=horas
        tarifa1=tarifa
    else:
        hora2=horas
        tarifa2=tarifa

p1=pagos(hora1,tarifa1)
p2=pagos(hora2,tarifa2)    

print("Pagos: ",p1,p2,"Total: ",p1+p2)