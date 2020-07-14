import unittest
import mock
from mock import MagicMock
from model import Mutants

Mutants.db=MagicMock()

class MutantsTest(unittest.TestCase):
    def test_save_mutant_should_finish(self):
        mutant = Mutants.Mutants()
        mutant.save_mutant()
        self.assertTrue(True)

    def test_get_mutants_ratio_should_raiseException(self):
        mutant = Mutants.Mutants()
        self.assertRaises(ZeroDivisionError, mutant.get_mutants_ratio)
