import json


def format_value(value):
    """Convert value to JSON-serializable format."""
    if isinstance(value, (bool, type(None))):
        return value
    elif isinstance(value, (int, float)):
        return value
    elif isinstance(value, dict):
        return {k: format_value(v) for k, v in value.items()}
    elif isinstance(value, list):
        return [format_value(item) for item in value]
    else:
        return str(value)


def format_json(diff):
    """Format diff as JSON string."""
    return json.dumps(diff, indent=2, ensure_ascii=False)
