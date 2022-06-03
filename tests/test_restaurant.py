import pytest
from restaurante import Restaurante

RESTAURANTE="Pizzaria X"

def test_pedidos_na_fila_valor_inicial_padrao_igual_a_zero():
    restaurante = Restaurante(RESTAURANTE)
    assert restaurante.orders_in_the_queue == 0
    
def test_pedidos_na_fila_valor_inicial_maior_que_zero():
    restaurante = Restaurante(RESTAURANTE, 1)
    assert restaurante.orders_in_the_queue == 1
    
def test_pedidos_na_fila_valor_inicial_menor_que_zero():
    with pytest.raises(ValueError):
        Restaurante(RESTAURANTE, -1)
        
def test_adiciona_um_pedido_na_fila():
    restaurante = Restaurante(RESTAURANTE, 1)
    restaurante.add_order()
    assert restaurante.orders_in_the_queue == 2
    
def test_remove_um_pedido_da_fila():
    restaurante = Restaurante(RESTAURANTE, 1)
    restaurante.remove_order()
    assert restaurante.orders_in_the_queue == 0
    
def test_remove_um_pedido_da_fila_vazia():
    restaurante = Restaurante(RESTAURANTE)
    restaurante.remove_order()
    assert restaurante.orders_in_the_queue == 0