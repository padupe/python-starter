import pytest

def soma_1(number):
    return int(number) + 1


def test_soma_1():
    assert soma_1(41) == 42
    
def test_soma_1_number_string():
    assert soma_1("41") == 42
    
# Quando quero que valide apenas se vai dar erro
def test_soma_1_word():
    with pytest.raises(ValueError):
        soma_1("fabio")
        