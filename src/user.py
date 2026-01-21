from datetime import datetime


class User:
    """A simple user class for user management."""

    def __init__(
        self,
        id: int,
        name: str,
        email: str,
        created_at: datetime | None = None,
        updated_at: datetime | None = None,
    ):
        self.id: int = id
        self.name: str = name
        self.email: str = email
        self.created_at: datetime | None = created_at
        self.updated_at: datetime | None = updated_at

    def __eq__(self, o: object) -> bool:
        if isinstance(o, User):
            return self.id == o.id

        return False
