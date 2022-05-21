# Criando Tuplas
"""
Ao contrário das Listas, TUPLAS utilizam paretêses ()
"""

names = ("Anna", "Bianca", "Lucas", "Monnylly")
print(f"Uma tupla => {names}.\nValidando o TYPE de uma tupla => {type(names)}.")

"""
Podemos verificar se um elemento existe em uma tupla.
Basta usar a sintaxe:

"Bia" in names

como implementaríamos este código:
print("Bianca" in names)

O retorno seria:
True

IMPORTANTE: Se implementássemos print("bianca" in names), o retorno seria False, devido o "B" estar minúsculo.
Em resumo, o elemento buscado deve estar idêntico ao buscado na tupla
"""

# Validando se o elemento existe na Tupla
print(f"Validando se o elemento 'Bia' existe na tupla 'names' => {'Bianca' in names}.")

# Verificando um elemento específico de uma Tupla
"""
Assim como nas listas, podemos verificar qual elemento ocupa uma posição na lista:
names[0]

Podemos ainda, assim como nas Listas, verificar um conjunto de elementos, por exemplo:
names[0:2]
Será printado: ("Anna", "Bianca")

E por que não "Lucas" que está na posição 2?
Porque o Python vai exibir até a posição 2, mas sem a incluir (na realidade, a pesquisa é entre elementos 0 e 1, parando no 2)
"""

print(f"Printando um conjunto de elementos utilizando 'names[0-2]' => {names[0:2]}.")

"""
É possível mesclar a consulta por conjuntos, conforme exemplos abaixo:
[1:-1] => Não irá exibir "Anna" e "Monnylly"
[2:] => Irá exibir "Lucas" e "Monnylly"
"""

print(f"Outros exemplos de consulta por conjuntos de elementos:\n - Utilizando '[1:-1] => {names[1:-1]}.\n - Utilizando '[2:]' => {names[2:]}")
print(f" - Utilizando '[:-2]' => {names[:-2]}.\n - Utilizando '[1:3]' => {names[1:3]}.")

# Verificando o tamanho de uma Tupla
print(f"Verificando o tamanho de um Tupla utilizando LEN: 'len(names)' => {len(names)}.")