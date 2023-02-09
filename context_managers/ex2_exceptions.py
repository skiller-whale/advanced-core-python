from time import time

"""
HANDLING EXCEPTIONS

1. Change `TimingManager` so that it only reports the time when the code
    within its`with` block executes successfully.

2. Make sure you are propagating the resulting exception so that
    when running the script you see a stack trace.

HINT: You will need to use the `exc_type` argument to the `__exit__` method.
"""


class CustomException(Exception):
    pass


def slow_function():
    """A slow function that takes a while to execute.
    """
    return [i ** 2 for i in range(int(1e6))]


def slow_crashing_function():
    """A slow function that takes a while to execute and then crashes.
    """
    a_long_list = [i ** 2 for i in range(int(1e6))]
    raise CustomException()


class TimingManager:
    def __enter__(self):
        self._start_time = time()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        end_time = time()
        elapsed_time = end_time - self._start_time
        print(f"Execution time was {elapsed_time}")


if __name__ == "__main__":
    with TimingManager():
        # this should print the execution time
        slow_function()

    with TimingManager():
        # this should not print anything
        #   and propagate the CustomException
        slow_crashing_function()

    print("The block has exited")
