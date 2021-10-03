import uuid


def primary_key() -> str:
    return str(uuid.uuid4())
