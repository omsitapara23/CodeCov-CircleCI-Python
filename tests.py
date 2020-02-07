import unittest

import src


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(src.smile(), ":)")
        self.assertEqual(src.frown(), ":(")


if __name__ == '__main__':
    unittest.main()
