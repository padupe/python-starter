print("Marcos da's Silva")
print("Marcos \nda Silva")

print("==== Definição de Variável [name] ====")
name = "João Paulo"
print(name)
print(" ")

# Concatenação
print("==== Concatenação ====")
print(name + " tem 19 anos de idade.")
print(" ")

# Funções

# Função para tornar toda a string em Letras Maiúsculas
print("==== Todas as letras maiúsculas ====")
print(name.upper())
print(" ")

# Função para tornar toda a string em Letras Minúsculas
print("==== Todas as letras minúsculas ====")
print(name.lower())

# Função para saber qual é o tamanho de uma String
print("==== Tamanho de uma String ====")
print(len(name))
print(" ")

# Função para realizar um filtro em uma String
print("==== Realizando filtros em uma String ====")
# Lembrando que a contagem começa em 0, 1, 2, 3...
print("**** Encontrando qual letra ocupa a posição na String [6] ****")
print(name[6])
print(" ")

# Para saber em qual posição começa a substring "Pa"
print("**** Para saber em qual posição começa uma Substring [Pa] ****")
print(name.index("Pa"))
print(" ")

# Para saber quantas letras existem na String
print("**** Para saber quantas vezes uma letra se repete na String [o]")
print(name.count("o"))
