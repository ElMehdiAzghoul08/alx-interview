#!/usr/bin/python3
"""Module"""
import sys


def print_stats(total_size, status_codes):
    """print_stats function"""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")


def main():
    """main function"""
    total_size = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0,
                    404: 0, 405: 0, 500: 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                parts = line.split()
                size = int(parts[-1])
                status = int(parts[-2])

                total_size += size
                if status in status_codes:
                    status_codes[status] += 1

                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)

            except (ValueError, IndexError):
                pass

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
