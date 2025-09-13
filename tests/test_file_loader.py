import pytest
import os
from gendiff.file_loader import load_file

def test_load_json_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    recursive_path = os.path.join(current_dir, 'fixtures', 'file1_recursive.json')
    if os.path.exists(recursive_path):
        data, format_type = load_file(recursive_path)
        assert format_type == 'json'
        assert 'common' in data  
    
    flat_path = os.path.join(current_dir, 'fixtures', 'file1_flat.json')
    if os.path.exists(flat_path):
        data, format_type = load_file(flat_path)
        assert format_type == 'json'
        assert 'host' in data  

def test_load_yaml_file():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    recursive_path = os.path.join(current_dir, 'fixtures', 'file1_recursive.yml')
    if os.path.exists(recursive_path):
        data, format_type = load_file(recursive_path)
        assert format_type == 'yaml'
        assert 'common' in data  
    
    flat_path = os.path.join(current_dir, 'fixtures', 'file1_flat.yml')
    if os.path.exists(flat_path):
        data, format_type = load_file(flat_path)
        assert format_type == 'yaml'
        assert 'host' in data  

def test_load_file_with_unknown_format():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    test_file = os.path.join(current_dir, 'fixtures', 'test_file.unknown')
    with open(test_file, 'w') as f:
        f.write("some content")
    
    try:
        with pytest.raises(ValueError):
            load_file(test_file)
    finally:
        if os.path.exists(test_file):
            os.remove(test_file)
