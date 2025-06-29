"""
Health check resource
"""

import falcon
from falcon.request import Request
from falcon.response import Response


class HealthResource:
    """Health check resource"""

    async def on_get(self, req: Request, resp: Response) -> None:
        resp.status = falcon.HTTP_200
        resp.media = {"message": "Prototype Falcon is running"}
