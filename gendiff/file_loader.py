import os
from gendiff.parsers import parse_file

def load_file(file_path):
    """Load and parse data from file based on its extension."""
    _, extension = os.path.splitext(file_path)
    format_name = extension.lstrip('.').lower()
    
    # Нормализуем название формата для YAML
    if format_name == 'yml':
        format_name = 'yaml'
    
    data = parse_file(file_path, format_name)
    return data, format_name

# Алиас для обратной совместимости
def load_data(file_path):
    """Alias for load_file that returns only data."""
    data, _ = load_file(file_path)
    return data
