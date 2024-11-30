#!/usr/bin/python3
"""
Contains a function to determine the fewest
number of coins needed to meet a given amount total.
"""

from collections import deque


def makeChange(coins, total):
    """
    Returns: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have, return -1
    """
    if total <= 0:
        return 0
    if not coins:
        return -1

    # Use a queue to perform BFS
    queue = deque([(0, 0)])  # (current amount, number of coins)
    visited = set()

    while queue:
        current_amount, num_coins = queue.popleft()

        for coin in coins:
            next_amount = current_amount + coin

            if next_amount == total:
                return num_coins + 1
            if next_amount < total and next_amount not in visited:
                visited.add(next_amount)
                queue.append((next_amount, num_coins + 1))

    return -1
