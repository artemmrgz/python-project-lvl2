import json


def to_json(diff):
    '''Convert diff to json.

    Args:
        diff (dict): Defference output

    Returns:
        Json result
    '''
    return json.dumps(diff, indent=2)
