class Customer:
    def __init__(self, customer_id: int, name: str)->None:
        self.customer_id = customer_id
        self.name = name

    def get_details(self)-> str:
        return f"Customer: {self.name}"