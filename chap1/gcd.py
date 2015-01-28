#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""


def gcd(a, b):
    if b == 0: return a
    return gcd(b, a%b)

def while_gcd(a, b):
    while b != 0:
        a,b = calc_new_gcd(a,b)
    return a

def calc_new_gcd(a, b):
    r = a%b
    a = b
    b = r
    return a, b

if __name__ == '__main__':
    print(gcd(206, 40))
    print(gcd(28, 16))
    print(while_gcd(206, 40))
    print(while_gcd(28, 16))


