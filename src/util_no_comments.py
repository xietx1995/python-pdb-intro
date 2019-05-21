import json


def load_info(path):
    with open(path) as f:
        return json.load(f)


def print_info(info):
    for k, v in info.items():
        print('{}: {}'.format(k, v))


def to_upper(info):
    for k, v in info.items():
        if isinstance(v, str):
            info[k] = v.upper()
    return info
