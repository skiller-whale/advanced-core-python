import asyncio
from utils.pub_sub import PubSubServer, PubSubClient, send_message

"""
PUB-SUB SERVER/CLIENT
-------------

In this exercise you will implement a pub-sub server loop using
    the provided PubSubServer and PubSubClient classes.

* Create a `PubSubServer` in `main_async`.

* Create two clients -- `client_1` and `client_2`.
    * Subscribe client_1 to channels `chat` and `general` using
        an appropriate method call on `server`.
    * Subscribe client_2 to the channel `chat`.

* The coroutine `send_message(server: PubSubServerInterface)` waits for 
    a message input from the terminal and sends it to the server.
    This coroutine will run indefinitely.

    Use `asyncio.gather` to run the following coroutines concurrently:
        - do_receive(client_1, server)
        - do_receive(client_2, server)
        - send_message(server)

* Currently messages are not received by the clients because
    do_receive is not implemented.

    Implement the `do_receive` coroutine so that it calls 
    `server.receive_message` appropriately in a loop 
    and prints the following upon receiving a message:

    'Client <client_id> received message: <message>'.

    You will need to call an appropriate method on client
    to obtain the <client_id>.

HINT 1: You will need to use `asyncio.sleep` inside the loop.
HINT 2: You will need to filter the messages received. Check
    the documentation of server.receive_message for details
    of system messages.
"""

async def do_receive(client, server):
    # TODO: Implement do_receive so that
    #    it continuously polls the PubSubServer and
    #    prints the messages client received.
    pass

async def main_async():
    # TODO: Implement pub-sub logic here.
    server = ...

if __name__ == "__main__":
    try:
        asyncio.run(main_async())
    except KeyboardInterrupt:
        print("\nGoodbye!")
