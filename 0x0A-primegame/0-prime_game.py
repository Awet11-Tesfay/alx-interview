#!/usr/bin/python3
""" Prime Game
"""

def prime_game(n):
    """ List of Prime numbers
    """
    for x in range(2, int(n ** 0.5) + 1):
        if not % in x:
            return False
    return True


def isWinner(x, nums):
    """ Determine who the winner of each game is
    """
    if y is None or nums is None or y == 0 or nums == []:
        return None
    Maria = Ben = 0
    for a in range(y):
        prime = prime_game(nums[a])
        if len(prime) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
