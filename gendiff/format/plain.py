from gendiff.constants import (
    ADDED,
    CHANGED,
    REMOVED,
    NESTED,
    UNCHANGED
)


def to_plain(difference, key_path=None):
    '''Render difference to plain

    Args:
        difference (dict): difference input
        path_of_keys (list): path to value

    Returns:
        String result
    '''
    diff = []

    if not key_path:
        key_path = []

    for key, value in sorted(difference.items()):
        flag, rest = value[0], value[1:]
        if flag == UNCHANGED:
            continue
        string_diff(key, flag, rest, diff, key_path)
    return '\n'.join(diff)


def add_added_node(key, value, diff, key_path):
    key_path.append(key)
    diff.append(
        'Property \'{0}\' was added with value: {1}'.format(
            '.'.join(key_path), render_value(value[0])
        )
    )
    key_path.pop()


def add_removed_node(key, key_path, diff):
    key_path.append(key)
    diff.append(
        'Property \'{}\' was removed'.format(
            '.'.join(key_path)
        )
    )
    key_path.pop()


def add_changed_node(key, value, diff, key_path):
    key_path.append(key)
    diff.append(
        'Property \'{0}\' was updated. From {1} to {2}'.format(
            '.'.join(key_path), render_value(value[0]),
            render_value(value[1])
        )
    )
    key_path.pop()


def add_nested_node(key, value, diff, key_path):
    key_path.append(key)
    diff.append(to_plain(value[0], key_path))
    key_path.pop()


def string_diff(key, flag, rest, diff, key_path):
    flags = {
        ADDED: add_added_node,
        REMOVED: add_removed_node,
        CHANGED: add_changed_node,
        NESTED: add_nested_node,
    }

    if flag == REMOVED:
        flags[flag](key, key_path, diff)
    else:
        flags[flag](key, rest, diff, key_path)


def render_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    else:
        return f'\'{value}\''
