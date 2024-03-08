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
        self.target_file = target_file
        self.to_exec = to_exec
        self.inp = inp
        self.cov_lines_set = set()  # set of covered lines
        self.cov_pairs_set = set()  # set of covered pairs of lines

    def trace_lines(self, frame, event, arg):
        """
        Trace function to record executed lines
        """
        if event == 'line':
            filename = frame.f_code.co_filename
            line_number = frame.f_lineno
            if filename.endswith(self.target_file):
                self.cov_lines_set.add((filename, line_number))
        return self.trace_lines

    def trace_pairs(self, frame, event, arg):
        """
        Trace function to record executed pairs of lines
        """
        if event == 'line':
            filename = frame.f_code.co_filename
            line_number = frame.f_lineno
            if filename.endswith(self.target_file):
                if hasattr(self, 'prev_line'):
                    self.cov_pairs_set.add(((self.prev_file, self.prev_line), (filename, line_number)))
                self.prev_file = filename
                self.prev_line = line_number
        return self.trace_pairs

    def coverage_runner(self):
        """
        Calculate the covered lines and pairs of lines
        return True if no exception was thrown (test passed)
        return False if there is an exception (test failed)
        """
        try:
            settrace(self.trace_lines)
            settrace(self.trace_pairs)
            self.to_exec(self.inp)
            return True
        except Exception:
            return False
