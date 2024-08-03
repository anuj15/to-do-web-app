import os

FILE_PATH = 'todos.txt'

if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, 'w') as f:
        pass


def read_file(filename=FILE_PATH):
    with open(filename) as f:
        return f.readlines()


def write_file(text, filename=FILE_PATH):
    with open(filename, 'w') as f:
        f.writelines(text)


if __name__ == '__main__':
    data = read_file()
    print(data)
