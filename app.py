"""
Main Falcon ASGI application
"""

import falcon.asgi
from falcon.request import Request
from falcon.response import Response

from config import config
from src.routers.health_router import configure_health_routes
from src.routers.posts_router import configure_posts_routes
from src.routers.comments_router import configure_comments_routes
from src.routers.albums_router import configure_albums_routes
from src.routers.users_router import configure_users_routes


class CORSMiddleware:
    """
    CORS middleware for handling cross-origin requests
    """

    async def process_request(self, req: Request, resp: Response) -> None:
        resp.set_header("Access-Control-Allow-Origin", "*")
        resp.set_header(
            "Access-Control-Allow-Methods",
            "GET, POST, PUT, PATCH, DELETE, OPTIONS",
        )
        resp.set_header(
            "Access-Control-Allow-Headers",
            "Content-Type, Authorization",
        )

    async def process_response(
        self,
        req: Request,
        resp: Response,
        resource,
        req_succeeded,
    ) -> None:
        if req.method == "OPTIONS":
            resp.status = falcon.HTTP_200


def create_app():
    # Create Falcon ASGI app with middleware
    app = falcon.asgi.App(middleware=[CORSMiddleware()])

    # Configure all routes
    configure_health_routes(app)
    configure_posts_routes(app)
    configure_comments_routes(app)
    configure_albums_routes(app)
    configure_users_routes(app)

    return app


# Create the application instance
application = create_app()

if __name__ == "__main__":
    import uvicorn

    print(f"Starting {config.API_TITLE} on {config.HOST}:{config.PORT}")
    print("Available endpoints:")
    print("  GET / - Health check")
    print("  GET /posts - Get all posts")
    print("  GET /posts/{id} - Get post by ID")
    print("  POST /posts - Create post")
    print("  PUT /posts/{id} - Update post")
    print("  PATCH /posts/{id} - Partial update post")
    print("  DELETE /posts/{id} - Delete post")
    print("  GET /posts?userId={id} - Get posts by user")
    print("  GET /posts/{id}/comments - Get post comments")
    print("  GET /comments - Get all comments")
    print("  GET /albums/{id}/photos - Get album photos")
    print("  GET /users/{id}/albums - Get user albums")
    print("  GET /users/{id}/todos - Get user todos")
    print("  GET /users/{id}/posts - Get user posts")

    uvicorn.run(
        "app:application",
        host=config.HOST,
        port=config.PORT,
        reload=config.DEBUG,
        log_level="info",
    )
