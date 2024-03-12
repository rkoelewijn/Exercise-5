from sys import settrace
from typing import Callable


class Coverage:
    def __init__(self, target_file: str, to_exec: Callable, inp: str):
        """
        Constructor for Coverage

        :param target_file: the file used to calculate the coverage
        :param to_exec: the function/method to execute
        :param inp: the input for to_exec
        """
        self.cov_lines_set = set()  # set of covered lines
        self.cov_pairs_set = set()  # set of covered pairs of lines
        pass

    def coverage_runner(self):
        """
        Calculate the covered lines and pairs of lines
        return True if no exception was thrown (test passed)
        return False if there is exception (test failed)
        """
        pass
