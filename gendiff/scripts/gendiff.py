#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.parser import cli_parser, parse_file


def main():
    '''Run CLI'''
    namespace = cli_parser()
    result = generate_diff(parse_file(namespace.first_file),
                           parse_file(namespace.second_file),
                           namespace.format)
    print(result)


if __name__ == '__main__':
    main()
