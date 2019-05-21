"""代码清单 5.2.py"""
import json
import util


def load_info(path):
    """读取json文件"""
    with open(path) as f:
        return json.load(f)


if __name__ == '__main__':
    info = load_info('info.json')
    util.print_info(None)
