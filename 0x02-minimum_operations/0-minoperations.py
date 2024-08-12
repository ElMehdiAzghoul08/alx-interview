#!/usr/bin/python3
"""Module"""


def minOperations(n):
    "minOperations function"
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

        if divisor * divisor > n:
            if n > 1:
                operations += n
            break

    return operations
