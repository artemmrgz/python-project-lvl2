from gendiff.parser import file_parser
import os


TESTS_DIR = 'tests'
FIXTURES = 'fixtures'


def locate(file):
    file_path = os.path.join(TESTS_DIR, FIXTURES, file)
    return file_path


def test_file_parser():
    output_from_json = file_parser(locate('file1.json'), locate('file2.json'))
    output_from_yml = file_parser(locate('file1.yml'), locate('file2.yaml'))
    with open(locate('file_parser_output.txt'), 'r') as file:
        output = file.read().strip()
        assert f'{output_from_json}' == output
        assert f'{output_from_yml}' == output
