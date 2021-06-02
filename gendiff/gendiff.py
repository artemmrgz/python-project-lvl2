import os
import argparse
from gendiff.parser import file_parser


def generate_diff(file1, file2):
    data1, data2 = file_parser(file1, file2)
    keys = set(data1) | set(data2)
    diff = {}
    for key in sorted(keys):
        if key in data1 and key in data2:
            if data1.get(key) == data2.get(key):
                diff[f'  {key}'] = data1.get(key)
            else:
                diff[f'- {key}'] = data1.get(key)
                diff[f'+ {key}'] = data2.get(key)
        elif key in data1 and key not in data2:
            diff[f'- {key}'] = data1.get(key)
        else:
            diff[f'+ {key}'] = data2.get(key)
    result = dict_to_str(diff)
    return result


def dict_to_str(di):
    dict_as_str = ''
    for key, value in di.items():
        dict_as_str = '{0}  {1}: {2}\n'.format(dict_as_str, key, value)
    return '{{\n{0}}}'.format(dict_as_str)
