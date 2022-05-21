#!python3

from functools import reduce

notes = [
    6.4,
    7.2,
    5.8,
    8.4
]

print(f"Notas iniciais: {notes}.\n")

"""
PARA VERIFIARMOS O ÍNDICE E A NOTA DE CADA ALUNO:

for index, note in enumerate(notes):
    print(index, note)
"""

for index, note in enumerate(notes):
    notes[index] = note + 1.5
    
print(f"Notas após o acréscimo de 1.5: {notes}.\n")


# OUTRA POSSIBILIDADE

notes_two = [
    5.0,
    6.5,
    7.2,
    8.5
]

print(f"Novo conjunto de Notas: {notes_two}.\n")

for index in range(len(notes_two)):
    notes_two[index] = notes_two[index] + 1.5
    
print(f"Outra possibilidade de retornar o acréscimo de 1.5: {notes_two}.\n")

# UTILIZANDO MAP
print("=== UTILIZANDO MAP ===\n")

def adiciona_ponto(note):
    return note + 1.5

notes_three = [
    5.2,
    6.4,
    7.0,
    7.9
]

print(f"Conjunto de Notas 3: {notes_three}.\n")

final_notes = map(adiciona_ponto, notes_three)

print(f"Acréscimo de pontuação utilizando o MAP: {tuple(final_notes)}.\n")

# Nova Possibilidade
print("=== NOVA POSSIBILIDADE UTILIZANDO MAP ===\n")

def somar_nota(delta):
    def calculo(note):
        return note + delta
    return calculo

notes_four = [
    4.2,
    4.4,
    4.7,
    4.9
]

print(f"Conjunto de Notas 4: {notes_four}.\n")

finally_notes = map(somar_nota(1.5), notes_four)

print(f"Acréscimo de pontuação utilizando o MAP [2]: {tuple(finally_notes)}.\n")

print("=== USANDO REDUCE ===\nIremos calcular o total de notas [4].\n")

def somar_notas_turma(a, b):
    return a + b

total_turma = reduce(somar_notas_turma, notes_four, 0)
print(f"O total das notas somadas [4] é {round(total_turma, 2)}.\n")