"""
Post Falcon resources
"""

import falcon
from falcon.request import Request
from falcon.response import Response

from src.services.post_service import post_service


class PostsResource:
    """Posts collection resource"""

    async def on_get(self, req: Request, resp: Response) -> None:
        try:
            user_id = req.get_param_as_int("userId")
            posts = post_service.get_all_posts(user_id=user_id)

            resp.status = falcon.HTTP_200
            resp.media = posts

        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}

    async def on_post(self, req: Request, resp: Response) -> None:
        try:
            post_data = req.media or {}
            post = post_service.create_post(post_data)

            resp.status = falcon.HTTP_201
            resp.media = post

        except ValueError as e:
            resp.status = falcon.HTTP_400
            resp.media = {"error": str(e)}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}


class PostResource:
    """Single post resource"""

    async def on_get(self, req: Request, resp: Response, post_id: str) -> None:
        try:
            post_id = int(post_id)
            post = post_service.get_post_by_id(post_id)

            if post:
                resp.status = falcon.HTTP_200
                resp.media = post
            else:
                resp.status = falcon.HTTP_404
                resp.media = {"error": "Post not found"}

        except ValueError:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Invalid post ID"}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}

    async def on_put(self, req: Request, resp: Response, post_id: str) -> None:
        try:
            post_id = int(post_id)
            post_data = req.media or {}
            post = post_service.update_post(post_id, post_data)

            if post:
                resp.status = falcon.HTTP_200
                resp.media = post
            else:
                resp.status = falcon.HTTP_404
                resp.media = {"error": "Post not found"}

        except ValueError as e:
            resp.status = falcon.HTTP_400
            resp.media = {"error": str(e)}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}

    async def on_patch(
        self, req: Request, resp: Response, post_id: str
    ) -> None:
        try:
            post_id = int(post_id)
            post_data = req.media or {}
            post = post_service.partial_update_post(post_id, post_data)

            if post:
                resp.status = falcon.HTTP_200
                resp.media = post
            else:
                resp.status = falcon.HTTP_404
                resp.media = {"error": "Post not found"}

        except ValueError as e:
            resp.status = falcon.HTTP_400
            resp.media = {"error": str(e)}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}

    async def on_delete(
        self, req: Request, resp: Response, post_id: str
    ) -> None:
        try:
            post_id = int(post_id)
            deleted = post_service.delete_post(post_id)

            if deleted:
                resp.status = falcon.HTTP_200
                resp.media = {"message": "Post deleted successfully"}
            else:
                resp.status = falcon.HTTP_404
                resp.media = {"error": "Post not found"}

        except ValueError:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Invalid post ID"}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}


class PostCommentsResource:
    """Post comments resource"""

    async def on_get(self, req: Request, resp: Response, post_id: str) -> None:
        try:
            post_id = int(post_id)
            comments = post_service.get_post_comments(post_id)

            resp.status = falcon.HTTP_200
            resp.media = comments

        except ValueError:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Invalid post ID"}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}
