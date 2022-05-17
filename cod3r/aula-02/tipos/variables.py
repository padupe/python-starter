#!python3

a = 3
b = 4.4

print(a + b)

text = "Sua idade é..."
age = 23

"""
Para printar, text e age, podemos utilizar:
print(text + str(age))

Mas existe uma maneira mais adequada:
"""
print(f"{text} {age}")

print(3 * "bom dia")

# Constantes

"""
Python não possui constantes, existe uma convenção que diz:
Utiliza-se letras maiúsculas para declarar uma constante
"""

PI = 3.14
raio = float(input("Informe o raio da circunferência: "))
area = PI * raio * raio
# poderíamos calcular realizando -> area = PI * pow(raio, 2)

print(f"A área é de {area}.")