numbers = [1, 2, 3]

print(f"Utilizando o método TYPE para saber que tipo de dado recebemos em um Array/Lista => {type(numbers)}")

# Adicionando um novo elemento na lista

numbers.append(4)
# Para se saber o TAMANHO de uma lista, utilizamos a função LEN
print(f"Como saber o tamanho de uma lista utilizando LEN => {len(numbers)}")

# Alterando o valor de um elemento/índice da lista
"""
Iremos alterar o elemento 3 da lista (lembrando que sempre começamos em 0)
Atualmente o valor é 4, e iremos alterar para 100
"""
numbers[3] = 100
print(f"Alterando o valor de um índice => {numbers}")

# Realizando um insert em uma lista
"""
IMPORTANTE: Este método não permite elementos repetidos (como o APPEND permite)
É ncessário informar a posição/índice que irá ocupar na lista e seu valor.

Exemplo:
numbers.insert(0, -1)

-> Quero inserir na POSIÇÃO zero, o VALOR -1
"""

numbers.insert(0, -200)
print(f"Lista de números atualizada com INSERT => {numbers}")

# Printando o último elemento de uma Lista
"""
Podemos realizar, quando sabemos o "tamanho" de uma lista o método:
print(numbers[4])

Mas em uma lista muito grande, podemos utilizar o método:
print(numbers[-1])

=> Em resumo conta-se de "trás para frente" a partir do -1
"""

print(f"Printando o último elemento de uma lista utilizando [-1] => {numbers[-1]}")

# Verificando se um elemento existe na Lista
print(f"Verificando se o número 2 existe na lista utilizando '2 in numbers' => {2 in numbers}.")