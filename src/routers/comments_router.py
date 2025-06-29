"""
Comments router configuration
"""

from src.resources.comments import CommentsResource


def configure_comments_routes(app) -> None:
    app.add_route("/comments", CommentsResource())
