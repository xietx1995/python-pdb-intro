"""代码清单 util.py"""
import json


def load_info(path):
    """读取json文件"""
    with open(path) as f:
        return json.load(f)


def print_info(info):
    """打印信息"""
    for k, v in info.items():
        print('{}: {}'.format(k, v))


def to_upper(info):
    for k, v in info.items():
        if isinstance(v, str):
            info[k] = v.upper()
    return info