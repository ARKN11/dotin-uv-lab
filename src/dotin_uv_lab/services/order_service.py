"""Order-related application service functions."""

from dotin_uv_lab.customers.models import Customer
from dotin_uv_lab.products.models import Product


def build_order_summary(customer: Customer, product: Product) -> str:
    """Build a display summary from a customer and a product."""
    return f"Order Summary:\n{customer.get_details()}\n{product.get_details()}"
