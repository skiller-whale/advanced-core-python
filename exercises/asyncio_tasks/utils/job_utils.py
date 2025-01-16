import json

def parse_jobs_file(filename, job_funcs_dfns):
    """Parse a JSON file of jobs and return a list of dictionaries
        {
            'func': <python function>
            'interval': int
        }

    Args:
        filename (str): JSON file of job definitions
        job_funcs_dfns: A object that contains python functions.
    """
    # Read jobs file and parse to a list of dicts of
    all_jobs = []

    with open(filename) as job_file:
        try:
            # Parse JSON file
            contents = json.loads(job_file.read())

            # JSON file should be a list of jobs
            for job_definition in contents:
                job_def = {
                    'func': getattr(job_funcs_dfns, job_definition['func']),
                    'interval': float(job_definition['interval']),
                }
                if 'repeats' in job_definition:
                    job_def['repeats'] = int(job_definition['repeats'])
                all_jobs.append(job_def)

        except Exception:
            print(f'[error] Error parsing jobs file!')

    return all_jobs
