from .models import Product
def create_sample_product(product_id:int = 101, name:str = 'Keyboard', price:float = 75.50) -> Product:
    return Product(product_id, name, price)