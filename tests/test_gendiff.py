import os
import pytest
from gendiff.scripts.gendiff import generate_diff

def get_fixture_path(filename):
    """Return absolute path to fixture file"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', filename)

def read_fixture(filename):
    """Read fixture file and return its content"""
    path = get_fixture_path(filename)
    with open(path, 'r') as f:
        return f.read()

@pytest.mark.parametrize("file1, file2, expected", [
    ('file1.json', 'file2.json', 'expected.txt'),
])
def test_generate_diff(file1, file2, expected):
    """Test generate_diff function with flat JSON files"""
    # Get paths to fixture files
    file1_path = get_fixture_path(file1)
    file2_path = get_fixture_path(file2)
    
    # Get expected result
    expected_result = read_fixture(expected)
    
    # Generate actual result
    result = generate_diff(file1_path, file2_path)
    
    # Normalize line endings (for Windows/Linux compatibility)
    expected_normalized = expected_result.replace('\r\n', '\n').replace('\r', '\n').strip()
    result_normalized = result.replace('\r\n', '\n').replace('\r', '\n').strip()
    
    # Compare results
    assert result_normalized == expected_normalized, (
        f"Expected:\n{expected_normalized}\n\nActual:\n{result_normalized}"
    )

def test_generate_diff_with_invalid_path():
    """Test generate_diff with non-existing files"""
    with pytest.raises(FileNotFoundError):
        generate_diff('non_existent1.json', 'non_existent2.json')
