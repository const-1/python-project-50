import argparse
from pathlib import Path
from gendiff.parsers import parse_file

def format_value(value):
    """Convert Python values to string representation for diff output"""
    if value is None:
        return 'null'
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, (int, float)):
        return str(value)
    return value

def generate_diff(data1, data2):
    """
    Generate a formatted diff between two data sources (dicts or file paths)
    """
    # Process first input
    if isinstance(data1, (str, Path)):
        data1 = parse_file(data1)
    
    # Process second input
    if isinstance(data2, (str, Path)):
        data2 = parse_file(data2)    

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

def main():
    """Command line interface for gendiff"""
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Generate diff between two configuration files',
        prog='gendiff'
    )
    parser.add_argument('file1', help='First configuration file (JSON or YAML)')
    parser.add_argument('file2', help='Second configuration file (JSON or YAML)')
    parser.add_argument('-f', '--format', 
                        help='Output format (default: "stylish")', 
                        default='stylish',
                        choices=['stylish'])
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Generate and print diff
        diff = generate_diff(args.file1, args.file2)
        print(diff)
    except FileNotFoundError as e:
        print(f"Error: {str(e)}")
        exit(1)
    except ValueError as e:
        print(f"Error: {str(e)}")
        exit(1)
    except TypeError as e:
        print(f"Error: {str(e)}")
        exit(1)

if __name__ == '__main__':
    main()
