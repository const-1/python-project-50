import argparse
import json

from gendiff import generate_diff
from gendiff.file_loader import load_file 


def main():
    """
    Main function that handles command-line interface for gendiff.
    Parses arguments, loads files, generates diff, and prints result.
    """
    # Initialize argument parser with custom settings
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.',
        add_help=False  # We'll add custom help option manually
    )

    # Add format option with default and help text
    parser.add_argument(
        '-f', '--format',
        help='set format of output (default: stylish)',
        default='stylish',
        metavar='FORMAT'
    )

    # Add required positional arguments for file paths
    parser.add_argument(
        'first_file',
        help='first configuration file (JSON)',
        metavar='FILE1'
    )
    parser.add_argument(
        'second_file',
        help='second configuration file (JSON)',
        metavar='FILE2'
    )
    
    # Add help option manually for better control
    parser.add_argument(
        '-h', '--help',
        action='help',
        default=argparse.SUPPRESS,
        help='show this help message and exit'
    )
    
    # Parse the arguments
    args = parser.parse_args()

    try:
        # Load and parse both configuration files
        data1 = load_file(args.first_file) 
        data2 = load_file(args.second_file)

        # Generate the difference between the two files
        diff = generate_diff(data1, data2, args.format)
        print(diff)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        exit(1)
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        exit(1)


if __name__ == '__main__':
    main()
