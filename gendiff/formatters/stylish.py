def stringify_value(value, depth):
    if isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        indent = '    ' * (depth + 1)
        lines = []
        for key, val in value.items():
            lines.append(f"{indent}{key}: {stringify_value(val, depth + 1)}")
        return '{\n' + '\n'.join(lines) + '\n' + '    ' * depth + '}'
    else:
        return str(value)


def format_stylish(diff, depth=0):
    lines = []
    indent = '    ' * depth
    
    for node in diff:
        key = node['key']
        type_ = node['type']
        
        if type_ == 'nested':
            lines.append(f"{indent}    {key}: {{")
            lines.append(format_stylish(node['children'], depth + 1))
            lines.append(f"{indent}    }}")
        elif type_ == 'added':
            value = stringify_value(node['value'], depth + 1)  
            lines.append(f"{indent}  + {key}: {value}")
        elif type_ == 'removed':
            value = stringify_value(node['value'], depth + 1)  
            lines.append(f"{indent}  - {key}: {value}")
        elif type_ == 'unchanged':
            value = stringify_value(node['value'], depth + 1)  
            lines.append(f"{indent}    {key}: {value}")
        elif type_ == 'changed':
            old_value = stringify_value(node['old_value'], depth + 1)  
            new_value = stringify_value(node['new_value'], depth + 1)  
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
    
    if depth == 0:
        return '{\n' + '\n'.join(lines) + '\n}'
    return '\n'.join(lines)


