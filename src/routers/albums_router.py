"""
Albums router configuration
"""

from src.resources.albums import AlbumPhotosResource


def configure_albums_routes(app) -> None:
    app.add_route("/albums/{album_id}/photos", AlbumPhotosResource())
