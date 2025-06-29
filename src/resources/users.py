"""
User Falcon resources
"""

import falcon
from falcon.request import Request
from falcon.response import Response

from src.services.user_service import user_service


class UserAlbumsResource:
    """User albums resource"""

    async def on_get(self, req: Request, resp: Response, user_id: str) -> None:
        try:
            user_id = int(user_id)
            albums = user_service.get_user_albums(user_id)

            resp.status = falcon.HTTP_200
            resp.media = albums

        except ValueError:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Invalid user ID"}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}


class UserTodosResource:
    """User todos resource"""

    async def on_get(self, req: Request, resp: Response, user_id: str) -> None:
        try:
            user_id = int(user_id)
            todos = user_service.get_user_todos(user_id)

            resp.status = falcon.HTTP_200
            resp.media = todos

        except ValueError:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Invalid user ID"}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}


class UserPostsResource:
    """User posts resource"""

    async def on_get(self, req: Request, resp: Response, user_id: str) -> None:
        try:
            user_id = int(user_id)
            posts = user_service.get_user_posts(user_id)

            resp.status = falcon.HTTP_200
            resp.media = posts

        except ValueError:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Invalid user ID"}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}
