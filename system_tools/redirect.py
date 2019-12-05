import sys


class Output:
    def __init__(self):
        self.text = ''

    def write(self, string: str):
        self.text += string

    def writelines(self, lines):
        for line in lines:
            self.write(line)


class Input:
    def __init__(self, input=''):
        self.text = input

    def read(self, size=None):
        if size:
            res, self.text = self.text[:size], self.text[size:]
        else:
            res, self.text = self.text, ''

        return res

    def readline(self):
        eoln = self.text.find('\n')
        if eoln:
            res, self.text = self.text[:eoln + 1], self.text[eoln + 1:]
        else:
            res, self.text = self.text, ''

        return res


def redirect(function, args, kwargs, input):
    savestreams = sys.stdin, sys.stdout
    sys.stdin = Input(input)
    sys.stdout = Output()

    try:
        result = function(*args, **kwargs)
        output = sys.stdout.text
    finally:
        sys.stdin, sys.stdout = savestreams

    return result, output
