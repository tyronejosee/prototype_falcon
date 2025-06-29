"""
Album Falcon resources
"""

import falcon
from falcon.request import Request
from falcon.response import Response

from src.services.album_service import album_service


class AlbumPhotosResource:
    """Album photos resource"""

    async def on_get(
        self, req: Request, resp: Response, album_id: str
    ) -> None:
        try:
            album_id = int(album_id)
            photos = album_service.get_album_photos(album_id)

            resp.status = falcon.HTTP_200
            resp.media = photos

        except ValueError:
            resp.status = falcon.HTTP_400
            resp.media = {"error": "Invalid album ID"}
        except Exception as e:
            resp.status = falcon.HTTP_500
            resp.media = {"error": str(e)}
