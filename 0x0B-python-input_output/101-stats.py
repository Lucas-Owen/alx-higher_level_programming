#!/usr/bin/python3
"""A script that reads input from stdin and computes metrics

Input is expected to be of the form
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""


class InputParser():
    """Class to parse the input"""
    def __init__(self):
        """Initializes the instance"""
        self.total_size = 0
        self.status_codes = {
            '200': 0,
            '301': 0,
            '400': 0,
            '401': 0,
            '403': 0,
            '404': 0,
            '405': 0,
            '500': 0
            }

    def parse_input(self, line):
        """Parse input from stdin"""
        line = line.strip()
        tokens = line.split(' ')
        try:
            size = int(tokens[-1])
            self.total_size += size
        except Exception:
            pass
        status_code = tokens[-2]
        if status_code in self.status_codes:
            self.status_codes[status_code] += 1

    def __repr__(self):
        """To print current stats in the desired format"""
        items = sorted(self.status_codes.items())
        codes = [f'{code}: {num}\n' for (code, num) in items if num != 0]
        return f'File size: {self.total_size}\n' + ''.join(codes)


if __name__ == '__main__':
    import sys
    parser = InputParser()
    num_lines = 0
    try:
        for line in sys.stdin:
            parser.parse_input(line)
            num_lines += 1
            if num_lines == 10:
                print(parser, end="")
                num_lines = 0
        print(parser, end="")
    except KeyboardInterrupt:
        print(parser, end="")
        raise
