import logging
import time

from random import random

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def ping(url, _last_ping_times={}):
    """Fakes a 'ping' to a server, with some calls failing"""
    time_now = time.time()

    if url in _last_ping_times:
        elapsed_time = time_now - _last_ping_times[url]
        logging.debug("Time since last ping to %s: %0.2fs", url, elapsed_time)

    _last_ping_times[url] = time_now

    time.sleep(random() / 2. + 0.05)  # Wait between 0.05 and 0.55 seconds

    return 200 if random() < 0.9 else 503  # Randomly send 10% failures
