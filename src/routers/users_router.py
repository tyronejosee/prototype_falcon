"""
Users router configuration
"""

from src.resources.users import (
    UserAlbumsResource,
    UserTodosResource,
    UserPostsResource,
)


def configure_users_routes(app) -> None:
    app.add_route("/users/{user_id}/albums", UserAlbumsResource())
    app.add_route("/users/{user_id}/todos", UserTodosResource())
    app.add_route("/users/{user_id}/posts", UserPostsResource())
