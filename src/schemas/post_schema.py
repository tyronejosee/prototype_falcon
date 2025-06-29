"""
Post validation schemas
"""


class PostValidator:
    """Post validation logic"""

    @staticmethod
    def validate_create(data: dict) -> list[dict]:
        errors = []

        if not data.get("title"):
            errors.append("Title is required")

        if not data.get("body"):
            errors.append("Body is required")

        if not isinstance(data.get("userId"), int) or data.get("userId") <= 0:
            errors.append("Valid userId is required")

        return errors

    @staticmethod
    def validate_update(data: dict) -> list[dict]:
        errors = []

        if "title" in data and not data["title"]:
            errors.append("Title cannot be empty")

        if "body" in data and not data["body"]:
            errors.append("Body cannot be empty")

        if "userId" in data and (
            not isinstance(data["userId"], int) or data["userId"] <= 0
        ):
            errors.append("Valid userId is required")

        return errors
