import json
import yaml

def parse(content, format_name):
    """Parse content based on format."""
    if format_name == 'json':
        try:
            return json.loads(content)
        except json.JSONDecodeError as e:
            raise ValueError(f"JSON parsing error: {str(e)}")
    elif format_name == 'yaml':
        try:
            return yaml.safe_load(content)
        except yaml.YAMLError as e:
            raise ValueError(f"YAML parsing error: {str(e)}")
    else:
        raise ValueError(f"Unsupported format: {format_name}")

def parse_file(file_path, format_name):
    """Parse file content based on format."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return parse(content, format_name)
    except IOError as e:
        raise ValueError(f"Error reading file {file_path}: {str(e)}")
