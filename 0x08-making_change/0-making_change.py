#!/usr/bin/python3
"""
Coin Change Problem
Determines the fewest number of coins needed to meet a given total
"""


def makeChange(coins, total):
    """
    Determines the minimum number of coins to meet the total.

    Args:
        coins (list): A list of the values of coins in possession.
        total (int): The total amount.

    Returns:
        int: Fewest number of coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
