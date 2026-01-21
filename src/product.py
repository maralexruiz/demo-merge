from datetime import datetime


class Product:
    """A simple product class for inventory and billing."""

    def __init__(
        self,
        id: int,
        sku: str,
        price: float,
        name: str,
        created_at: datetime | None = None,
    ):
        self.id: int = id
        self.sku: str = sku
        self.price: float = price
        self.name: str = name
        self.created_at: datetime | None = created_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Product):
            return self.id == o.id
        return False
