#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""


def main():
    print(expt(3, 3))

def expt(b, n):
    x = 0
    bn = 1
    while x < n:
        bn = b * bn
        x += 1
    return bn


if __name__ == '__main__':
    main()

