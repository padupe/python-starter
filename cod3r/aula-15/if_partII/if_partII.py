# Outros cenários utilizando IF

a = "value" # True
print(f"Variável 'a': {a}.\n")

if a:
    print("Variável 'a' Existe.\n")
else:
    print("'a' Não existe (zero, vazio ou, de fato, não existe).\n")
    
b = 0 # False
print(f"Variável 'b': {b}.\n")

if b:
    print("Variável 'b' Existe.\n")
else:
    print("Variável 'b' Não existe (zero, vazio ou, de fato, não existe).\n")
    
c = -0.00001 # True
print(f"Variável 'c': {c}.\n")

if c:
    print("Variável 'c' Existe.\n")
else:
    print("Variável 'c' Não existe (zero, vazio ou, de fato, não existe).\n")
    
d = "" # False
print(f"Variável 'd': {d}.\n")

if d:
    print("Variável 'd' Existe.\n")
else:
    print("Variável 'd' Não existe (zero, vazio ou, de fato, não existe).\n")
    
e = " " # True
print(f"Variável 'e': {e}.\n")

if e:
    print("Variável 'e' Existe.\n")
else:
    print("Variável 'e' Não existe (zero, vazio ou, de fato, não existe).\n")
    
f = [] # False
print(f"Variável 'f': {f}.\n")

if f:
    print("Variável 'f' Existe.\n")
else:
    print("Variável 'f' Não existe (zero, vazio ou, de fato, não existe).\n")

g = {} # False
print(f"Variável 'g': {g}.\n")

if g:
    print("Variável 'g' Existe.\n")
else:
    print("Variável 'g' Não existe (zero, vazio ou, de fato, não existe).\n")