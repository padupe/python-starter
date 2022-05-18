my_set = {1, 2, 3}

print(f"Um conjunto em Python: {my_set}, e o seu tipo é {type(my_set)}.")

"""
IMPORTANTE: Conjuntos, ou seja, dados do tipo SET, não aceitam elementos repetidos.
Não é possível acessar um elemento dentro de um conjunto.
Por exemplo, não é possível realizar my_set[0]. Este código, gerará um erro.
"""

# Verificando o tamanho de um conjunto com elementos repetidos
my_set_two = {1, 2, 3, 4, 5, 5, 5}
print(f"Verificando o tamanho de um conjunto com elementos repetidos, utilizando o método LEN => {len(my_set_two)}.")

"""
Perceba que mesmo com o número 5 aparecendo três vezes, você receberá no Terminal a indicação que este conjunto possui o 'tamanho' 5
Isso ocorre pois os elementos repetidos são simplesmente ignorados pelo Python.
"""