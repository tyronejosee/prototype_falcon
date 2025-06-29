"""
Comment Falcon resources
"""

import falcon
from falcon.request import Request
from falcon.response import Response

from src.services.comment_service import comment_service


class CommentsResource:
    """Comments collection resource"""

    async def on_get(self, req: Request, resp: Response) -> None:
        try:
            comments = comment_service.get_all_comments()

            resp.status = falcon.HTTP_200
            resp.media = comments

        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}
