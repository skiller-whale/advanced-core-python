from time import time

from numpy import true_divide

"""
BASIC CONTEXT MANAGER

1. Implement the below context manager so it times (in seconds) how long its block takes to execute.
When called, the imported function `time` reports the time (in seconds) that have ellapsed since
January 1st 1970.
Ignore the arguments to `__exit__` for now.

2. Using the `with TimingManager()` syntax, convert the main function so
it uses the TimingManager.
"""

class TimingManager:
    def __init__(self):
        pass

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        pass


### SOLUTION
# class TimingManager:
#     def __init__(self):
#         pass

#     def __enter__(self):
#         self.time = time()

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         print(time() - self.time)


def slow_function():
    print("Executing slow function")
    return [i ** 2 for i in range(int(1e7))]


def main():
    start_time = time()
    slow_function()
    end_time = time()
    elapsed_time = end_time - start_time
    print(elapsed_time)

    ### SOLUTION
    # with TimingManager():
    #     slow_function()



main()


"""
HANDLING EXCEPTIONS

1. Change the TimingManager so that it reports whether the code executed successfully.
You will need to use the `exc_type` argument to the `__exit__` method.

2. Add a `recognised_exceptions` argument to the constructor, with a default value of [].
This will be a list of exception types that the TimingManager captures.
If an exception is raised and it's a recognised one, the manager should report how long
it took to reach that error, as well as print out its message.
Otherwise, that error should be left unhandled.
"""

class TimingInterupt(Exception):
    pass

### SOLUTION
# class TimingManager:
#     def __init__(self, recognised_exceptions=[]):
#         self.recognised_exceptions = recognised_exceptions

#     def __enter__(self):
#         self.time = time()

#     def __exit__(self, exc_type, exc_value, exc_traceback):
#         if not exc_type:
#             print(time() - self.time)

#         if exc_type in self.recognised_exceptions:
#             print(time() - self.time)
#             print(exc_value)
#             return True
#         return False

def main():
    raise_exception = True
    with TimingManager([TimingInterupt]):
        slow_function()
        if raise_exception:
            raise TimingInterupt("Execution was stopped after the first function call")
        slow_function()
    print("The block has exited")

main()


"""
CONTEXT MANAGER DECORATOR

1. Convert the below class context manager to a function one.

2. Change the main function so that it uses the new context manager.
"""
import io
from contextlib import contextmanager

class FileManager:
    def __init__(self, file_path, mode):
        self.file_path = file_path
        self.mode = mode

    def __enter__(self):
        self.file_obj = open(self.file_path, mode=self.mode)
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file_obj:
            self.file_obj.close()

        if exc_type:
            if isinstance(exc_val, io.UnsupportedOperation):
                print("Trying to write to a read-only file.")
                return True
            return False

### SOLUTION
# @contextmanager
# def file_manager(file_path, mode):
#     try:
#         file_obj = open(file_path, mode=mode)
#         yield file_obj
#     except io.UnsupportedOperation:
#         print("Trying to write to a read-only file.")
#     except Exception as e:
#         raise e


def main():
    try_write = True
    with FileManager('./data/word_set_1.txt', 'r') as file:
    ### SOLUTION
    # with file_manager('./data/word_set_1.txt', 'r') as file:
        if try_write:
            file.write('test')
        else:
            file.unexisting_method()

main()


"""
MULTIPLE CONTEXT MANAGERS

When testing, you may sometimes want to 'mock' some global properties.
For example, imagine that you want to ensure that a function always reports
the same time taken to execute.

1. Create a context manager that replaces the imported time function with
an anonymous function that always returns 0. When the context manager is exited
the global function should be restored to its previous value.

2. Write code in the main function that times `slow_function` and produces
a total time of 0 seconds.

3. Reverse the order of the context managers. What happens?
"""

### SOLUTION
# @contextmanager
# def mock_time():
#     global time
#     saved_time = time
#     time = lambda: 0
#     yield
#     time = saved_time

def main():
    pass
    # SOLUTION
    # CORRECT
    # with mock_time():
    #     with TimingManager():
    #         slow_function()

    # REVERSED
    # with TimingManager():
    #     with mock_time():
    #         slow_function()


main()


"""
CONTEXTLIB UTILITIES

Use `ExitStack` to make sure that all opened files are closed by the end of
the exection of the program.
"""
from contextlib import ExitStack
from pathlib import Path

def round_robin(stream):
    blank_line_encountered = False
    while not blank_line_encountered:
        for stream in streams:
            line = stream.readline().strip()
            if not line:
                blank_line_encountered = True
                break
            print(line)

txt_files = sorted(Path("data").rglob("*.txt"))

streams = [open(fname, "r") for fname in txt_files]
round_robin(streams)

# SOLUTION
# with ExitStack() as stack:
    # streams = [stack.enter_context(open(fname, "r")) for fname in txt_files]
    # round_robin(streams)


### CHECK THAT THE FILES HAVE BEEN CLOSED

for stream in streams:
    print(stream)
    if not stream.closed:
        raise Exception("A file was left unclosed")