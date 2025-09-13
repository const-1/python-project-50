import os
from gendiff.parsers import parse_file

def load_file(file_path):
    """Load and parse data from file based on its extension."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")
    
    _, extension = os.path.splitext(file_path)
    format_name = extension.lstrip('.').lower()

    if format_name == 'yml':
        format_name = 'yaml'

    if format_name not in ['json', 'yaml']:
        raise ValueError(f"Unsupported format: {format_name}")

    try:
        data = parse_file(file_path, format_name)
    except Exception as e:
        raise ValueError(f"Error parsing file {file_path}: {str(e)}")

    return data, format_name

def load_data(file_path):
    """Alias for load_file that returns only data."""
    data, _ = load_file(file_path)
    return data
