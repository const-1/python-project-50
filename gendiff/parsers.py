import json
from pathlib import Path

def parse_file(file_path):
    """Parse JSON or YAML files using safe methods"""
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(path, 'r') as f:
        # Process JSON files
        if path.suffix == '.json':
            return json.load(f)
        
        # Process YAML/YML files using our custom parser
        elif path.suffix in ('.yaml', '.yml'):
            return parse_simple_yaml(f)
        else:
            raise ValueError(f"Unsupported file format: {path.suffix}")

def parse_simple_yaml(file):
    """Parse simple YAML files without external dependencies
    
    This parser handles only flat key-value structures without:
    - Nested objects
    - Arrays/lists
    - Complex YAML features
    
    It's suitable for simple configuration files with primitive values.
    """
    result = {}
    for line in file:
        # Skip comments and empty lines
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        
        # Skip lines without colon separator
        if ':' not in line:
            continue
            
        # Split into key and value (only at first colon)
        key, value = line.split(':', 1)
        key = key.strip()
        value = value.strip()
        
        # Convert value to appropriate data type
        # Handle quoted strings
        if (value.startswith('"') and value.endswith('"')) or \
           (value.startswith("'") and value.endswith("'")):
            value = value[1:-1]
        
        # Handle boolean values
        elif value.lower() == 'true':
            value = True
        elif value.lower() == 'false':
            value = False
        
        # Handle null values
        elif value.lower() == 'null' or value.lower() == '~':
            value = None
        
        # Handle integers
        elif value.isdigit():
            value = int(value)
        
        # Handle floats
        elif value.replace('.', '', 1).isdigit() and value.count('.') == 1:
            value = float(value)
        
        # Add to result dictionary
        result[key] = value
    
    return result
