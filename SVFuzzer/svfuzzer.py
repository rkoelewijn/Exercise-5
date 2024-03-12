from typing import List, Callable

from coverage import Coverage
from mutator import Mutator



class SVFuzzer:
    def __init__(self, coverage_type: int, input_num: int, seeds: List[str], target_file: str, function: Callable):
        """
        Constructor of SVFuzzer

        :param coverage_type: type of coverage used for the fuzzing.
            0 stands for line coverage, 1 stands for branch coverage
        :param input_num: the number of generated inputs
        :param seeds: initial inputs given by the user
        :param target_file: the file you will consider for coverage calculation. In this case, "html/parser.py"
        :param function: the function/method you want to fuzz
        """
        self.coverage_type = coverage_type
        self.input_num = input_num
        self.seeds = seeds
        self.target_file = target_file
        self.function = function 
        

    def runs(self):
        """
        Run the fuzzer for input_num times.
        For every 100 runs, print the number of runs and the coverage value
        """

        mutator = Mutator() 

        visited_lines = set() 

        for i in range(0,self.input_num):
            if (i % 100) == 0: 
                print(f"{i} runs, coverage is {len(visited_lines)}")

            mutated = mutator.mutate(self.seeds.pop())
            cov = Coverage(self.target_file, self.function, mutated)
            if self.coverage_type == 0: 
                visited_lines = visited_lines.union(cov.cov_lines_set)
            else: 
                visited_lines = visited_lines.union(cov.cov_pairs_set)
            
        

            
