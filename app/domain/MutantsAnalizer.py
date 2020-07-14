import re
from model.Mutants import Mutants


class MutantsAnalizer():

    @staticmethod
    def analyze_dna(arr_str):
        adn_chain_size = 0
        for s in arr_str:
            adn_chain_size += len(re.findall(r"C{4}|A{4}|G{4}|T{4}", s))
        return adn_chain_size

    @staticmethod
    def save_dna(arr_str, match):
        try:
            mutant = Mutants(dna=",".join(arr_str), ismutant=match)
            mutant.save_mutant()
        except:
            raise Exception("Could not process request")

    @staticmethod
    def get_mutants_ratio():
        try:
            mutant = Mutants()
            return mutant.get_mutants_ratio()
        except:
            raise Exception("Could not process request")