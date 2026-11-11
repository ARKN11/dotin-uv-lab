from dotin_uv_lab.products import Product
from dotin_uv_lab.customers.models import Customer
from dotin_uv_lab.products.operations import create_sample_product
from dotin_uv_lab.services import build_order_summary

user1 = Customer(1,"Amir")
p1 = Product(1, "Laptop", 1200.00)

print(user1.get_details())
print(p1.get_details())
p2 = create_sample_product()
print(p2.get_details())
print(build_order_summary(user1, p1))