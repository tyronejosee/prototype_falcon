"""
Photo model and in-memory storage
"""

from dataclasses import dataclass

from src.core.id_generator import id_generator


@dataclass
class Photo:
    """Photo entity"""

    id: int
    albumId: int
    title: str
    url: str
    thumbnailUrl: str


class PhotoRepository:
    """In-memory photo repository"""

    def __init__(self):
        self._photos: dict[int, Photo] = {}
        self._initialize_sample_data()

    def _initialize_sample_data(self):
        sample_photos = [
            {
                "albumId": 1,
                "title": "accusamus beatae ad facilis",
                "url": "https://via.placeholder.com/600/92c952",
                "thumbnailUrl": "https://via.placeholder.com/150/92c952",
            },
            {
                "albumId": 1,
                "title": "reprehenderit est deserunt",
                "url": "https://via.placeholder.com/600/771796",
                "thumbnailUrl": "https://via.placeholder.com/150/771796",
            },
            {
                "albumId": 2,
                "title": "officia porro iure quia",
                "url": "https://via.placeholder.com/600/24f355",
                "thumbnailUrl": "https://via.placeholder.com/150/24f355",
            },
            {
                "albumId": 2,
                "title": "culpa odio esse rerum",
                "url": "https://via.placeholder.com/600/d32776",
                "thumbnailUrl": "https://via.placeholder.com/150/d32776",
            },
        ]

        for photo_data in sample_photos:
            photo_id = id_generator.get_next_id("photo")
            photo = Photo(id=photo_id, **photo_data)
            self._photos[photo_id] = photo

    def find_by_album_id(self, album_id: int) -> list[Photo]:
        return [
            photo
            for photo in self._photos.values()
            if photo.albumId == album_id
        ]


photo_repository = PhotoRepository()
