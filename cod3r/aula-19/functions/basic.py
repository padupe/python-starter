#!python3

"""
FUNCTIONS (Funções) - Introdução às funções em Python

DEF -> Palavra reservada para definir uma função (No Javascript temos o function)
SINTAXE DO NOME -> padrão snake case:
    Exemplo:
    
    def meu_exemplo():
"""
 
"""
Função que NÃO REALIZA NADA
Funções que não realizam nada, precisam ter ao menos um PASS
"""
def nao_faz_nada():
    pass

def saudacao():
    print("Bom dia!")
    
def saudacao_nome(name):
    print(f"{name}, Bom dia!")
    
"""
Se eu quiser que a função seja executada apenas deste arquivo, posso adotar a estratégia a seguir:
"""    
if __name__ == "__main__":
    saudacao_nome("Ana")
    

def soma_e_multiplica(number1, number2, number3):
    return number1 + number2 * number3