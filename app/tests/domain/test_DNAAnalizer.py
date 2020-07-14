import unittest
import mock
from domain.DNAAnalizer import DNAAnalizer
from domain.MutantsAnalizer import MutantsAnalizer

@mock.patch("domain.DNAAnalizer.DNAAnalizer")
class DNAAnalizerTest(unittest.TestCase):
    def test_analize_should_return_true(self, mock_dnaanalizer):
        mock_dnaanalizer.save_dna.return_value = True
        mock_dnaanalizer.analyze_dna.return_value = 1
        result = DNAAnalizer(mock_dnaanalizer, ["CTGCCA", "CCCCTG", "CTCCTG", "CCTCCG"]).analize()
        self.assertEqual(True, result)

    def test_analize_should_return_false_when_none_dna_found(self, mock_dnaanalizer):
        mock_dnaanalizer.save_dna.return_value = True
        mock_dnaanalizer.analyze_dna.return_value = 0
        result = DNAAnalizer(mock_dnaanalizer, ["CTGCCA", "CCCCTG", "CTCCTG", "CCTCCG"]).analize()
        self.assertEqual(False, result)

    def test_find_horizontal_should_return_1(self, mock_dnaanalizer):
        result = DNAAnalizer(MutantsAnalizer,[]).find_horizontal(["CCCCTG"])
        self.assertEqual(1,result)

    def test_find_horizontal_should_return_0(self, mock_dnaanalizer):
        result = DNAAnalizer(MutantsAnalizer,[]).find_horizontal(["CCTCTG"])
        self.assertEqual(0,result)

    def test_find_vertical_should_return_1(self, mock_dnaanalizer):
        result = DNAAnalizer(MutantsAnalizer,[]).find_vertical(["CTGCCA","CTCGTG","CTGCTG","CCTCTG"])
        self.assertEqual(1,result)

    def test_find_vertical_should_return_0(self, mock_dnaanalizer):
        result = DNAAnalizer(MutantsAnalizer,[]).find_vertical(["ATGCCA","CTCGTG","CTGCTG","CCTCTG"])
        self.assertEqual(0,result)

    def test_find_oblique_should_return_1(self, mock_dnaanalizer):
        result = DNAAnalizer(MutantsAnalizer,[]).find_oblique(["CTGCCA","CCCGTG","CTCCTG","CCTCCG"])
        self.assertEqual(1,result)

    def test_find_oblique_should_return_0(self, mock_dnaanalizer):
        result = DNAAnalizer(MutantsAnalizer,[]).find_oblique(["ATGCCA","CTCGTG","CTGCTG","CCTCTG"])
        self.assertEqual(0,result)