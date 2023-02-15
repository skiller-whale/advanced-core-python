from time import time
from contextlib import contextmanager

"""
CONTEXT MANAGER DECORATOR

1. Convert the below class context manager to a function one using
    @contextmanager.

2. Change the main function so that it uses the new context manager.

HINT: A try block must have an except block too.
    In this case do you need a try block at all?
"""


class CustomError(Exception):
    pass


def slow_function():
    """A slow function that takes a while to execute.
    """
    return [i ** 2 for i in range(int(1e6))]


def slow_crashing_function():
    """A slow function that takes a while to execute and then crashes.
    """
    a_long_list = [i ** 2 for i in range(int(1e6))]
    raise CustomError()


class TimingManager:
    def __enter__(self):
        self._start_time = time()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is CustomError:
            end_time = time()
            elapsed_time = end_time - self._start_time
            print(f"Execution time was {elapsed_time}")

        # we are not processing exceptions
        return False


if __name__ == "__main__":
    with TimingManager():
        # this should print the execution time
        slow_function()

    with TimingManager():
        # this should not print anything
        #   and propagate the CustomError
        slow_crashing_function()

    print("The block has exited")
