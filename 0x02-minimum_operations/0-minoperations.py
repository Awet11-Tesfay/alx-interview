#!/usr/bin/env python3
''' Description: In a ext file there is a single cahracter H your text
                 editor can execue only two operations in this file copy all
                 and paste given a number n write a method that calculates the
                 fewest number of operations needed to result in exactly n H
                 characters in the file
'''


def minOperations(n):
    if n < 2 or type(n) is not int:
        return 0

    a = 0
    x = 2
    while (x <= n):
        if not (n % x):
            n = int(n / x)
            a += x
            x = 1
    return a