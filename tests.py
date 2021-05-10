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


if __name__ == '__main__':
    unittest.main()
