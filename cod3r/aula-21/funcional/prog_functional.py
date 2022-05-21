def soma(a, b):
    return a + b

def subtraco(a, b):
    return a - b

somar = soma
print(somar(3,4))

def operacao_aritmetica(function, operador1, operador2):
    return function(operador1, operador2)

result = operacao_aritmetica(soma, 13, 48)
print(result)

result = operacao_aritmetica(subtraco, 51, 1)
print(result)


def soma_parcial(number1):
    def concluir_soma(number2):
        return number1 + number2
    return concluir_soma

fn = soma_parcial(10)
final_result = fn(12)
print(f"Resultado da função que chama outra função é: {final_result}.")

"""
Poderíamos escrever assim:

def soma_parcial(number1):
    def concluir_soma(number2):
        return number1 + number2
    return concluir_soma

final_result = somar_parcial(10)(12)
print(f"Resultado da função que chama outra função é: {final_result}.")

Essa abordagem pode ser mais simples na hora da codificação.
Porém, pode consumir muito tempo de execução.
Assim sendo, devemos buscar sempre SEPARAR o processamento em partes, de maneira que economizamos tempo.
"""