"""
Programa: Cálculo del IMC
Autor: Andretti Soto
Fecha: 04 de Octubre de 20268
Descripción: Calcula el Índice de Masa Corporal dado el peso y la altura.
"""

peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)

print("Tu Índice de Masa Corporal es:", round(imc, 2))