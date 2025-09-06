#!/usr/bin/env python3
import argparse
from gendiff import generate_diff

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
                        choices=['stylish'])  # Adding other formats as implemented
    
    # Parse arguments
    args = parser.parse_args()
    
    try:
        # Generate and print diff with format option
        diff = generate_diff(args.file1, args.file2, args.format)
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
