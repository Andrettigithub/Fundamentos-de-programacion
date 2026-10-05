"""
Programa: Cálculo del salario neto de un empleado 
Autor: Andretti Soto
Fecha: 04 de Octubre de 20268
Descripción: Calcula el salario neto mensual de un empleado después de aplicar impuestos y deducciones.
"""

sal_bruto = float(input("Ingresa tu salario bruto mensual: "))
impuestos = float(input("Ingresa el porcentaje de tus impuestos: "))
deducciones = float(input("Ingresa las deducciones adicionales: "))

impuestos = sal_bruto * (impuestos / 100)

salario_neto = sal_bruto - impuestos - deducciones

print("El salario neto mensual es:", round(salario_neto, 2))