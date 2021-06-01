import json
import argparse


def generate_diff(json1=None, json2=None):
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')

    if not json1 and not json2:
        args = parser.parse_args()
        json1 = args.first_file
        json2 = args.second_file
    file1 = json.load(open(json1))
    file2 = json.load(open(json2))
    keys = set(file1) | set(file2)
    diff = {}
    for key in sorted(keys):
        if key in file1 and key in file2:
            if file1.get(key) != file2.get(key):
                diff[f'- {key}'] = file1.get(key)
                diff[f'+ {key}'] = file2.get(key)
            else:
                diff[f'  {key}'] = file1.get(key)
        elif key in file1 and key not in file2:
            diff[f'- {key}'] = file1.get(key)
        else:
            diff[f'+ {key}'] = file2.get(key)
    result = dict_to_str(diff)
    return result


def dict_to_str(di):
    dict_as_str = ''
    for key, value in di.items():
        dict_as_str = '{0}  {1}: {2}\n'.format(dict_as_str, key, value)
    return '{{\n{0}}}'.format(dict_as_str)
