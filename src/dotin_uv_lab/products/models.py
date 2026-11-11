class Product:
    def __init__(self, product_id:int, name:str, price:float) -> None:
        self.product_id = product_id
        self.name = name
        self.price = price

    def get_details(self) -> str:
        return f'{self.name} - ${self.price:.2f}'

    def apply_discount(self, percentage: float) -> float:
        if not 0 <= percentage <= 100:
            raise ValueError("Discount must be between 0 and 100")

        return self.price * (1 - percentage / 100)