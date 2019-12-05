"""
split and interactively page a string or file of text
"""


def more(text: str, num_lines=15):
    lines = text.splitlines()

    while lines:
        chunk = lines[:num_lines]
        lines = lines[num_lines:]

        for line in chunk:
            print(line)

        if lines and input('More?') not in ['y', 'Y']:
            break


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        more(sys.stdin.read())
    else:
        more(open(sys.argv[1]).read())
