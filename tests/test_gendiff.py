import os
import json
from gendiff.gendiff import generate_diff, build_diff
from gendiff.parser import parse_file
from gendiff.formatters import stylish

TESTS_DIR = 'tests'
FIXTURES = 'fixtures'


def locate(file):
    file_path = os.path.join(TESTS_DIR, FIXTURES, file)
    return file_path


def diff_result(file_path1, file_path2, output_format):
    file1 = locate(file_path1)
    file2 = locate(file_path2)
    return generate_diff(file1, file2, output_format)


def test_generate_diff_json():
    with open(locate('expected_flat1.txt')) as file:
        output = file.read().strip()
    assert diff_result('file1.json', 'file2.json', stylish) == output


def test_generate_diff_yaml():
    with open(locate('expected_flat1.txt')) as file:
        output = file.read().strip()
    assert diff_result('file1.yml', 'file2.yaml', stylish) == output


def test_generate_nested_diff():
    with open(locate('expected_nested.txt')) as file:
        output = file.read().strip()
    assert diff_result('nested_file1.json','nested_file2.json', stylish) == output

    with open(locate('expected_nested.txt')) as file:
        output2 = file.read().strip()
    assert diff_result('nested_file1.yaml', 'nested_file2.yaml', stylish) == output2


def test_build_diff():
    old_dict = parse_file(locate('nested_file1.json'))
    new_dict = parse_file(locate('nested_file2.json'))
    with open(locate('build_diff.txt')) as f:
        output = f.read().strip()
    assert json.dumps(build_diff(old_dict, new_dict)) == output
