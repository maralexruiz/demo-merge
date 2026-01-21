from datetime import datetime


class Invoice:
    """A simple invoice class for billing management."""

    def __init__(
        self,
        id: int,
        user_id: int,
        amount: float,
        description: str,
        status: str = "pending",
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ):
        self.id: int = id
        self.user_id: int = user_id
        self.amount: float = amount
        self.description: str = description
        self.status: str = status
        self.created_at: datetime | None = created_at
        self.updated_at: datetime | None = updated_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Invoice):
            return self.id == o.id

        return False

    def __repr__(self) -> str:
        return f"<Invoice(id={self.id}, amount={self.amount}, status='{self.status}')>"
