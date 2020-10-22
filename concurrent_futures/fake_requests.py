"""DO NOT EDIT THIS FILE

This simulates slow requests to websites used in the exercises.
If you provide an unexpected url then it will raise a connection error.
"""

import pathlib
import time
import random
import json


data_dir = pathlib.Path(__file__).parent / 'data'
temperatures_file = data_dir / 'temperatures.json'
speed_test_file = data_dir / 'speed_test.json'


url_data = {}

for path in [speed_test_file, temperatures_file]:
    with open(path) as file:
        url_data.update(json.load(file))


def get(url, max_wait=1):
    if url not in url_data:
        print(f"fake_requests does not have any data for {url}!")
        raise ConnectionError(f"fake_requests could not connect to {url}")

    time.sleep(random.uniform(max_wait/2, max_wait))
    return url_data[url]