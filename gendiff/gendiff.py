from gendiff.parser import parse_file
from gendiff.constants import ADDED, CHANGED, REMOVED, NESTED, UNCHANGED


def build_diff(old, new):
    keys = set(old) | set(new)
    difference = {}
    for key in keys:
        old_value = old.get(key)
        new_value = new.get(key)
        children = isinstance(old_value, dict) and isinstance(new_value, dict)
        if children:
            difference[key] = (NESTED, build_diff(old_value, new_value))
        elif key in old and key in new:
            if old_value == new_value:
                difference[key] = (UNCHANGED, new_value)
            else:
                difference[key] = (CHANGED, old_value, new_value)
        elif key in old and key not in new:
            difference[key] = (REMOVED, old_value)
        else:
            difference[key] = (ADDED, new_value)
    return difference


def generate_diff(old, new, output_format):
    diff = build_diff(parse_file(old), parse_file(new))
    return output_format(diff)
