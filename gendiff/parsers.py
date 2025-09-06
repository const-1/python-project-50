import json
import yaml

def parse(content, format_name):
    """Parse content based on format."""
    if format_name == 'json':
        return json.loads(content)
    elif format_name in ['yml', 'yaml']:  # Принимаем оба варианта
        return yaml.safe_load(content)
    else:
        raise ValueError(f"Unsupported format: {format_name}")

def parse_file(file_path, format_name):
    """Parse file content based on format."""
    with open(file_path, 'r') as file:
        content = file.read()
    return parse(content, format_name)
