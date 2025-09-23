import argparse
from gendiff import generate_diff


def main():
    """Command line interface for gendiff"""
    parser = argparse.ArgumentParser(
        description='Generate diff between two configuration files',
        prog='gendiff'
    )
    parser.add_argument(
            'file1', help='First configuration file (JSON or YAML)'
            )
    parser.add_argument(
            'file2', help='Second configuration file (JSON or YAML)'
            )
    parser.add_argument('-f', '--format',
                        help='Output format (default: "stylish")',
                        default='stylish',
                        choices=['stylish', 'plain', 'json'])  

    args = parser.parse_args()

    try:
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


