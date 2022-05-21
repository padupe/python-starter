"""
OPERADORES ARITMÉTICOS

+ Adição
- Subtração
* Multiplicação
/ Divisão
% Módulo (Resto da Divisão)

"""

# +3 prefix
# x++ postfix
# x + y infix

x = 10
y = 2

print(f"Criamos duas variáveis:\nx = {x};\ny = {y}.\n")
print(f"Soma de x + y => { x + y }.\n")
print(f"Subtração de x - y => { x - y }.\n")
print(f"Multiplicação de x * y => { x * y }.\n")
print(f"Divisão de x / y => { x / y }.\n")
print(f"Módulo (Resto da Divisão) de x % y => { x % y }.\n")

"""
Validando se um número é par ou ímpar.

Podemos criar variávies e utilizar do Módulo (%) para validar:
"""

print("==== Validando se um número é par ou ímpar ====")

par = 10
impar = 5

print(f"Variáveis criadas para o teste:\n- par = {par};\n- impar = {impar}.\n")
print(f"10 é par?\nUtilizamos o seguinte código 'par % 2 == 0' => { par % 2 == 0 }.\n")
print(f"5 é ímpar?\nUtilizamos o seguinte código 'impar % 2 == 1' => { impar % 2 == 1 }.\n")