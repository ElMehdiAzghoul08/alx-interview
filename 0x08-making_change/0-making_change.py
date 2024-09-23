#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """Calculate minimum coins."""
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        while total >= coin:
            total -= coin
            count += 1

        if total == 0:
            return count

    return -1
