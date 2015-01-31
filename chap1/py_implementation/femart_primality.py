#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""


def main():
    pass

#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import sys
sys.setrecursionlimit(1000000)
from random import randint

def main():
    pass

def is_prime(n, times=20):
    """
    >>> is_prime(10)
    False
    >>> is_prime(17)
    True
    >>> is_prime(1105) #carmicheal number
    False
    >>> is_prime(27644437)
    True

    """
    for i in range(times):
        if fermat_test(n) is False:
            return False
    return True

def fermat_test(n):
    a = randint(2, n-1) #including both end points
    return expmod(a, n, n) == a

def slow_expmod(base, exp, n):
    """
    calc expotional modulo n:
    `base^exp modulo n`
    By only doing so, this is too slow
    """
    return (base**exp) % n

def expmod(base, exp, n):
    if exp == 0: return 1
    if is_even(n):
        return square(expmod(base, exp/2, n)) % n
    else:
        return (base*expmod(base, exp-1, n)) % n

def is_even(n):
    return n % 2 == 0

def square(x):
    return x*x

if __name__ == '__main__':
    pass

