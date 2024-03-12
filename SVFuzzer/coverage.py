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
        self.last_line = None 


    def tracer(self, frame, event, arg=None):
        code = frame.f_code 

        func_name = code.co_name

        line_no = frame.f_lineo 

        self.cov_lines_set.add(line_no)

        if self.last_line is None:
            self.last_line = line_no
        else:
            self.cov_pairs_set.add((self.last_line, line_no))
            self.last_line = line_no

        print(f"A {event} encountered in \{func_name}() at line number {line_no} ") 
  
        return self.tracer 
    

    def coverage_runner(self):
        """
        Calculate the covered lines and pairs of lines
        return True if no exception was thrown (test passed)
        return False if there is exception (test failed)
        """
        settrace(self.tracer)
        try:
            self.to_exec(self.inp)
            settrace(None)
            return True
        except Exception as e:
            print(f"Exception thrown {e}")
            settrace(None)
            return False

