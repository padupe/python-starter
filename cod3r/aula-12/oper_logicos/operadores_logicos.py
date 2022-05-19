"""
OPERADORES LÓGICOS

AND -> E
Or -> OU
!= -> DIFERENTE
NOT -> NÃO / NEGAÇÃO
"""

print("==== Operadores Lógicos ====")

b1 = True
b2 = False
b3 = True

print(f"Criamos três variáveis para os testes:\n- b1 = {b1};\n- b2 = {b2};\n- b3 = {b3}.\n")

print(f"Comparando as três variáveis: 'b1 and b2 and b3' => { b1 and b2 and b3 }.\n")
print(f"Comparando as três variáveis: 'b1 or b2 or b3' => { b1 or b2 or b3 }.\n")
print(f"Comparando as duas variáveis: 'b1 != b2' => { b1 != b2 }.\n")
print(f"Mudando b2 de False para True: 'not b2' => { not b2 }.\n")

x = 3
y = 4

print(f"Se b1 for True, e X ({x}) for menor que Y ({y}) retorne TRUE => { b1 and x < y }")
