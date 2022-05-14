# Lists, podem ser resumidos em arrays

print("==== Lists ====\n\nLists are arrays.")

friends = [
    "Anna",
    "Bianca",
    "Erick",
    "Lucas",
    "Muarício",
    "Rodrigo",
    "Samuel",
    "Vitor",
    "Yago"
]

print("List all Friends: " + str(friends))

"""
Podemos utilizar o index (sumário, índice) do array para printar um elemento específico
Para isso, basta utilizar, por exemplo = print(friends[2]), e teremos como retorno "Erick"
"""

print("Find an friend at index 2: " + str(friends[2]) +".\n")

"""
E se nossa lista (array), possuísse muitos elementos. Por exemplo, 1000, e eu quisesse saber
qual o amigo está no último elemento? Em Python basta usar a numeração negativa, por exemplo,
para saber o último elemento utilizamos "-1", o penúltimo "-2" e assim por diante.

Por exemplo, se quisermos saber o último elemento da lista friends, executaríamos o código a seguir:
print(friends[-1])
O retorno seria "Yago"
"""

print("Find a friend on last position of list with '-1': " + str(friends[-1]) + ".\n")

"""
Podemos também retornar um intervalo de elementos da nossa Lista
Por exemplo, quero retornar os cinco primeiros amigos da lista.

Devemos implementar o código a seguir:
print(friends[0:5])
O retorno seria: ['Anna', 'Bianca', 'Erick', 'Lucas', 'Muarício']

Mas por que até 5?
Porque o Python vai parar de ler no quinto elemento (começando de 0 -> 0,1,2,3,4)
Abaixo um exemplo objetivo:
"""

print("Listing the first five friends with '[0-5]': " + str(friends[0:5]) + ".\n")

"""
Podemos também "pular" elementos.
Por exemplo, se quisermos printar a partir do terceiro amigo?

Devemos implementar o código a seguir:
print(friends[2:])
O retorno seria: ['Erick', 'Lucas', 'Muarício', 'Rodrigo', 'Samuel', 'Vitor', 'Yago']

Abaixo um exemplo objetivo:
"""

print("Listing from 3rd friend onwards with '[2:]': " + str(friends[2:]) + ".\n")

"""
Outra coisa legal que podemos fazer com listas, é manipular os dados a partir de um ponto.
Em resumo, basta passar o index (índice) do elemento que queremos alterar e passar o novo valor.

Por exemplo, iremos alterar "Bianca" para "Bianca Zanol".
Para isso, iremos implementar o código:
friends[1] = "Bianca Zanol"

Ao realizarmos um print da lista de amigos -> print(friends), receberemos o seguinte retorno:
['Anna', 'Bianca Zanol', 'Erick', 'Lucas', 'Muarício', 'Rodrigo', 'Samuel', 'Vitor', 'Yago']
"""

friends[1] = "Bianca Zanol"
print("Update Friends List with 'friends[1] = \"Bianca Zanol\"': " + str(friends) + ".\n")