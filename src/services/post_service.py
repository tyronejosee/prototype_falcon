"""
Post business logic service
"""

from src.models.post import Post, post_repository
from src.models.comment import Comment, comment_repository
from src.schemas.post_schema import PostValidator


class PostService:
    """Post business logic service"""

    def __init__(self) -> None:
        self.repository = post_repository
        self.comment_repository = comment_repository
        self.validator = PostValidator()

    def get_all_posts(self, user_id: int | None = None) -> list[dict]:
        if user_id:
            posts = self.repository.find_by_user_id(user_id)
        else:
            posts = self.repository.find_all()

        return [self._post_to_dict(post) for post in posts]

    def get_post_by_id(self, post_id: int) -> dict | None:
        post = self.repository.find_by_id(post_id)
        return self._post_to_dict(post) if post else None

    def create_post(self, post_data: dict) -> dict:
        errors = self.validator.validate_create(post_data)
        if errors:
            raise ValueError(f"Validation errors: {', '.join(errors)}")

        post = self.repository.create(post_data)
        return self._post_to_dict(post)

    def update_post(self, post_id: int, post_data: dict) -> dict | None:
        errors = self.validator.validate_update(post_data)
        if errors:
            raise ValueError(f"Validation errors: {', '.join(errors)}")

        post = self.repository.update(post_id, post_data)
        return self._post_to_dict(post) if post else None

    def partial_update_post(
        self,
        post_id: int,
        post_data: dict,
    ) -> dict | None:
        errors = self.validator.validate_update(post_data)
        if errors:
            raise ValueError(f"Validation errors: {', '.join(errors)}")

        post = self.repository.partial_update(post_id, post_data)
        return self._post_to_dict(post) if post else None

    def delete_post(self, post_id: int) -> bool:
        return self.repository.delete(post_id)

    def get_post_comments(self, post_id: int) -> list[dict]:
        if not self.repository.find_by_id(post_id):
            return []

        comments = self.comment_repository.find_by_post_id(post_id)
        return [self._comment_to_dict(comment) for comment in comments]

    def _post_to_dict(self, post: Post) -> dict:
        return {
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "userId": post.userId,
        }

    def _comment_to_dict(self, comment: Comment) -> dict:
        return {
            "id": comment.id,
            "postId": comment.postId,
            "name": comment.name,
            "email": comment.email,
            "body": comment.body,
        }


post_service = PostService()
