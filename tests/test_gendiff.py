import os
import json
from gendiff.gendiff import generate_diff, build_diff
from gendiff.parser import parse_file
from gendiff.format import stylish, plain


def locate(file):
    return os.path.join('tests', 'fixtures', file)


def diff_result(output_format):
    return generate_diff(
        locate('file_before.json'),
        locate('file_after.json'),
        output_format
    )


def test_generate_diff():
    with open(locate('expected_nested.txt')) as f:
        expected = f.read().strip()
    assert diff_result(stylish) == expected


    with open(locate('expected_plain.txt')) as f:
        expected = f.read().strip()
    assert diff_result(plain) == expected


def test_build_diff():
    old_dict = parse_file(locate('file_before.json'))
    new_dict = parse_file(locate('file_after.json'))
    with open(locate('build_diff.txt')) as f:
        expected = f.read().strip()
    assert json.dumps(build_diff(old_dict, new_dict)) == expected
