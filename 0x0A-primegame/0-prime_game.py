#!/usr/bin/python3
"""Prime game module"""


def isWinner(x, nums):
    """Determine winner"""
    if not nums or x < 1:
        return None
    max_num = max(nums)

    sieve = [True] * (max_num + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(max_num**0.5) + 1):
        if sieve[i]:
            for j in range(i*i, max_num + 1, i):
                sieve[j] = False

    prime_counts = [0] * (max_num + 1)
    for i in range(2, max_num + 1):
        prime_counts[i] = prime_counts[i-1] + (1 if sieve[i] else 0)

    maria_wins = 0
    for n in nums:
        if prime_counts[n] % 2 == 1:
            maria_wins += 1

    if maria_wins * 2 > x:
        return "Maria"
    elif maria_wins * 2 < x:
        return "Ben"
    else:
        return None
