"""
Album business logic service
"""

from src.models.album import album_repository
from src.models.photo import Photo, photo_repository


class AlbumService:
    """Album business logic service"""

    def __init__(self) -> None:
        self.repository = album_repository
        self.photo_repository = photo_repository

    def get_album_photos(self, album_id: int) -> list[dict]:
        photos = self.photo_repository.find_by_album_id(album_id)
        return [self._photo_to_dict(photo) for photo in photos]

    def _photo_to_dict(self, photo: Photo) -> dict:
        return {
            "id": photo.id,
            "albumId": photo.albumId,
            "title": photo.title,
            "url": photo.url,
            "thumbnailUrl": photo.thumbnailUrl,
        }


album_service = AlbumService()
