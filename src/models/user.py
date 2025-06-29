"""
User model and in-memory storage
"""

from dataclasses import dataclass

from src.core.id_generator import id_generator


@dataclass
class User:
    """User entity"""

    id: int
    name: str
    email: str


class UserRepository:
    """In-memory user repository"""

    def __init__(self) -> None:
        self._users: dict[int, User] = {}
        self._initialize_sample_data()

    def _initialize_sample_data(self) -> None:
        sample_users = [
            {"name": "Leanne Graham", "email": "Sincere@april.biz"},
            {"name": "Ervin Howell", "email": "Shanna@melissa.tv"},
            {"name": "Clementine Bauch", "email": "Nathan@yesenia.net"},
        ]

        for user_data in sample_users:
            user_id = id_generator.get_next_id("user")
            user = User(id=user_id, **user_data)
            self._users[user_id] = user

    def find_by_id(self, user_id: int) -> User | None:
        return self._users.get(user_id)


user_repository = UserRepository()
