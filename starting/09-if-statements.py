print("==== If Statements ====")

acordei_antes_9h = False

"""
IMPORTANTE: True e False devem sempre ser escritos iniciando com letra maiúscula
"""

print("**** IF / ELSE ****\n")

if acordei_antes_9h:
    print("Hora de fazer café da manhã.\n")
else:
    print("Hora de fazer o almoço.\n")
    
    
print("**** ELIF ****\n")
    
acordei_antes_8h = False
fome = True

if acordei_antes_8h and fome:
    print("Hora de fazer o café da manhã, pois já estou com fome!\n")
elif acordei_antes_8h and not fome:
    print("Hora de fazer uma caminhada!\n")
else:
    print("Hora de fazer o almoço!\n")
    

print("*** Using OR ***\n")

tanque_cheio = False
meio_taque = True

if tanque_cheio or meio_taque:
    print("Ok! Temos combustível para viajar!")
else:
    print("Precisamos abastecer o carro!")