name_one, age_one = "Anna", 32
name_two, age_two = "Bianca", 31
name_three, age_three = "Erick", 33

# Primeira Maneira [Mais Antiga]
"""
%s -> String
%d -> Número Inteiro
%f -> Número Float (Decimal)
  %.2f -> Float com duas casas decimais
"""
print("Name: %s, Age: %d" % (name_one, age_one))

# Segunda maneira -> Python < 3.6
"""
Pode ser escrita assim também, informando os índices:
print("Name: {1}, Age: {2}".format(name_two, age_two))
"""
print("Name: {}, Age: {}".format(name_two, age_two))

# Terceira Maneira -> Python >= 3.6
print(f"Name: {name_three}, Age: {age_three}.")