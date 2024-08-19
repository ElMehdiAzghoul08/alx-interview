#!/usr/bin/python3
"""Module"""
import sys


def print_stats(status_codes, total_size):
    """print_stats function"""
    print("File size: {}".format(total_size))
    for key, val in sorted(status_codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_size = 0
code = 0
count = 0
status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0}


try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            count += 1

            if count <= 10:
                total_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in status_codes.keys()):
                    status_codes[code] += 1

            if (count == 10):
                print_stats(status_codes, total_size)
                count = 0

finally:
    print_stats(status_codes, total_size)
