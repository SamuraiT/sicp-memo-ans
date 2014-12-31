#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""


def main():
    print(expt(3, 4))
    print(fast_expt(3, 4))

def expt(b, n):
    a = 1
    for i in range(n):
       a *= b
    return a

def fast_expt(b, n):
    def iter(b, n, a):
        if n == 0: return a
        if is_even(n):return iter(b*b, n/2, a)
        else: return iter(b, n-1, a*b)
    return iter(b,n,1)

def is_even(x):
    return x % 2 == 0

if __name__ == '__main__':
    main()

