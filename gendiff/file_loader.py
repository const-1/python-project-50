# python-project-50/gendiff/file_loader.py

import json
from pathlib import Path


def load_file(file_path):
    """
    Load and parse a JSON configuration file.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        dict: Parsed JSON data as Python dictionary
        
    Note: Converts relative paths to absolute paths
    """
    # Convert to absolute path for consistent behavior
    absolute_path = Path(file_path).resolve()
    
    # Open file using context manager (automatically handles file closing)
    with open(absolute_path, 'r') as file:
        # Parse JSON content into Python dictionary
        return json.load(file)
