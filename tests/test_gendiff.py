import os
from gendiff.gendiff import generate_diff

TESTS_DIR = 'tests'
FIXTURES = 'fixtures'

def locate(file):
    file_path = os.path.join(TESTS_DIR, FIXTURES, file)
    return file_path


def test_generate_diff_json():
    with open(locate('expected.txt'), 'r') as file:
        output = file.read().strip()
        assert generate_diff(locate('file1.json'), locate('file2.json')) == output
    with open(locate('expected2.txt'), 'r') as file2:
        output2 = file2.read().strip()
        assert generate_diff(locate('file3.json'), locate('empty.json')) == output2


def test_generate_diff_yaml():
    with open(locate('expected.txt'), 'r') as file:
        output = file.read().strip()
        assert generate_diff(locate('file1.yml'), locate('file2.yaml')) == output
    with open(locate('expected2.txt'), 'r') as file2:
        output2 = file2.read().strip()
        assert generate_diff(locate('file3.yaml'), locate('empty.yml')) == output2

