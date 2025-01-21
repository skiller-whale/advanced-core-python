import asyncio
from pathlib import Path
from utils import job_funcs, job_utils

DATA_PATH = Path(__file__).parent / 'data'

# pylint: disable=pointless-string-statement
"""
In this exercise you will implement code that runs tasks at regular intervals in the future.

Jobs are specified data/jobs.json as a python function name ("func")
    and an "interval" in seconds (delay between calls):
{
    "func": "print_date",
    "interval": 2.5,
    "repeats": 10
}

The functions to be executed for each job are defined in the module
`utils.job_funcs` (imported above - you don't need to edit these).

Currently the `__main__` block parses the JSON file into a list of dicts that contain the job
    function and interval:
{
    "func": <python function>,
    "interval": <float>
}

1. `main_async` is called with a list of jobs. For each job, schedule
    `run_job` using `create_task`.

2. Implement `run_job` to run the job at the interval.

HINT 1: You can await tasks returned from `create_task`.
NOTE: This is similar to a cronjob service on UNIX/Linux.
"""

async def run_job(job, interval):
    """Runs `job` asynchronously at an `interval`.

    Args:
        job (func): A function that takes no arguments.
        interval (Numeric): Number of seconds between calls.
    """
    # YOUR CODE GOES HERE
    pass


async def main_async(jobs):
    # YOUR CODE GOES HERE
    # Run each job in `jobs` using `run_job`.
    print(jobs)

    pass


if __name__ == '__main__':
    all_jobs = job_utils.parse_jobs_file(DATA_PATH / 'jobs.json', job_funcs)
    # Call main_async to schedule all jobs
    asyncio.run(main_async(all_jobs))
