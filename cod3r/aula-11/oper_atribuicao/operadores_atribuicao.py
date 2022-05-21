"""
OPERADORES DE ATRIBUÇÃO

+= Para acrescentar novos valores a variável
-= Para remover valores da variável
*= Para multiplicar o valor da variável
/= Para dividir o valor da variável
%= Para realizar o módulo (resto da divisão) de uma variável

"""

result = 2
print(f"Valor inicial da variável result = {result}.\n")

result += 3 # result = result (2) + 3 => 5
print(f"result após receber o incremento = {result}.\n")

result -= 1 # result = result (5) - 1 => 4
print(f"result após receber o decremento = {result}.\n")

result *= 4 # result = result (4) * 4 => 16
print(f"result após receber a multiplicação = {result}.\n")

result /= 2 # result = result (16) / 2 => 8
print(f"result após receber a divisão = {int(result)}.\n")

result %= 6 # result = result (8) % 6 => 2
print(f"result após receber a multiplicação = {int(result)}.\n")

result -= result # result = result (2) - result (2) => 0
print(f"result - result = {int(result)}.\n")