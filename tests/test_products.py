import pytest

from dotin_uv_lab.products.models import Product


def test_product_creation_with_valid_data():
    # Arrange
    product_id = 1
    name = "Keyboard"
    price = 100.0

    # Act
    product = Product(product_id, name, price)

    # Assert
    assert product.product_id == product_id
    assert product.name == name
    assert product.price == price


def test_product_creation_with_negative_id():
    with pytest.raises(ValueError):
        Product(-1, "Keyboard", 100.0)


def test_product_creation_with_empty_name():
    with pytest.raises(ValueError):
        Product(1, "   ", 100.0)


def test_product_creation_with_negative_price():
    with pytest.raises(ValueError):
        Product(1, "Keyboard", -100.0)


def test_product_discount_20_percent():
    product = Product(1, "Keyboard", 100.0)

    discounted_price = product.apply_discount(20)

    assert discounted_price == 80.0
    assert product.price == 100.0


def test_product_discount_zero_percent():
    product = Product(1, "Keyboard", 100.0)

    discounted_price = product.apply_discount(0)

    assert discounted_price == 100.0
    assert product.price == 100.0


def test_product_discount_100_percent():
    product = Product(1, "Keyboard", 100.0)

    discounted_price = product.apply_discount(100)

    assert discounted_price == 0.0
    assert product.price == 100.0


def test_product_discount_above_100_percent():
    product = Product(1, "Keyboard", 100.0)

    with pytest.raises(ValueError):
        product.apply_discount(101)


def test_product_negative_discount():
    product = Product(1, "Keyboard", 100.0)

    with pytest.raises(ValueError):
        product.apply_discount(-10)
