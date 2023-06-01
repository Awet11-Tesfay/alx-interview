#!/usr/bin/python3
""" Prime Game
"""


def prime_game(n):
    """ List of the Prime numbers
    """
    game = []
    game_b = [True] * (n + 1)
    for m in range(2, n + 1):
        if (game_b[m]):
            game.append(m)
            for z in range(m, n + 1, m):
                game_b[z] = False
    return game


def isWinner(x, nums):
    """ Determine who the winner of each game is
    """
    if x is None or nums is None or x == 0 or nums == []:
        return None
    Maria = Ben = 0
    for a in range(x):
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
