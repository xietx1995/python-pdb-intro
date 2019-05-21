"""代码清单 3.1.py"""
import json


def load_info(path):
    """读取json文件"""
    with open(path) as f:
        return json.load(f)
        

def print_info(info):
    """打印信息"""
    for k, v in info.items():
        print('{}: {}'.format(k, v))


if __name__ == '__main__':
    info = load_info('info.json')
    print_info(info)
