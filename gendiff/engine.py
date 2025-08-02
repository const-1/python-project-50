import json
from pathlib import Path

def format_value(value):
    """Convert Python values to string representation for diff output"""
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)
    return value  # strings are returned as-is

def generate_diff(data1, data2):
    """
    Generate a formatted diff between two data sources (dicts or file paths).
    
    Args:
        data1 (dict | str | Path): First data (dictionary or file path)
        data2 (dict | str | Path): Second data (dictionary or file path)
    
    Returns:
        str: Formatted diff string showing differences between dictionaries
    
    Raises:
        TypeError: If inputs are not dictionaries or valid paths
        FileNotFoundError: If input file doesn't exist
        ValueError: If file contains invalid JSON
    """
    # Convert Path objects to strings
    if isinstance(data1, Path):
        data1 = str(data1)
    if isinstance(data2, Path):
        data2 = str(data2)

    # Process first input
    if isinstance(data1, str):
        try:
            with open(data1, 'r') as f:
                data1 = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file not found: {data1}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {data1}")
    
    # Process second input
    if isinstance(data2, str):
        try:
            with open(data2, 'r') as f:
                data2 = json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Input file not found: {data2}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON format in file: {data2}")
    
    # Validate input types
    if not isinstance(data1, dict):
        raise TypeError(f"Expected dict, got {type(data1).__name__} for first argument")
    if not isinstance(data2, dict):
        raise TypeError(f"Expected dict, got {type(data2).__name__} for second argument")
    
    # Generate sorted list of all unique keys
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    
    # Build diff lines
    lines = []
    for key in all_keys:
        if key not in data2:
            val = format_value(data1[key])
            lines.append(f"  - {key}: {val}")
        elif key not in data1:
            val = format_value(data2[key])
            lines.append(f"  + {key}: {val}")
        elif data1[key] == data2[key]:
            val = format_value(data1[key])
            lines.append(f"    {key}: {val}")
        else:
            val1 = format_value(data1[key])
            val2 = format_value(data2[key])
            lines.append(f"  - {key}: {val1}")
            lines.append(f"  + {key}: {val2}")
    
    # Format as single string
    return "{\n" + "\n".join(lines) + "\n}"
