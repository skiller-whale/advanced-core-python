"""
The code below is almost identical to ex3_part1.

This time, you'll write a new version of `rate_limit`, which accepts an argument
to specify the minimum time there should be between calls. You can copy the
`rate_limit` decorator from exercise 2 as a starting point if you like.

1. Write your new `rate_limit` decorator, which should expect one argument. This
   argument should specify the minimum time (in seconds) allowed between two
   calls to the wrapped function.

2. Uncomment the decorator line above the `send_ping` function. This should
   add a rate limit of one call every 1.75s. Run the script, and make sure that
   the pings are always exactly 1.75s apart.
"""

import logging
import time

from utils import ping


# TODO: Write your new `rate_limit` decorator here.


# @rate_limit(1.75)
def send_ping(url):
    logging.info("Sending ping to %s...", url)
    response = ping(url)
    logging.info("response code: %s\n", response)


while True:
    send_ping("http://adding_para.ms")
