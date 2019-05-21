"""代码清单 6.1.py"""

names = ['Peter', 'John', 'Bob', 'Cindy']


def print_and_count_names(names):
	count = 0
	for name in names:
		print(name)
		count += 1
	return count


if __name__ == '__main__':
    print_and_count_names(names)
