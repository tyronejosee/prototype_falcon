"""
Posts router configuration
"""

from src.resources.posts import (
    PostsResource,
    PostResource,
    PostCommentsResource,
)


def configure_posts_routes(app) -> None:
    app.add_route("/posts", PostsResource())
    app.add_route("/posts/{post_id}", PostResource())
    app.add_route("/posts/{post_id}/comments", PostCommentsResource())
