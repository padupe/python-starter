print("#### NUMBERS ####")

print(6)
print(" ")

"""
    Python aceita:
    - Números Inteiros -> 1, 2, 3
    - Números Decimais -> 1.05, 2.89
    - Números Negativos -> -3, -2, -1
"""

number1 = 5
print("number1 = 5\n ")

number2 = 2
print("number2 = 2\n ")

number3 = 10
print("number3 = 10\n ")

number4 = 11.7
print("number 4 = 11.7\n ")

print("==== Adição ====")
print("number1 + number3")
print(number1 + number3)
print(" ")

print("==== Subtração ====")
print("number1 - number2")
print(number1 - number2)
print(" ")

print("==== Multiplicação ====")
print("number1 * number2")
print(number1 * number2)
print(" ")

print("==== Divisão ====")
print("number3 - number1")
print(number3 / number1)
print(" ")

# Concatenando String + Número
print("==== Concatentando String + Números ====")

"""
Não é possível apenas informar print(number1 + " é o número cinco.")
Precisamos converter um dos tipos (String ou Int) para que ambos fiquem iguais
No exemplo, optamos por transformar o Int, no caso a variável "number1" em String utilizando "str()"
"""
print(str(number1) + " é o número cinco.")
print(" ")

print("==== Funções ====")
print(" ")

# Função para saber o menor valor entre um grupo de números
print("*** Função MIN -> min(number1, number2, number3)***")
print("Mostre o menor valor entre os números 2, 5 e 10")
print(min(number1, number2, number3))
print(" ")

# Função para saber o maior valor entre um grupo de números
print("*** Função MAX -> min(number1, number2, number3)***")
print("Mostre o maior valor entre os números 2, 5 e 10")
print(max(number1, number2, number3))
print(" ")

# Função para pontências
print("*** Função POW -> pow(number1, number2)***")
print("Mostre o valor obitdo de 5 elevado a potência de 2 (ou 5 ao quadrado)")
print(pow(number1, number2))
print(" ")

# Função para arredondar valores
print("*** Função ROUND -> round(number4)***")
print("Arredonde o valor 11.7")
print(round(number4))
print(" ")
