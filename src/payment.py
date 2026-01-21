from datetime import datetime


class Payment:
    """A simple payment class to track invoice settlements."""

    def __init__(
        self,
        id: int,
        invoice_id: int,
        user_id: int,
        amount: float,
        method: str,
        processed_at: datetime | None = None,
    ):
        self.id: int = id
        self.invoice_id: int = invoice_id
        self.user_id: int = user_id
        self.amount: float = amount
        self.method: str = method
        self.processed_at: datetime | None = processed_at or datetime.now()

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Payment):
            return self.id == o.id
        return False

    class Meta:
        """Meta class for Payment."""

        table_name: str = "payments"
        metadata: dict = {
            "description": "Table to store payment records for invoices.",
            "version": 1.0,
        }
