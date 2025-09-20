import pytest
from gendiff.parsers import parse  


def test_parse_json():
    json_content = '{"key": "value"}'
    result = parse(json_content, 'json')  
    assert result == {"key": "value"}


def test_parse_yaml():
    yaml_content = "key: value"
    result = parse(yaml_content, 'yaml')  
    assert result == {"key": "value"}


def test_parse_unknown_format():
    unknown_content = "some content"
    with pytest.raises(ValueError):
        parse(unknown_content, 'unknown')


