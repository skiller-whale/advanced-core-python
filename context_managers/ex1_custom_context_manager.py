from time import time

"""
CUSTOM CONTEXT MANAGERS

1. Define and implement a `TimingManager` context manager
    which times (in seconds) how long its block takes to execute.

2. Upon exiting, `TimingManager` should print the execution time.
    Ignore the arguments to `__exit__` for this task.

3. Rewrite __main__ so that it uses `TimingManager` .

HINT: Like in __main__, you can use the `time` function to get the 
    current UNIX time in seconds. This is an integer that reports the 
    seconds that elapsed since January 1st 1970.
"""


class TimingManager:
    # YOUR CODE GOES HERE
    pass


def slow_function():
    """A slow function that takes a while to execute.
    """
    return [i ** 2 for i in range(int(1e6))]


if __name__ == "__main__":
    # record start time
    start_time = time()

    slow_function()

    # print the elapsed time
    end_time = time()
    elapsed_time = end_time - start_time
    print(f"Execution time was {elapsed_time}")
