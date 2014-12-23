#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""


def main():
    display_pascal(5)

def display_pascal(n):
    for i in range(n):
        for j in range(i+1):
            print comb(i,j),
        print

def comb(n, m):
    return fact(n)/(fact(m) * fact(n-m))

def fact(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

if __name__ == '__main__':
    main()

