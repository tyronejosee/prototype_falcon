"""
Comment business logic service
"""

from src.models.comment import Comment, comment_repository


class CommentService:
    """Comment business logic service"""

    def __init__(self) -> None:
        self.repository = comment_repository

    def get_all_comments(self) -> list[dict]:
        comments = self.repository.find_all()
        return [self._comment_to_dict(comment) for comment in comments]

    def _comment_to_dict(self, comment: Comment) -> dict:
        return {
            "id": comment.id,
            "postId": comment.postId,
            "name": comment.name,
            "email": comment.email,
            "body": comment.body,
        }


comment_service = CommentService()
