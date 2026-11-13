"""Typed inventory helper functions used during the Python typing block."""

from typing import TypedDict


class ProductRecord(TypedDict):
    product_id: int
    name: str
    price: float
    stock: int


def calculate_inventory_value(products: list[ProductRecord]) -> float:
    """Return the combined value of all currently stocked units."""
    return sum(product["price"] * product["stock"] for product in products)


def find_product_by_id(
    products: list[ProductRecord], product_id: int
) -> ProductRecord | None:
    """Find a product by its identifier, or return None when absent."""
    for product in products:
        if product["product_id"] == product_id:
            return product
    return None


def find_low_stock_products(
    products: list[ProductRecord], threshold: int = 5
) -> list[ProductRecord]:
    """Return products whose stock is below the supplied threshold."""
    return [product for product in products if product["stock"] < threshold]
