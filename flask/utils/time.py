from datetime import datetime

def parse_datetime(value: str | None):
    if value is None:
        return None
    return datetime.fromisoformat(value)
