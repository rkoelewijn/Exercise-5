from html.parser import HTMLParser
from mutator import Mutator
from coverage import Coverage
import random

class SVFuzzer:
    def __init__(self, coverage_type: int, input_num: int, seeds: list, target_file: str):
        """
        Constructor of SVFuzzer

        :param coverage_type: type of coverage used for the fuzzing.
            0 stands for line coverage, 1 stands for branch coverage
        :param input_num: the number of generated inputs
        :param seeds: initial inputs given by the user
        :param target_file: the file you will consider for coverage calculation. In this case, "html/parser.py"
        """
        self.coverage_type = coverage_type
        self.input_num = input_num
        self.seeds = seeds
        self.target_file = target_file
        self.corpus = seeds[:]
        self.mutator = Mutator()
        self.parser = HTMLParser()
        self.coverage = Coverage(target_file, self.parser.feed, '')

    def generate_input(self):
        """
        Generate a new input by mutating an existing input from the corpus
        """
        return self.mutator.mutate(random.choice(self.corpus))

    def execute_input(self, input):
        """
        Execute the target function/method with the given input
        """
        return self.coverage.coverage_runner()

    def runs(self):
        """
        Run the fuzzer for input_num times.
        For every 100 runs, print the number of runs and the coverage value
        """
        failures = 0
        for i in range(1, self.input_num + 1):
            input = self.generate_input()
            coverage_result = self.execute_input(input)
            
            if not coverage_result:
                failures += 1
                print(f"Failure {failures}: Input - {input}")

            if i % 100 == 0:
                coverage_value = len(self.coverage.cov_lines_set) if self.coverage_type == 0 else len(self.coverage.cov_pairs_set)
                print(f"Number of runs: {i}, Coverage: {coverage_value}")
