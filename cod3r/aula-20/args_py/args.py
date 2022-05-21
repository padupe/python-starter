def soma(*numbers):
    total = 0
    
    for n in numbers:
        total += n
    return total

# KWARGS = Argumentos nomeados
def resultado_final(**kwargs):
    
    status = "Aprovado(a)" if kwargs["nota"] >= 7 else "Reprovado(a)"
    return(f"{kwargs['nome']} foi {status}.")