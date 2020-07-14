import unittest
import mock
from domain.MutantsAnalizer import MutantsAnalizer

@mock.patch("model.Mutants.Mutants")
class MutantsAnalizerTest(unittest.TestCase):
    def test_analyze_dna_should_return_1(self, mockmutants):
        result = MutantsAnalizer.analyze_dna(["CCCCTG"])
        self.assertEqual(1,result)

    def test_analyze_dna_should_return_0(self, mockmutants):
        result = MutantsAnalizer.analyze_dna(["CTCCTG"])
        self.assertEqual(0,result)

    def test_analyze_2dna_should_return_1(self, mockmutants):
        result = MutantsAnalizer.analyze_dna(["CTCCTG","CCCCTG"])
        self.assertEqual(1,result)

    def test_save_mutant_should_raise_except(self, mockmutants):
        self.assertRaises(Exception, MutantsAnalizer.save_dna,["CCCCTG","CCCCTG","CCCCTG"],True)

    def test_save_mutant_should_finish(self, mockmutants):
        mockmutants.save_mutant.return_value = True
        MutantsAnalizer.save_dna(["CCCCTG","CCCCTG","CCCCTG"],True, mockmutants)
        self.assertTrue(True)

    def test_get_mutant_ratio_should_raise_except(self, mockmutants):
        self.assertRaises(Exception, MutantsAnalizer.get_mutants_ratio)

    def test_get_mutant_ratio_should_finish(self, mockmutants):
        mockmutants.get_mutants_ratio.return_value = True
        MutantsAnalizer.get_mutants_ratio(mockmutants)
        self.assertTrue(True)