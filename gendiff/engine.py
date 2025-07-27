# python-project-50/gendiff/scripts/gendiff.py

def generate_diff(data1, data2):
    """
    Generate a formatted diff between two dictionaries.
    
    Args:
        data1 (dict): First dictionary to compare
        data2 (dict): Second dictionary to compare
        
    Returns:
        str: Formatted diff string showing differences between dictionaries
    """
    # Get all unique keys from both dictionaries and sort alphabetically
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    lines = []  # Stores lines of the diff output
    
    for key in all_keys:
        # Key exists only in the first file
        if key not in data2:
            lines.append(f"  - {key}: {format_value(data1[key])}")
        
        # Key exists only in the second file
        elif key not in data1:
            lines.append(f"  + {key}: {format_value(data2[key])}")
        
        # Key exists in both files with same value
        elif data1[key] == data2[key]:
            lines.append(f"    {key}: {format_value(data1[key])}")
        
        # Key exists in both files but with different values
        else:
            lines.append(f"  - {key}: {format_value(data1[key])}")
            lines.append(f"  + {key}: {format_value(data2[key])}")
    
    # Combine all lines into a formatted diff string
    return "{\n" + "\n".join(lines) + "\n}"


def format_value(value):
    """
    Format values for consistent representation in diff output.
    
    Args:
        value: Value to format (any type)
        
    Returns:
        str: Formatted string representation of the value
    """
    # Convert booleans to lowercase strings (true/false)
    if isinstance(value, bool):
        return str(value).lower()
    
    # Convert None to 'null'
    elif value is None:
        return 'null'
    
    # For all other types, use standard string conversion
    return str(value)
