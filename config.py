class Config:
    """
    Application configuration
    """

    # Server settings
    HOST = "0.0.0.0"
    PORT = 8000
    DEBUG = True

    # API settings
    API_VERSION = "v1"
    API_TITLE = "JSONPlaceholder Falcon API"

    # CORS settings
    CORS_ORIGINS = ["*"]
    CORS_METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
    CORS_HEADERS = ["Content-Type", "Authorization"]


config = Config()
