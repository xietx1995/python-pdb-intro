"""代码清单 7.1.py"""

names = ['Peter', 'John', 'Bob', 'Cindy']


def print_and_count_names(names):
	count = 0
	for name in names:
		count += 1
		print(name)
	return count


if __name__ == '__main__':
    print_and_count_names(names)
