from gendiff.file_loader import load_file
from gendiff.ast_builder import build_diff  # Добавьте эту строку
from gendiff.formatters.stylish import format_stylish

def generate_diff(file_path1, file_path2, format_name='stylish'):
    """Generate diff between two files."""
    data1, _ = load_file(file_path1)
    data2, _ = load_file(file_path2)
    diff = build_diff(data1, data2)  # Теперь эта функция будет определена
    
    if format_name == 'stylish':
        return format_stylish(diff)
    return format_stylish(diff)
