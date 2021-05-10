# Andrew Eppinger
# CS362 Software Engineering II - Spring 2021
# A2: TDD Hands On - Unit tests

import unittest
from unittest import TestCase
from check_pwd import check_pwd


class Test(TestCase):
    def test1(self):
        inp = ""
        expected = False
        self.assertEqual(check_pwd(inp), expected)

    def testLength1(self):
        inp = "abcdefg"
        self.assertFalse(check_pwd(inp))

    def testLength2(self):
        inp = "abcdefghijklmnopqrstu"
        self.assertFalse(check_pwd(inp))

    def testChars1(self):
        inp = "TESTPASSWORD"
        self.assertFalse(check_pwd(inp))

    def testChars2(self):
        inp = "testpassword"
        self.assertFalse(check_pwd(inp))


if __name__ == '__main__':
    unittest.main()
