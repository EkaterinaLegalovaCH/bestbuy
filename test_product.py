import pytest
import products


def test_creating_product():
    assert products.Product("MacBook Air M2", 1450, 100, promotion=None).name == "MacBook Air M2"
    assert products.Product("MacBook Air M2", 1450, 100, promotion=None).price == 1450
    assert products.Product("MacBook Air M2", 1450, 100, promotion=None).quantity == 100


def test_creating_prod_invalid_details():
    assert products.Product("", 1450, 100, promotion=None).name == None
    assert products.Product("MacBook Air M2", -1450, 100, promotion=None).price == 0
    assert products.Product("MacBook Air M2", 1450, 0, promotion=None).quantity == 0


def test_product_becomes_inactive():
    mac = products.Product("MacBook Air M2", 1450, 100, promotion=None)
    assert mac.set_quantity(0) == False

def test_buy_modifies_quantity():
    mac = products.Product("MacBook Air M2", 1450, 100, promotion=None)
    mac.buy(50)
    assert mac.quantity == 50


def test_buy_too_much():
    mac = products.Product("MacBook Air M2", 1450, 100, promotion=None)
    assert mac.buy(150) == "Sorry, chosen quantity bigger than exist!"


