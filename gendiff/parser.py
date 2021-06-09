import os
import json
import yaml
import argparse
from gendiff import format


def formatter(string_format='stylish'):
    '''Gets CLI parser's format.

    Args:
        string_format: Formatting option

    Returns:
        Function of parse
    '''
    formats = {
        'stylish': format.stylish,
        'plain': format.plain,
        'json': format.json
    }
    return formats[string_format]


def cli_parser():
    '''Parse arguments.

    Returns:
        option: Inspect the command line, convert each argument
                to the appropriate type
    '''
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', default='stylish', type=formatter,
                        help='set format of output (default: stylish)')
    return parser.parse_args()


def parse_file(file_path):
    '''Takes content of file.

    Args:
        file_path: Path to file

    Returns:
        Parsed data
    '''
    formats = {
        '.json': json.loads,
        '.yaml': yaml.safe_load,
        '.yml': yaml.safe_load
    }
    file_format = os.path.splitext(file_path)[1]
    with open(os.path.abspath(file_path)) as f:
        return formats[file_format](f.read())
