import functools
import logging
import random
import time


def titlecase(string):
    """Capitalise the first letter of each word in string"""
    return string.title()


def remove_spaces(string):
    """Remove all spaces from string"""
    return string.replace(' ', '')


def lowercase_first_letter(string):
    """Make the first letter of string lowercase"""
    return string[0].lower() + string[1:]


def ping():
    """Fakes a 'ping' to a server, with some calls failing"""
    time.sleep(random.random() + 0.5)
    switch = random.random()
    if switch < 0.2:
        raise ConnectionError("Could not connect to server")
    elif switch < 0.4:
        return 503
    else:
        return 200


def format_function(name, args, kwargs):
    args_display = [str(arg) for arg in args]
    kwargs_display = [f"{kw}={value}" for kw, value in kwargs.items()]
    arguments_display = ', '.join(args_display + kwargs_display)
    return f"{name}({arguments_display})"


def log_duration(func):
    """Decorator that logs how long a function call takes"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        duration = round(time.time() - start, 2)
        logging.info(f"Call to {func.__name__} took {duration}s")
        return result
    return wrapper


def debug(func):
    """Decorator that logs function calls, with arguments and returned value"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        logging.debug(
            "Calling: %s" % format_function(func.__name__, args, kwargs)
        )
        result = func(*args, **kwargs)
        logging.debug(f"Call to {func.__name__} returned: {result}")
        return result
    return wrapper
