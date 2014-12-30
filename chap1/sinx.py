#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""


def main():
    print(sine(12.15))
    print(better_sine(12.15))

def sine(angle):
    if angle <= 0.1:
        return angle
    else:
        return p(sine(angle/3.0))

def p(x):
    return 3*x-4*cube(x)

def cube(x):
    return x*x*x

def better_sine(angle):
    x = sinx = angle
    while angle > 0.1:
        angle /= 3.0
    while angle < x:
       if angle <= 0.1:
           sinx = angle
       else:
           sinx = 3*sinx - 4*cube(sinx)
       angle *= 3.0
    return sinx
        


if __name__ == '__main__':
    main()

