from gendiff.parser import parse_file
import os


def locate(file):
    return os.path.join('tests', 'fixtures', file)


def test_file_parser():
    output = parse_file(locate('file1.yml')), parse_file(locate('file2.yaml'))
    with open(locate('file_parser_output.txt')) as f:
        expected = f.read().strip()
        assert f'{output}' == expected
