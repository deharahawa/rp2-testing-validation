import unittest
import os

class crawlerTests(unittest.TestCase):
    def testParse(self):
        self.assertTrue(os.stat("results.txt").st_size == 0)