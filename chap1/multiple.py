#! /usr/bin/env python
# coding: utf-8
"""
Copyright 2014 Tatsuro Yasukawa.

Distributed under the GNU General Public License at
gnu.org/licenses/gpl.html.
"""
import unittest

class TestMultiple(unittest.TestCase):
    def test_mult(self):
        a,b  = 2,3
        self.assertEqual(mult(a,b), a*b)
        a,b = 4,5
        self.assertEqual(mult(a,b), a*b)

def main():
    pass    

def mult(a,b):
    ans = 0
    for i in range(b):
        ans += a
    return ans

if __name__ == '__main__':
    unittest.main()

