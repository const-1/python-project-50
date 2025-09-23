import json


def format_value(value):
    """Convert value to JSON-serializable format."""
    if isinstance(value, (bool, type(None))):
        return value
    elif isinstance(value, (int, float)):
        return value
    elif isinstance(value, (dict, list)):
        return value
    else:
        return str(value)


def build_json_diff(diff):
    """Build a JSON-serializable diff structure."""
    result = {}
    
    for node in diff:
        key = node['key']
        node_type = node['type']
        
        if node_type == 'nested':
            result[f"  {key}"] = build_json_diff(node['children'])
        elif node_type == 'added':
            result[f"+ {key}"] = format_value(node['value'])
        elif node_type == 'removed':
            result[f"- {key}"] = format_value(node['value'])
        elif node_type == 'unchanged':
            result[f"  {key}"] = format_value(node['value'])
        elif node_type == 'changed':
            result[f"- {key}"] = format_value(node['old_value'])
            result[f"+ {key}"] = format_value(node['new_value'])
    
    return result


def format_json(diff):
    """Format diff as JSON string."""
    json_diff = build_json_diff(diff)
    return json.dumps(json_diff, indent=2, ensure_ascii=False)
