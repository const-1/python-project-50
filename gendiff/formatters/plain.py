def stringify_value(value):
    """Convert value to string representation for plain format."""
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, (int, float)):
        return str(value)
    elif isinstance(value, (dict, list)):
        return '[complex value]'
    else:
        return f"'{value}'"


def format_plain(diff, path=''):
    """Format diff as plain text."""
    lines = []
    
    for node in diff:
        current_path = f"{path}.{node['key']}" if path else node['key']
        node_type = node['type']
        
        if node_type == 'nested':
            lines.append(format_plain(node['children'], current_path))
        elif node_type == 'added':
            value = stringify_value(node['value'])
            lines.append(
                    f"Property '{current_path}' was added "
                    f"with value: {value}"
                    )
        elif node_type == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == 'changed':
            old_value = stringify_value(node['old_value'])
            new_value = stringify_value(node['new_value'])
            lines.append(
                    f"Property '{current_path}' was updated."
                    f"From {old_value} to {new_value}"
                    )
            
    return '\n'.join(lines)


