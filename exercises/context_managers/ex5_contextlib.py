from contextlib import ExitStack
from pathlib import Path

BASE_PATH = Path(__file__).parent / 'data'


"""
CONTEXTLIB UTILITIES

The below code reads three files line-by-line in a round-robin manager.
    This means after reading a line from one file, it reads a line from
    the next file and then the next and so on.

Use `ExitStack` to make sure that all opened files are closed by the end of
    the execution of the program.
"""


def round_robin(files):
    blank_line_encountered = False
    while not blank_line_encountered:
        for stream in files:
            # read a line from the file
            line = stream.readline().strip()
            if not line:
                # exit if end of file
                blank_line_encountered = True
                break
            # print line
            print(line.strip())


if __name__ == "__main__":
    # YOUR CODE GOES HERE
    files = [
        open(BASE_PATH / f"word_set_{i}.txt")
        for i in range(3)
    ]

    round_robin(files)

    ### DO NOT EDIT BELOW
    ### CHECK THAT THE FILES HAVE BEEN CLOSED
    for file in files:
        assert file.closed, "A file object was not closed!"
