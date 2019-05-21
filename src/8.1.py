"""代码清单 8.1.py"""
import util


def my_func1(path):
    info = util.load_info(path)
    my_func2(info)

def my_func2(info):
	info = util.to_upper(info)
	my_func3(info)

def my_func3(info):
	util.print_info(info)


if __name__ == '__main__':
    my_func1('info.json')
