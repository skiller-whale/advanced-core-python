"""
The code below is very similar to the code in exercise 1. A ping is sent in a
loop, with the response logged.

This time, you'll write a new version of `add_delay`, which accepts an argument
to specify how long the delay should be. You can copy the `add_delay` decorator
from exercise 1 as a starting point.

1. Write your new `add_delay` decorator, which should expect one argument. This
   argument should specify the length of time (in seconds) to sleep before
   calling the wrapped function.

2. Uncomment the decorator line above the `send_ping` function. This should
   add a 1.5 second delay before each call. Run the script, and make sure that
   the pings are always > 1.5s apart.

3. Change the 1.5 to 3, and make sure that the ping spacing increases to > 3s
"""

import logging
import time

from utils import ping


# TODO: Write your new `add_delay` decorator here.


# @add_delay(1.5)
def send_ping(url):
    logging.info("Sending ping to %s...", url)
    response = ping(url)
    logging.info("response code: %s\n", response)


while True:
    send_ping("http://adding_para.ms")
