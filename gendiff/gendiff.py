from gendiff.constants import ADDED, CHANGED, REMOVED, NESTED, UNCHANGED


def build_diff(old, new):
    '''Build difference report

    Args:
        old (dict): dataset before changing
        new (dict): dataset after changing

    Returns:
        difference (dict)
    '''
    difference = {}
    removed_keys = old.keys() - new.keys()
    difference.update(
        {
            key: (REMOVED, old.get(key))
            for key in sorted(removed_keys)
        }
    )
    added_keys = new.keys() - old.keys()
    difference.update(
        {
            key: (ADDED, new.get(key))
            for key in sorted(added_keys)
        }
    )
    for key in sorted(old.keys() & new.keys()):
        old_value = old.get(key)
        new_value = new.get(key)
        has_children = (
            isinstance(old_value, dict)
        ) and (
            isinstance(new_value, dict)
        )
        if has_children:
            difference[key] = (NESTED, build_diff(old_value, new_value))
        elif old_value == new_value:
            difference[key] = (UNCHANGED, new_value)
        else:
            difference[key] = (CHANGED, old_value, new_value)
    return difference


def generate_diff(old, new, output_format):
    '''Find differences in files

    Args:
        old (dict): dictionary from first file
        new (dict): dictionary from second file
        output_format: format.plain(), format.nested(), format.json()

    Returns:
        str: difference string
    '''
    diff = build_diff(old, new)
    return output_format(diff)
