import pytest

from dotin_uv_lab.products.models import Product


@pytest.fixture
def sample_product():
    return Product(1, "Laptop", 1000)
