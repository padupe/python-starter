#!python3

"""
Maneiras de realizar o import de um função no Python:

Exemplo 1:
from functions import basic

basico.saudacao()

Exemplo 2:
from functions.basic import saudacao

saudacao()
"""

from functions.basic import saudacao
from functions.basic import saudacao_nome
from functions.basic import soma_e_multiplica

saudacao()

saudacao_nome("Paulo")

result = soma_e_multiplica(number1=10, number2=5, number3=2)
print(f"O resultado da expressão é {result}.")
