"""
Album model
"""

from dataclasses import dataclass

from src.core.id_generator import id_generator


@dataclass
class Album:
    """Album entity"""

    id: int
    userId: int
    title: str


class AlbumRepository:
    """In-memory album repository"""

    def __init__(self) -> None:
        self._albums: dict[int, Album] = {}
        self._initialize_sample_data()

    def _initialize_sample_data(self) -> None:
        sample_albums = [
            {"userId": 1, "title": "quidem molestiae enim"},
            {"userId": 1, "title": "sunt qui excepturi placeat culpa"},
            {"userId": 2, "title": "omnis laborum odio"},
            {"userId": 2, "title": "non esse culpa molestiae omnis"},
        ]

        for album_data in sample_albums:
            album_id = id_generator.get_next_id("album")
            album = Album(id=album_id, **album_data)
            self._albums[album_id] = album

    def find_by_user_id(self, user_id: int) -> list[Album]:
        return [
            album for album in self._albums.values() if album.userId == user_id
        ]


album_repository = AlbumRepository()
