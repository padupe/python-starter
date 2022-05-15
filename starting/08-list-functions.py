print("==== List Functions ====\nUsing functions in Lists\n")

numbers = [ 3, 5, 12, 15, 18, 22, 1, 4, 2 ]
print("List Numbers: " + str(numbers) +".\n")
friends = [ "Adriano", "Bruna", "Carlos Alberto", "Jonathan", "Luanda", "Raphaela" ]
print("List Friends: " + str(friends) +".\n")

"""
Function EXTENDS
No exemplos vamos informar que a lista FRIENDS extende a de NUMBERS
Código a ser implementado:

frindes.extend(numbers)
print("Friends List extends Numbers List: " + str(friends) + ".\n")

Retorno esperado:
Friends List extends Numbers List: ['Adriano', 'Bruna', 'Carlos Alberto', 'Jonathan', 'Luanda', 'Raphaela', 3, 5, 12, 15, 18, 22].
"""

print("==== Function Extends ====\n")

friends.extend(numbers)
print("Friends List extends Numbers List: " + str(friends) + ".\n")

"""
Function APPEND
Para adicionar um elemento a uma Lista
No exemplo, vamos adicionar um time a lista TEAMS

Código a ser implementado:
teams = [ "Avaí", "Chapecoense", "Goiás", "Santos" ]
teams.append("Vitória")
print("Update list of teams using 'append' function: " + str(teams) + ".\n")

Retorno esperado:
Update list of teams using 'append' function: ['Avaí', 'Chapecoense', 'Goiás', 'Santos', 'Vitória'],
"""

print("==== Function Append ====\n")

teams = [ "Avaí", "Chapecoense", "Goiás", "Santos" ]
teams.append("Vitória")
print("Update list of teams using 'append' function: " + str(teams) + ".\n")

"""
Podemos ainda indicar uma posição específica para inserir um novo elemento na lista
Para isso, utilizamos a função INSERT. É necessário informar o index (índice), ou seja, a posição do elemento no array,
e o próprio elemento.

EXEMPLO
Código a ser implementado:
teams.insert(1, "Botafogo")
print("Update list of teams using 'insert' function: " + str(teams) + ".\n")

Retorno esperado:
Update list of teams using 'insert' function: ['Avaí', 'Botafogo', 'Chapecoense', 'Goiás', 'Santos', 'Vitória'].
"""

print("==== Function Insert ====\n")

teams.insert(1, "Botafogo")
print("Update list of teams using 'insert' function: " + str(teams) + ".\n")

"""
Podemos ainda remover um elemento na lista
Para isso, podemos utilizar a função REMOVE. É necessário informar o elemento no que desejamos remover.

EXEMPLO
Código a ser implementado:
teams.remove("Vitória")
print("Update list of teams using 'remove' function: " + str(teams) + ".\n")

Retorno esperado:
Update list of teams using 'remove' function: ['Avaí', 'Botafogo', 'Chapecoense', 'Goiás', 'Santos'].
"""

print("==== Function Remove ====\n")

teams.remove("Vitória")
print("Update list of teams using 'remove' function: " + str(teams) + ".\n")

"""
Outra maneira possível de remover um elemento na lista é utilizar a função POP.
É necessário informar o index (índice) do elemento no array que desejamos remover.

EXEMPLO
Código a ser implementado:
teams.pop(3)
print("Update list of teams using 'pop' function: " + str(teams) + ".\n")

Retorno esperado:
Update list of teams using 'pop' function: ['Avaí', 'Botafogo', 'Chapecoense', 'Santos'].
"""

print("==== Function Pop ====\n")

teams.pop(3)
print("Update list of teams using 'pop' function: " + str(teams) + ".\n")

"""
Podemos também verificar se um elemento existe na lista.

EXEMPLO -> Queremos saber se existe o time SANTOS na lista, e qual seu index.
Código a ser implementado:
print("Check if there is the 'Santos' team in the list.: " + str(teams.index("Santos")) + ".\n")

Retorno esperado:
Check if there is the 'Santos' team in the list.: 3.
"""

print("*** Checking the existence of an element in the list *** \n")
print("Check if there is the 'Santos' team in the list.: " + str(teams.index("Santos")) + ".\n")

"""
Podemos também verificar a quantidade de vezes que um elemento aparece na lista.

EXEMPLO > Queremos saber quantas vezes o time SANTOS aparece na lista.
Código a ser implementado:
print("Check if there is the 'Santos' team in the list.: " + str(teams.count("Santos")) + ".\n")

Retorno esperado:
Check if there is the 'Santos' team in the list.: 3.
"""

print("*** Checking the number of repetitions of an element in the list *** \n")
print("Check how many times the team 'Santos' appears in the list: " + str(teams.count("Santos")) + ".\n")

"""
Podemos também organizar uma lista por ordem.

EXEMPLO > Queremos ordenar a lista de NUMBERS.
Código a ser implementado:
numbers.sort()
print("Arrange the list of numbers in ascending order: " + str(numbers) + ".\n")

Retorno esperado:
Check if there is the 'Santos' team in the list.: 3.
"""

print("*** Sorting a List *** \n")
numbers.sort()
print("Arrange the list of numbers in ascending order: " + str(numbers) + ".\n")