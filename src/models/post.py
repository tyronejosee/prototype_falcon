"""
Post model and in-memory storage
"""

from dataclasses import dataclass
from src.core.id_generator import id_generator


@dataclass
class Post:
    """Post entity"""

    id: int
    title: str
    body: str
    userId: int


class PostRepository:
    """In-memory post repository"""

    def __init__(self):
        self._posts: dict[int, Post] = {}
        self._initialize_sample_data()

    def _initialize_sample_data(self):
        sample_posts = [
            {
                "title": "sunt aut facere repellat provident",
                "body": "quia et suscipit\nsuscipit recusandae",
                "userId": 1,
            },
            {
                "title": "qui est esse",
                "body": "est rerum tempore vitae\nsequi sint",
                "userId": 1,
            },
            {
                "title": "ea molestias quasi exercitationem",
                "body": "et iusto sed quo iure\nvoluptatem occaecati",
                "userId": 1,
            },
            {
                "title": "eum et est occaecati",
                "body": "ullam et saepe reiciendis voluptatem",
                "userId": 2,
            },
            {
                "title": "nesciunt quas odio",
                "body": "repudiandae veniam quaerat sunt sed",
                "userId": 2,
            },
        ]

        for post_data in sample_posts:
            post_id = id_generator.get_next_id("post")
            post = Post(id=post_id, **post_data)
            self._posts[post_id] = post

    def find_all(self) -> list[Post]:
        return list(self._posts.values())

    def find_by_id(self, post_id: int) -> Post | None:
        return self._posts.get(post_id)

    def find_by_user_id(self, user_id: int) -> list[Post]:
        return [
            post for post in self._posts.values() if post.userId == user_id
        ]

    def create(self, post_data: dict) -> Post:
        post_id = id_generator.get_next_id("post")
        post = Post(
            id=post_id,
            title=post_data.get("title", ""),
            body=post_data.get("body", ""),
            userId=post_data.get("userId", 1),
        )
        self._posts[post_id] = post
        return post

    def update(self, post_id: int, post_data: dict) -> Post | None:
        if post_id not in self._posts:
            return None

        post = self._posts[post_id]
        post.title = post_data.get("title", post.title)
        post.body = post_data.get("body", post.body)
        post.userId = post_data.get("userId", post.userId)

        return post

    def partial_update(self, post_id: int, post_data: dict) -> Post | None:
        return self.update(post_id, post_data)

    def delete(self, post_id: int) -> bool:
        if post_id in self._posts:
            del self._posts[post_id]
            return True
        return False


post_repository = PostRepository()
