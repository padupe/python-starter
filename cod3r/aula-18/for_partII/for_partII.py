"""
FOR - Part II
"""

persons = [
    "Guilherme",
    "Rebeca"
]

adjectives = [
    "Sapeca",
    "Inteligente"
]

for p in persons:
    for a in adjectives:
        print(f"{p} é {a}!")
        
# Laço Vazio
for i in [ 1, 2, 3 ]:
    pass


"""
Verificando entre os números 1 e 11 quais são PARES
- Sempre que o resultado do RESTO DA DIVISÃO for 1, o for continuará percorrendo os números
- Serão impressos apenas os números PARES, ou seja, que o RESTO DA DIVISÃO é 0
"""
for i in range(1, 11):
    if i % 2:
        continue
    print(i, end=" ")
    
print("\n")

"""
BRAKE - De freiar/parar
Quando tem uma condição atendida, para a repetição e SAI do laço.
"""

for i in range(1, 11):
    if i == 5:
        break
    print(i)

print("Fim\n")