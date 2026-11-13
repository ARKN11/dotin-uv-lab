"""Customer domain entity and its invariants."""


class Customer:
    """A customer known to the application."""

    def __init__(self, customer_id: int, name: str) -> None:
        if isinstance(customer_id, bool) or not isinstance(customer_id, int):
            raise TypeError("customer_id must be an integer")
        if customer_id <= 0:
            raise ValueError("customer_id must be greater than zero")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        normalized_name = name.strip()
        if not normalized_name:
            raise ValueError("name must not be empty")

        self.customer_id = customer_id
        self.name = normalized_name

    def get_details(self) -> str:
        """Return a human-readable customer description."""
        return f"Customer: {self.name}"
