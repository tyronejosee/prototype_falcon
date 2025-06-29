# Prototype Falcon

A modular and scalable REST API built with Falcon (ASGI) that replicates the behavior of JSONPlaceholder. This project demonstrates clean architecture principles with separation of concerns and extensibility for future enhancements.

```mermaid
graph TD
    A[app.py] -->|Configures| B(Routers)
    B --> C1[src/routers/health_router.py]
    B --> C2[src/routers/posts_router.py]
    B --> C3[src/routers/comments_router.py]
    B --> C4[src/routers/albums_router.py]
    B --> C5[src/routers/users_router.py]

    C1 --> D1[src/resources/health.py]
    C2 --> D2[src/resources/posts.py]
    C3 --> D3[src/resources/comments.py]
    C4 --> D4[src/resources/albums.py]
    C5 --> D5[src/resources/users.py]

    D2 --> E1[src/services/post_service.py]
    D3 --> E2[src/services/comment_service.py]
    D4 --> E3[src/services/album_service.py]
    D5 --> E4[src/services/user_service.py]

    E1 --> F1[src/models/post.py]
    E1 --> F2[src/models/comment.py]
    E2 --> F2
    E3 --> F3[src/models/album.py]
    E3 --> F4[src/models/photo.py]
    E4 --> F5[src/models/user.py]
    E4 --> F3
    E4 --> F6[src/models/todo.py]
    E4 --> F1

    E1 --> G1[src/schemas/post_schema.py]

    subgraph Configuration
        H[config.py]
    end
```

## ✨ Features

- In-memory data storage with auto-incrementing IDs
- JSON responses for all endpoints
- Basic validation for required fields
- CORS support
- Error handling and appropriate HTTP status codes

## ⚙️ Installation & Running

Clone the repository

```bash
git clone https://github.com/tyronejosee/prototype_falcon.git
```

> Note: Python and [UV](https://docs.astral.sh/uv/) is required for running the application.

Create a virtual environment and install dependencies

```bash
uv venv
```

Activate the virtual environment

```bash
# Windows
.venv\Scripts\activate.ps1

# Linux/Mac
source .venv/bin/activate
```

```bash
uv pip install -r requirements.txt
```

Run the application using uvicorn

```bash
uvicorn app:application --reload
```

The API will be available at `http://localhost:8000`

## 🌱 Endpoints

### Health Check

- `GET /` - API health check

### Posts

- `GET /posts` - Get all posts
- `GET /posts/{id}` - Get specific post
- `POST /posts` - Create new post
- `PUT /posts/{id}` - Update post
- `PATCH /posts/{id}` - Partial update post
- `DELETE /posts/{id}` - Delete post
- `GET /posts?userId={id}` - Filter posts by user
- `GET /posts/{id}/comments` - Get post comments

### Comments

- `GET /comments` - Get all comments

### Albums & Photos

- `GET /albums/{id}/photos` - Get album photos

### Users

- `GET /users/{id}/albums` - Get user albums
- `GET /users/{id}/todos` - Get user todos
- `GET /users/{id}/posts` - Get user posts

Enjoy! 🎉
