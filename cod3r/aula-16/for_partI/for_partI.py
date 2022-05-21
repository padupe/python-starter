#!python3

"""
FOR - Laços de Repetição
"""
print("Primeiro FOR: 'for i in range(10):'")
for i in range(10):
    print(i)

print("\nSegundo FOR: 'for i in range(1, 11):'")
for i in range(1, 11):
    print(i)
    
print("\nTerceiro FOR: 'for i in range(1, 100, 5):'\n[ De 1 a 100, com os 'passos' de 5 em 5 ]")
for i in range(1, 100, 5):
    print(i)
    
print("\nQuarto FOR: 'for i in range(20, 0, -3):'\n[ De 20 a 0 (diminuindo), com os 'passos' de -3 em -3 ]")
for i in range(20, 0, -3):
    print(i)
    
print("\nCriamos a variável 'numbers' para novos casos de uso do FOR.")
numbers = [2, 4, 6, 8]
print(f"numbers = {numbers}.\n")

# END = é um parâmetro utilizado para separar os itens em um for

print("Quinto FOR: 'for n in numbers:\n             print(n, end=', ')'\n[ Passe por todos os itens da variável 'numbers' e os separe por ', ' (vírgula e um espaço em branco) ]")
for n in numbers:
    print(n, end=", ")
    
print("\nCriamos a variável 'text' para novos casos de uso do FOR.")
text = "Python é muito massa!"
print(f"text = {text}.\n")

print("Sexto FOR: 'for letter in text:\n             print(letter, end=', ')'\n[ Passe por todos os itens da variável 'text' e os separe por ' ' (um espaço em branco) ]")
for letter in text:
    print(letter, end=" ")
    
print("\n\nSétimo FOR em um Conjunto/SET:")
for n in {1, 2, 3, 4, 4, 4 }:
    print(n, end=" ")
    
print("\n\nOitavo FOR em um Dicionário/DICT:")

print("\nCriamos a variável 'product' para novos casos de uso do FOR.")

product = {
    "name": "Caneta",
    "price": 0.80,
    "discount": 0
}

print(f"product = {product}.\n")

for attribute in product:
    print(attribute, "=>", product[attribute])

print("\n")    
# Segunda maneira de percorrer um DICT
for attribute, value in product.items():
    print(attribute, "==>", value)

# Terceira maneira de percorrer um DICT  (percorrendo apenas os atributos)  
print("\n")
for attributes in product.keys():
    print(attributes, end=" ")