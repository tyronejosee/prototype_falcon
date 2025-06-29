"""
Todo model and in-memory storage
"""

from dataclasses import dataclass

from src.core.id_generator import id_generator


@dataclass
class Todo:
    """Todo entity"""

    id: int
    userId: int
    title: str
    completed: bool


class TodoRepository:
    """In-memory todo repository"""

    def __init__(self) -> None:
        self._todos: dict[int, Todo] = {}
        self._initialize_sample_data()

    def _initialize_sample_data(self) -> None:
        sample_todos = [
            {"userId": 1, "title": "delectus aut autem", "completed": False},
            {"userId": 1, "title": "quis ut nam facilis", "completed": False},
            {"userId": 1, "title": "fugiat veniam minus", "completed": True},
            {"userId": 2, "title": "et porro tempora", "completed": True},
            {"userId": 2, "title": "laboriosam mollitia", "completed": False},
        ]

        for todo_data in sample_todos:
            todo_id = id_generator.get_next_id("todo")
            todo = Todo(id=todo_id, **todo_data)
            self._todos[todo_id] = todo

    def find_by_user_id(self, user_id: int) -> list[Todo]:
        """Get todos by user ID"""
        return [
            todo for todo in self._todos.values() if todo.userId == user_id
        ]


todo_repository = TodoRepository()
