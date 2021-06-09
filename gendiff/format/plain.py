from gendiff.constants import (
    ADDED,
    CHANGED,
    REMOVED,
    NESTED,
    UNCHANGED
)


def to_plain(difference, path_of_keys=None):
    '''Render difference to plain

    Args:
        difference (dict): difference input
        path_of_keys (list): path to value

    Returns:
        String result
    '''
    diff = []

    if path_of_keys is None:
        path_of_keys = []

    for key, value in sorted(difference.items()):
        flag, rest = value[0], value[1:]
        if flag == UNCHANGED:
            continue
        string_diff(key, flag, rest, diff, path_of_keys)

    return '\n'.join(diff)


def add_added_node(key, value, diff, path_of_keys):
    path_of_keys.append(key)
    diff.append(
        'Property {0} was added with value: {1}'.format(
            '.'.join(path_of_keys), show_value(value[0])
        )
    )


def add_removed_node(key, path_of_keys, diff):
    path_of_keys.append(key)
    diff.append(
        'Property {} was removed'.format(
            '.'.join(path_of_keys)
        )
    )


def add_changed_node(key, value, diff, path_of_keys):
    path_of_keys.append(key)
    diff.append(
        'Property {0} was updated. From {1} to {2}'.format(
            '.'.join(path_of_keys), show_value(value[0]),
            show_value(value[1])
        )
    )


def add_nested_node(key, value, diff, path_of_keys):
    path_of_keys.append(key)
    diff.append(to_plain(value[0], path_of_keys))


def string_diff(key, flag, rest, diff, path_of_keys):
    flags = {
        ADDED: add_added_node,
        REMOVED: add_removed_node,
        CHANGED: add_changed_node,
        NESTED: add_nested_node,
    }

    if flag == REMOVED:
        flags[flag](key, path_of_keys, diff)
    else:
        flags[flag](key, rest, diff, path_of_keys)


def show_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    else:
        return f'\'{value}\''
