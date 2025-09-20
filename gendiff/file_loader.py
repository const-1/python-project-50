import os
from gendiff.parsers import parse_file


def get_format_name(file_path):
    """Extract and normalize format name from file extension."""
    _, extension = os.path.splitext(file_path)
    format_name = extension.lstrip('.').lower()
    return 'yaml' if format_name == 'yml' else format_name


def load_file(file_path):
    """Load and parse data from file based on its extension."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")

    format_name = get_format_name(file_path)

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


