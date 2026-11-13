"""Product domain entity and its invariants."""

import math


class Product:
    """A product with validated identity, name, and price."""

    def __init__(self, product_id: int, name: str, price: int | float) -> None:
        if isinstance(product_id, bool) or not isinstance(product_id, int):
            raise TypeError("product_id must be an integer")
        if product_id <= 0:
            raise ValueError("product_id must be greater than zero")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        normalized_name = name.strip()
        if not normalized_name:
            raise ValueError("name must not be empty")
        if isinstance(price, bool) or not isinstance(price, (int, float)):
            raise TypeError("price must be a number")
        normalized_price = float(price)
        if not math.isfinite(normalized_price):
            raise ValueError("price must be finite")
        if normalized_price < 0:
            raise ValueError("price must not be negative")

        self.product_id = product_id
        self.name = normalized_name
        self.price = normalized_price

    def get_details(self) -> str:
        """Return a human-readable product description."""
        return f"{self.name} - ${self.price:.2f}"

    def apply_discount(self, percentage: int | float) -> float:
        """Return the price after a percentage discount without mutating it."""
        if isinstance(percentage, bool) or not isinstance(percentage, (int, float)):
            raise TypeError("percentage must be a number")
        normalized_percentage = float(percentage)
        if not math.isfinite(normalized_percentage):
            raise ValueError("percentage must be finite")
        if not 0 <= normalized_percentage <= 100:
            raise ValueError("Discount must be between 0 and 100")
        return self.price * (1 - normalized_percentage / 100)
