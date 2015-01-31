#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import sys
sys.setrecursionlimit(10000)

def main():
    pass

def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(17)
    True
    >>> is_prime(27644437)
    True
    """
    return smallest_divisor(n) == n

def smallest_divisor(n):
    return non_recursive_find_divisor(n, 2)
    #return find_divisor(n, 2)

def square(x):
    return x*x

def is_divisible(a, b):
    return a % b == 0

def find_divisor(n, test_divisor):
    if square(test_divisor) > n:
        return n
    if is_divisible(n, test_divisor):
        return test_divisor
    else:
        return find_divisor(n, test_divisor+1)

def non_recursive_find_divisor(n, test_divisor):
    """
    while loop version of find divisor
    """
    while square(test_divisor) <= n:
        if is_divisible(n, test_divisor):
            return test_divisor
        test_divisor +=  1
    return n

if __name__ == '__main__':
    pass

[]
