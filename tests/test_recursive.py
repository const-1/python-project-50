import pytest
import os
from gendiff import generate_diff


def get_fixture_path(filename):
    return os.path.join(os.path.dirname(__file__), 'fixtures', filename)


def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().strip()


@pytest.mark.parametrize("file1, file2, expected", [
    ('file1_recursive.json', 'file2_recursive.json', 'expected_recursive.txt'),
    ('file1_recursive.yml', 'file2_recursive.yml', 'expected_recursive.txt'),
])
def test_recursive_diff(file1, file2, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)
    
    expected_result = read_file(expected_path)
    assert generate_diff(file1_path, file2_path) == expected_result


