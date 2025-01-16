import asyncio

async def compute_pi(it):
    """Compute pi using Madhava-Leibniz series.

    Args:
        it (int): The number of iteration of the series.

    Returns:
        float: pi
    """
    pi, sign = 0.0, 1

    for i in range(it):
        pi += sign * 4.0 / (2 * i + 1)
        sign *= -1

        await asyncio.sleep(0)

    print(f'PI computed: {pi}')
    return pi


async def compute_e(it):
    """Computes Euler's constant using the series:
       1/0! + 1/1! + 1/2! + 1/3! + ...

    Args:
        it (int): The number of iterations.

    Returns:
        float: e
    """
    e, fact = 0, 1
    for i in range(it):
        if i > 0:
            fact *= i
        e += 1 / fact

        await asyncio.sleep(0)

    print(f'e computed: {e}')
    return e
