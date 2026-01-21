from datetime import datetime


class Company:
    """A simple company class for organization management."""

    def __init__(
        self,
        id: int,
        name: str,
        tax_id: str,
        address: str | None = None,
        is_active: bool = True,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ):
        self.id: int = id
        self.name: str = name
        self.tax_id: str = tax_id
        self.address: str | None = address
        self.is_active: bool = is_active
        self.created_at: datetime | None = created_at
        self.updated_at: datetime | None = updated_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, Company):
            return self.id == o.id

        return False

    def __repr__(self) -> str:
        return f"<Company(id={self.id}, name='{self.name}', active={self.is_active})>"

    @property
    def info(self):
        return f"{self.name} - Address: {self.address or 'N/A'}"
