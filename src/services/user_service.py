"""
User business logic service
"""

from src.models.user import user_repository
from src.models.album import Album, album_repository
from src.models.todo import Todo, todo_repository
from src.models.post import Post, post_repository


class UserService:
    """User business logic service"""

    def __init__(self):
        self.repository = user_repository
        self.album_repository = album_repository
        self.todo_repository = todo_repository
        self.post_repository = post_repository

    def get_user_albums(self, user_id: int) -> list[dict]:
        albums = self.album_repository.find_by_user_id(user_id)
        return [self._album_to_dict(album) for album in albums]

    def get_user_todos(self, user_id: int) -> list[dict]:
        todos = self.todo_repository.find_by_user_id(user_id)
        return [self._todo_to_dict(todo) for todo in todos]

    def get_user_posts(self, user_id: int) -> list[dict]:
        posts = self.post_repository.find_by_user_id(user_id)
        return [self._post_to_dict(post) for post in posts]

    def _album_to_dict(self, album: Album) -> dict:
        return {
            "id": album.id,
            "userId": album.userId,
            "title": album.title,
        }

    def _todo_to_dict(self, todo: Todo) -> dict:
        return {
            "id": todo.id,
            "userId": todo.userId,
            "title": todo.title,
            "completed": todo.completed,
        }

    def _post_to_dict(self, post: Post) -> dict:
        return {
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "userId": post.userId,
        }


user_service = UserService()
