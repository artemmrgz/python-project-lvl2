#!/usr/bin/env python3
from gendiff.gendiff import generate_diff
from gendiff.parser import cli_parser

def main():
    first_file, second_file = cli_parser()
    result = generate_diff(first_file, second_file)
    print(result)


if __name__ == '__main__':
    main()
