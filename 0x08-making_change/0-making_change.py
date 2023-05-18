#!/usr/bin/python3
""" Change comes from within
"""


def makeChange(coins, total):
    """ Returns fewest number of coins needed to meet total
    """
    n_of_coins = 0
    if total <= 0:
        return n_of_coins
    coins.sort(reverse=True)
    while (total > 0 and coins):
        n = int(total / coins[0])
        total = total - (coins[0] * n)
        n_of_coins = n_of_coins + n
        coins.remove(coins[0])
    if total != 0:
        return -1
    return n_of_coins