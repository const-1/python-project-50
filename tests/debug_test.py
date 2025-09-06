import os
from gendiff import generate_diff

# Получаем абсолютные пути к файлам
current_dir = os.path.dirname(os.path.abspath(__file__))
file1_path = os.path.join(current_dir, 'fixtures', 'file1_recursive.json')
file2_path = os.path.join(current_dir, 'fixtures', 'file2_recursive.json')
expected_path = os.path.join(current_dir, 'fixtures', 'expected_recursive.txt')

# Генерируем diff
result = generate_diff(file1_path, file2_path)

# Выводим результат
print("ACTUAL RESULT:")
print(result)
print("\n" + "="*50 + "\n")

# Читаем ожидаемый результат
with open(expected_path, 'r') as f:
    expected = f.read()

print("EXPECTED RESULT:")
print(expected)

# Сравниваем построчно
print("\n" + "="*50 + "\n")
print("LINE BY LINE COMPARISON:")
actual_lines = result.split('\n')
expected_lines = expected.split('\n')

min_len = min(len(actual_lines), len(expected_lines))
for i in range(min_len):
    actual = actual_lines[i]
    expected_line = expected_lines[i]
    if actual != expected_line:
        print(f"Line {i}: DIFFERENCE")
        print(f"  Actual:   '{actual}'")
        print(f"  Expected: '{expected_line}'")
    else:
        print(f"Line {i}: MATCH")

# Если строк разное количество
if len(actual_lines) != len(expected_lines):
    print(f"\nDifferent number of lines: actual={len(actual_lines)}, expected={len(expected_lines)}")
    if len(actual_lines) > len(expected_lines):
        print("Extra lines in actual:")
        for i in range(min_len, len(actual_lines)):
            print(f"  Line {i}: '{actual_lines[i]}'")
    else:
        print("Missing lines in actual:")
        for i in range(min_len, len(expected_lines)):
            print(f"  Line {i}: '{expected_lines[i]}'")
