import pytest
from restaurante import Restaurante

RESTAURANTE="Pizzaria X"

"""
Criamos dois parâmetros:
- inicial
- final

Depois, criamos um array de tuplas, com os valores correspondentes ao INICIAL e FINAL.

Criamos uma função "teste_remocao_de_pedidos", e chamamos os parâmetros INICIAL e FINAL.
Ou seja, esperamos que setando o valor INICIAL, após utilizar a função "remove_order", que o resultado seja igual ao valor FINAL.
"""    
@pytest.mark.parametrize("inicial,final", [(0,0),(1,0),(2,1)])
def teste_remocao_de_pedidos(inicial, final):
    restaurante = Restaurante(RESTAURANTE, inicial)
    restaurante.remove_order()
    assert restaurante.orders_in_the_queue == final