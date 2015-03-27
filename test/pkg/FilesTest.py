'''
Created on 26 mai 2014

@author: Odile
'''
import struct
import unittest

from pkg.dataset import RawDataset


class Test(unittest.TestCase):

    def setUp(self):
        self.filename = "G:\\PIRENEA_manips\\2014\\data_2014_07_30\\2014_07_30_001.A00"
        self.wrong = self.filename + ".txt"

    def tearDown(self):
        pass

    def test01_contents(self):
        r = RawDataset(self.filename)
        self.assertIsInstance(r.step, float)
        self.assertGreater(r.points, 0)

    def test02_noFilename(self):
        self.assertRaises(IOError, r=RawDataset(""))

    def test03_badTypeOfFile(self):
        self.assertRaises(struct.error, r=RawDataset(self.wrong))


if __name__ == "__main__":
    #     import sys;sys.argv = ['', 'Test.testName']
    unittest.main(verbosity=2)
