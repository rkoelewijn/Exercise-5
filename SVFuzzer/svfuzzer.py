from typing import List, Callable


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
        pass

    def runs(self):
        """
        Run the fuzzer for input_num times.
        For every 100 runs, print the number of runs and the coverage value
        """
        pass
