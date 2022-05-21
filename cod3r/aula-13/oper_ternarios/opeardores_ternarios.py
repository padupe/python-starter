"""
OPERADOR TERNÁRIO

Estrutura:
variável = cenário | SE (if) | condição para cenário 1 ser verdadeiro | OU (else) | cenário 2

"""

print("==== Operador Ternário ====")

lockdown = True

status = "Devido ao lockdown, fique em casa!" if lockdown else "Fim da pandemia!"

print(f"Status: {status}.\n")

# Exemplo 2

health = True
money = 50

travel = "Viagem cancelada" if health or money < 100 else "Vamos viajar!"

print(f"Status para nossa viagem é {travel}.\n")