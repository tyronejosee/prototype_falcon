"""
Health router configuration
"""

from src.resources.health import HealthResource


def configure_health_routes(app) -> None:
    app.add_route("/", HealthResource())
