#!/usr/bin/python3
""" write a script that reads stdin line by line and computes metrics """

import sys


if __name__ == "__main__":
    code = {"200": 0,
            "301": 0,
            "400": 0,
            "401": 0,
            "403": 0,
            "404": 0,
            "405": 0,
            "500": 0}
    count = 1
    file_size = 0

    def parse(line):
        """ read line """
        try:
            parsed = line.split()
            stat_code = parse[-2]
            if stat_code in code.keys():
                code[stat_code] += 1
            return int(parse[-1])
        except Exception:
            return 0

    def print():
        """ prints status in ascending order """
        print("File size: {}".format(file_size))
        for key in sorted(code.keys):
            if code[key]:
                print("{}: {}".format(key, code[key]))

    try:
        for line in sys.stdin:
            file_size += parse(line)
            if count % 10 == 0:
                print()
            count += 1
    except KeyboardInterrupt:
        print()
        raise
    print()
