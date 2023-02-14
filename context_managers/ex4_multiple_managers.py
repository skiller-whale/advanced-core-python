from time import time
from contextlib import contextmanager

"""
MULTIPLE CONTEXT MANAGERS

When testing, you often want to 'mock' some global properties.
For example, imagine that you want to ensure that a function always reports
the same time taken to execute.

1. Create a context manager that replaces the imported time function with
a function that always returns 0. When the context manager is exited
the global function should be restored to its previous value.

2. Use the `mock_time` context manager in `__main__` together with
    `Timing Manager` so that it prints a time of `0`.

3. Reverse the order of the context managers.
    Can you explain what is happening?

HINT: You can define a custom mock time function or you can use
    a lambda expression inside the `mock_time` context manager.
"""


def slow_function():
    """A slow function that takes a while to execute.
    """
    return [i ** 2 for i in range(int(1e6))]


@contextmanager
def TimingManager():
    start_time = time()

    yield

    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Execution time was {elapsed_time}")


@contextmanager
def mock_time():
    global time
    # YOUR CODE GOES HERE


if __name__ == "__main__":
    with TimingManager():
        slow_function()
