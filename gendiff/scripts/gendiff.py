#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.parser import cli_parser


def main():
    namespace = cli_parser()
    result = generate_diff(namespace.first_file,
                           namespace.second_file,
                           namespace.format)
    print(result)


if __name__ == '__main__':
    main()
