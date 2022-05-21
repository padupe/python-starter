# Dicionários lembra objetos JSON

students = {
    "name": "Pedro Henrique",
    "note": 9.2,
    "active": True
}

print(f"Um dicionário (DICT) => {students}.\n")
print(f"Verificando o tipo do DICT students (Dicionário) => {type(students)}.\n")

"""
É possível mapear o objeto/dict gerado
"""

print(f"Verificando o valor da chave 'name' no dict 'students' => {students['name']}.\n")
print(f"Verificando o valor da chave 'note' no dict 'students' => {students['note']}.\n")
print(f"Verificando o valor da chave 'active' no dict 'students' => {students['active']}.\n")
print(f"Verificando o tamanho do dict 'students' => {len(students)}.\n")