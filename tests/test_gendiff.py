import pytest
import os
import json
from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read_file(file_path):
    with open(file_path, 'r') as f:
        return f.read().strip()


@pytest.mark.parametrize("file1, file2, expected", [
    ('file1_flat.json', 'file2_flat.json', 'expected_flat.txt'),
    ('file1_recursive.json', 'file2_recursive.json',
     'expected_recursive.txt'),
    ('file1_recursive.yml', 'file2_recursive.yml',
     'expected_recursive.txt'),
])
def test_gendiff_default_format(file1, file2, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)

    result = generate_diff(file1_path, file2_path)
    expected_result = read_file(expected_path)

    assert result == expected_result


@pytest.mark.parametrize("file1, file2, format_name, expected", [
    ('file1_recursive.json', 'file2_recursive.json', 'plain',
     'expected_plain.txt'),
    ('file1_recursive.yml', 'file2_recursive.yml', 'plain',
     'expected_plain.txt'),
    ('file1_recursive.json', 'file2_recursive.json', 'json',
     'expected_json.txt'),
    ('file1_recursive.yml', 'file2_recursive.yml', 'json',
     'expected_json.txt'),
])
def test_gendiff_formats(file1, file2, format_name, expected):
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    expected_path = get_fixture_path(expected)

    result = generate_diff(file1_path, file2_path, format_name)
    expected_result = read_file(expected_path)

    assert result == expected_result


def test_json_format_validity():
    """Test that JSON output is valid JSON."""
    file1_path = get_fixture_path('file1_recursive.json')
    file2_path = get_fixture_path('file2_recursive.json')
    
    result = generate_diff(file1_path, file2_path, 'json')
    
    # Check that the result is valid JSON
    try:
        parsed = json.loads(result)
        assert isinstance(parsed, list)  
    except json.JSONDecodeError:
        pytest.fail("JSON output is not valid JSON")


