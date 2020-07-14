import unittest
import numpy as np
import mock
from utils import InputConverter

class InputConverterTest(unittest.TestCase):
    def test_obtain_vertical_should_return_traspose(self):
        result = InputConverter.obtain_vertical(["ABCD","ABCD","ABCD","ABCD"])
        self.assertEqual(["AAAA","BBBB","CCCC","DDDD"],result)

    def test_obtain_oblique_should_return_oblique(self):
        result = InputConverter.oblique_to_horizontal(np.array([list(s) for s in ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG"]]))
        self.assertEqual(["AAAA"],result)

    def test_obtain_inv_oblique_should_return_inv_oblique(self):
        result = InputConverter.oblique_to_horizontal(np.array([list(s) for s in ["ACGA", "GAGC", "ATAT", "AAGA"]]))
        self.assertEqual(["AAAA"],result)