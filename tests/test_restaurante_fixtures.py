import pytest
from restaurante import Restaurante

RESTAURANTE="Pizzaria X"

@pytest.fixture
def restaurante_fila_vazia():
    return Restaurante(RESTAURANTE)

@pytest.fixture
def restaurante_com_pedido():
    return Restaurante(RESTAURANTE, 1)

def test_pedidos_na_fila_valor_inicial_padrao_igual_a_zero(restaurante_fila_vazia):
    assert restaurante_fila_vazia.orders_in_the_queue == 0
    
def test_pedidos_na_fila_valor_inicial_maior_que_zero(restaurante_com_pedido):
    assert restaurante_com_pedido.orders_in_the_queue == 1
    
def test_pedidos_na_fila_valor_inicial_menor_que_zero():
    with pytest.raises(ValueError):
        Restaurante(RESTAURANTE, -1)
        
def test_adiciona_um_pedido_na_fila(restaurante_com_pedido):
    restaurante_com_pedido.add_order()
    assert restaurante_com_pedido.orders_in_the_queue == 2
    
def test_remove_um_pedido_da_fila(restaurante_com_pedido):
    restaurante_com_pedido.remove_order()
    assert restaurante_com_pedido.orders_in_the_queue == 0
    
def test_remove_um_pedido_da_fila_vazia(restaurante_fila_vazia):
    restaurante_fila_vazia.remove_order()
    assert restaurante_fila_vazia.orders_in_the_queue == 0