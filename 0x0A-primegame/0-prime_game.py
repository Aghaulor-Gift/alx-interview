#!/usr/bin/python3
"""A moddule that represent prime game"""


def sieve_of_eratosthenes(max_n):
    """Generates a list of prime counts for numbers from 0 to max_n"""
    sieve = [True] * (max_n + 1)
    sieve[0], sieve[1] = False, False  # 0 and 1 are not primes
    for i in range(2, int(max_n**0.5) + 1):
        if sieve[i]:
            for j in range(i * i, max_n + 1, i):
                sieve[j] = False
    return sieve


def isWinner(x, nums):
    """Determines who the winner of the game is after x rounds"""
    if x < 1 or not nums:
        return None

    max_n = max(nums)
    # Precompute prime numbers using sieve of Eratosthenes
    sieve = sieve_of_eratosthenes(max_n)

    # Track the number of wins for Maria and Ben
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(sieve[2:n+1])

        # If the number of primes is odd, Maria wins; if even, Ben wins
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
