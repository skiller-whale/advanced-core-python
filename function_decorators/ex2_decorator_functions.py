"""
The imported ping method will (pretend to) send a ping to a web server, and
either return a status code (e.g. 200) or raise a ConnectionError.

1. Run this script - you should see some output indicating that several pings
   are being sent. Eventually one will error and the program will terminate.

2. Decorate send_ping with the catch_errors decorator.

   (at the moment this won't do anything because catch_errors just returns
   the function it decorates without adding any behaviour)

3. Update the catch_errors decorator so it catches any errors raised by the
   wrapped function (func), and prints an error message instead of terminating.

   NOTE: To catch and print exceptions raised by a_function, you could write:

   try:
       a_function()
   except Exception as error:
       print("ERROR:", error)

4. Run the script again. Instead of terminating, errors in the ping() call
   should now be handled more gracefully.
"""

# Client is a class which simulates fake 'ping's to a web server
from utils import ping


def catch_errors(func):
    """A decorator that will catch and print any errors raised by func"""
     # TODO: Properly implement this decorator function
    return func


def send_ping():
    print("Sending ping to server...", end='\t', flush=True)
    response = ping()
    print("response code:", response)


if __name__ == "__main__":
    while True:
        send_ping()
