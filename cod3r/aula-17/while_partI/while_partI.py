"""
WHILE -> Traduzindo para Português, seria ENQUANTO
"""
print("==== WHILE ====\n")

print("==== Exemplo 1 ====\n")
x = 0

"""
No exemplo, podemos entender:
- ENQUANTO (while) x for DIFERENTE de -1, continue rodando o INPUT
- QUANDO for -1, imprima no console "Fim"
"""

while x != -1:
    x = float(input("Informe o número ou '-1' para sair: "))

print("Fim")
    
print("\n==== Exemplo 2 ====\n")

total = 0
note = 0
quantity = 0


while note != -1:
    note = float(input(f"Informe a 'nota' ou -1 para sair: "))
    
    if note != -1:
        quantity += 1
        total += note

print(f"A média da turma é { total / quantity }.\n")

print("==== Exemplo 3 ====\n")

number = 10

while number:
    print(f"Number: {number}")
    number -= 1

print("Fim da contagem regressiva!")