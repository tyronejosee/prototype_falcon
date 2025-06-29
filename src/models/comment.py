"""
Comment model and in-memory storage
"""

from dataclasses import dataclass

from src.core.id_generator import id_generator


@dataclass
class Comment:
    """Comment entity"""

    id: int
    postId: int
    name: str
    email: str
    body: str


class CommentRepository:
    """In-memory comment repository"""

    def __init__(self) -> None:
        self._comments: dict[int, Comment] = {}
        self._initialize_sample_data()

    def _initialize_sample_data(self) -> None:
        sample_comments = [
            {
                "postId": 1,
                "name": "id labore ex et quam laborum",
                "email": "Eliseo@gardner.biz",
                "body": "laudantium enim quasi est quidem magnam",
            },
            {
                "postId": 1,
                "name": "quo vero reiciendis velit similique",
                "email": "Jayne_Kuhic@sydney.com",
                "body": "est natus enim nihil est dolore omnis",
            },
            {
                "postId": 2,
                "name": "odio adipisci rerum aut animi",
                "email": "Nikita@garfield.biz",
                "body": "quia molestiae reprehenderit quasi",
            },
            {
                "postId": 2,
                "name": "alias odio sit",
                "email": "Lew@alysha.tv",
                "body": "non et atque occaecati deserunt quas",
            },
        ]

        for comment_data in sample_comments:
            comment_id = id_generator.get_next_id("comment")
            comment = Comment(id=comment_id, **comment_data)
            self._comments[comment_id] = comment

    def find_all(self) -> list[Comment]:
        return list(self._comments.values())

    def find_by_post_id(self, post_id: int) -> list[Comment]:
        return [
            comment
            for comment in self._comments.values()
            if comment.postId == post_id
        ]


comment_repository = CommentRepository()
