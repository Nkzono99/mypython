import subprocess
from pathlib import Path
import sys


def parse_args():
    if len(sys.argv) < 2:
        print('filename is required')
        exit(1)

    print(sys.argv)

    return sys.argv


def search_pyfile(filename, directory='.mypython', depth=10):
    curdir = Path(Path('.').resolve())
    for i in range(depth):
        filepath = curdir / directory / filename
        if filepath.exists():
            return filepath
        curdir = curdir.parent
    return None


def python(filepath, params):
    command = 'python {} {}'.format(filepath.resolve(), ' '.join(params))
    print(command)

    res = subprocess.Popen(
        ['python', filepath] + params,
        stdout=subprocess.PIPE)
    return [line.decode('utf-8') for line in res.stdout.readlines()]


def main():
    args = parse_args()
    filepath = search_pyfile(args[1])

    if filepath is None:
        print('{} not found'.format(args[1]))
        return

    print(''.join(python(filepath, args[2:])))


if __name__ == '__main__':
    main()
