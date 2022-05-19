nota = float(input("Informe a nota do aluno: "))

if nota >= 9:
    print(f"Nota: {nota}.\nDuas palavras: 'para' 'béns'! :D\nQuadro de Honra.")
elif nota >= 7:
    print(f"Nota: {nota}.\nVocê foi aprovado! :)")
elif nota >= 5:
    print(f"Nota: {nota}.\nVocê está de recuperação! :/")
else:
    print(f"Nota: {nota}.\nVocê está Reprovado. :(")