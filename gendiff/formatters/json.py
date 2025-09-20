import json


def format_json(diff):
    """Format diff as JSON string."""
    return json.dumps(diff, indent=2)


