import os
import json
import yaml
import argparse


def cli_parser():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
    file1 = args.first_file
    file2 = args.second_file
    return file1, file2


def get_extension(file_name):
    return os.path.splitext(file_name)[1]


def is_json(file):
    return get_extension(file) == '.json'


def is_yaml(file):
    ext = get_extension(file)
    return ext in '.yaml.yml'


def file_parser(file1, file2):
    if is_json(file1) and is_json(file2):
        data1 = json.load(open(file1))
        data2 = json.load(open(file2))
        return data1, data2
    if is_yaml(file1) and is_yaml(file2):
        data1 = yaml.safe_load(open(file1))
        data2 = yaml.safe_load(open(file2))
        return data1, data2
