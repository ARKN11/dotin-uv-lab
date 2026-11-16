import pytest

from dotin_uv_lab.products.models import Product

# -------------------------
# Product creation
# -------------------------


def test_product_creation():
    product = Product(1, "Laptop", 1000)

    assert product.product_id == 1
    assert product.name == "Laptop"
    assert product.price == 1000


# -------------------------
# Product ID validation
# -------------------------


@pytest.mark.parametrize("product_id", [0, -1, -100])
def test_product_rejects_invalid_ids(product_id):
    with pytest.raises(ValueError):
        Product(product_id, "Laptop", 1000)


@pytest.mark.parametrize("product_id", [True, 1.5, "1"])
def test_product_rejects_invalid_id_types(product_id):
    with pytest.raises(TypeError):
        Product(product_id, "Laptop", 1000)


# -------------------------
# Product name validation
# -------------------------


@pytest.mark.parametrize("name", ["", " ", "   "])
def test_product_rejects_empty_names(name):
    with pytest.raises(ValueError):
        Product(1, name, 1000)


@pytest.mark.parametrize("name", [None, 123, True])
def test_product_rejects_invalid_name_types(name):
    with pytest.raises(TypeError):
        Product(1, name, 1000)


# -------------------------
# Price validation
# -------------------------


@pytest.mark.parametrize(
    "price",
    [0, 0.01, 100, 999999.99],
)
def test_product_accepts_valid_prices(price):
    product = Product(1, "Laptop", price)

    assert product.price == pytest.approx(price)


@pytest.mark.parametrize(
    "price",
    [-0.01, -1, -100],
)
def test_product_rejects_negative_prices(price):
    with pytest.raises(ValueError):
        Product(1, "Laptop", price)


@pytest.mark.parametrize(
    "price",
    [float("nan"), float("inf"), float("-inf")],
)
def test_product_rejects_non_finite_prices(price):
    with pytest.raises(ValueError):
        Product(1, "Laptop", price)


@pytest.mark.parametrize(
    "price",
    ["100", None, True],
)
def test_product_rejects_invalid_price_types(price):
    with pytest.raises(TypeError):
        Product(1, "Laptop", price)


# -------------------------
# Discount behavior
# -------------------------


@pytest.mark.parametrize(
    "discount, expected",
    [
        (0, 1000),
        (0.01, 999.9),
        (20, 800),
        (50, 500),
        (100, 0),
    ],
)
def test_apply_discount_returns_correct_price(
    sample_product,
    discount,
    expected,
):
    result = sample_product.apply_discount(discount)

    assert result == pytest.approx(expected)
    assert sample_product.price == 1000


@pytest.mark.parametrize(
    "discount",
    [-0.01, -1, 100.01, 101],
)
def test_apply_discount_rejects_out_of_range_values(
    sample_product,
    discount,
):
    with pytest.raises(ValueError):
        sample_product.apply_discount(discount)


@pytest.mark.parametrize(
    "discount",
    [float("nan"), float("inf"), float("-inf")],
)
def test_apply_discount_rejects_non_finite_values(
    sample_product,
    discount,
):
    with pytest.raises(ValueError):
        sample_product.apply_discount(discount)


@pytest.mark.parametrize(
    "discount",
    ["20", None, True],
)
def test_apply_discount_rejects_invalid_types(
    sample_product,
    discount,
):
    with pytest.raises(TypeError):
        sample_product.apply_discount(discount)
