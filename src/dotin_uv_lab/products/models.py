class Product:
    def __init__(self, product_id:int, name:str, price:float) -> None:
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_details(self) -> str:
        return f'{self.name} - ${self.price:.2f}'