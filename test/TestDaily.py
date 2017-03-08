# -*- coding: UTF-8 -*-

import unittest


class TestDaily(unittest.TestCase):
    def setUp(self):
        pass

    def test_number(self):
        self.assertEquals(3**2, 9)


if __name__ == '__main__':
    unittest.main()