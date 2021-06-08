from gendiff.constants import (
    ADDED,
    CHANGED,
    REMOVED,
    NESTED,
    UNCHANGED,
    DEFAULT_INDENT,
    FLAG_INDENT
)

flags = {
    ADDED: '+',
    REMOVED: '-',
    UNCHANGED: ' '
}


def to_stylish(difference, level=0):  # noqa: C901
    indent = level * DEFAULT_INDENT * ' '
    diff = []
    for key, value in sorted(difference.items()):
        if isinstance(value, tuple):
            flag, rest = value[0], value[1:]
            if flag == UNCHANGED or flag == NESTED:
                diff.append(content_to_str(UNCHANGED, key, rest[0], level + 1))
            if flag == CHANGED:
                diff.append(content_to_str(REMOVED, key, rest[0], level + 1))
                diff.append(content_to_str(ADDED, key, rest[1], level + 1))
            if flag == REMOVED:
                diff.append(content_to_str(REMOVED, key, rest[0], level + 1))
            if flag == ADDED:
                diff.append(content_to_str(ADDED, key, rest[0], level + 1))
        else:
            diff.append(content_to_str(UNCHANGED, key, value, level + 1))
    return '{\n' + '\n'.join(diff) + '\n' + indent + '}'


def content_to_str(flag, key, value, level):
    indent = (level * DEFAULT_INDENT - FLAG_INDENT) * ' '
    if isinstance(value, dict):
        result = to_stylish(value, level)
        return f'{indent}{flags[flag]} {key}: {result}'
    return f'{indent}{flags[flag]} {key}: {value}'
