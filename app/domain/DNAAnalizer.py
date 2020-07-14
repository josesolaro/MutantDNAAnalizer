import numpy as np
import utils.InputConverter as converter


class DNAAnalizer:

    def __init__(self, dna_analizer, arr_str):
        self._dna_analizer = dna_analizer
        self._arr_str = arr_str

    def analize(self):
        total_chain_found = 0
        total_chain_found += self.find_horizontal(self._arr_str)
        total_chain_found += self.find_vertical(self._arr_str)
        total_chain_found += self.find_oblique(self._arr_str)

        match = True if total_chain_found > 1 else False
        self._dna_analizer.save_dna(self._arr_str, match)

        return match

    def find_horizontal(self, str):
        return self._dna_analizer.analyze_dna(str)

    def find_vertical(self, str):
        vertical_str = converter.obtain_vertical(str)
        return self._dna_analizer.analyze_dna(vertical_str)

    def find_oblique(self, str):
        partial_found = 0
        mat = np.array([list(s) for s in str])
        partial_found += self._dna_analizer.analyze_dna(converter.oblique_to_horizontal(mat))
        partial_found += self._dna_analizer.analyze_dna(converter.inv_oblique_to_horizontal(mat))
        return partial_found