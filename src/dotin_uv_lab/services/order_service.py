from dotin_uv_lab.customers import Customer
from dotin_uv_lab.products import Product

def build_order_summary(customer: Customer, product: Product) -> str:
    customer_details = customer.get_details()
    product_details = product.get_details()
    return f"Order Summary:\n{customer_details}\n{product_details}"