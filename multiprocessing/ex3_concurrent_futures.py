"""
The code below is similar to the previous exercise, hashing passwords with a
CPU-intensive algorithm. Follow the instructions further down to update the
script so that it uses concurrent.futures to parallelise the task.
"""

import concurrent.futures
import pathlib
import time

from utils import hash_password, PASSWORDS  # a dict of { username : password }
start_time = time.time()  # Used to time the execution of this script


def write_to_file(path, username, salt, hashed_password):
    """Write username, salt and hashed_password to file, separated by commas"""
    with open(path, 'a') as file:
        file.write(f'{username}, {salt}, {hashed_password}\n')

# Define the hashed passwords file path, and create a blank file there
target_path = pathlib.Path(__file__).parent / 'hashed_passwords_3.txt'
with open(target_path, 'w'):
    pass

# <<<<<<<<<<<<<<<<<<<<<<<<<<<< INSTRUCTIONS >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#
# Update this code to use concurrent.futures
#
# You'll need to:
#
#   1. Create an appropriate executor (remember this is a CPU-bound task)
#
#   2. Call .submit with each (username, password) combination and keep track
#      of the futures returned.
#
#      You'll also need to match these futures with their corresponding
#      username, so you might want to store them as a {username: future} dict
#
#   3. Loop over these returned futures to get the results, and call
#      write_to_file to write the results back to the file.

for username, password in PASSWORDS.items():
    hashed_password, salt = hash_password(password)
    write_to_file(target_path, username, salt, hashed_password)

# <<<<<<<<<<<<<<<<< DON'T CHANGE THE CODE BELOW HERE >>>>>>>>>>>>>>>>>>>>>>>>>>>

print(f'Done in {time.time() - start_time:.2f}.')
print(f'Hashed passwords saved to: {target_path}')
