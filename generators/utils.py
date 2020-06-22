def format_big_int(value):
    """Return a standard form representation of a large integer

    This is needed because float types cannot handle values associated with
    big integer types
    """
    string = str(value)
    exponent = len(string) - 1
    base = round(int(string[:5]), -2) / 10_000
    return f"{base}e+{exponent}"


def format_size(n_bytes):
    """Format a number of bytes as a human-readable string"""
    for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
        if abs(n_bytes) < 1024.0:
            return f"{n_bytes:.1f} {unit}B"
        n_bytes /= 1024.0
    return f"{n_bytes:.1f} YiB"



def display_malloc_snapshot(snapshot):
    """Helper function for rendering a tracemalloc memory usage snapshot"""
    print("\nMemory Allocation:")
    for statistic in snapshot.statistics('lineno'):
        line_no = statistic.traceback[0].lineno
        print("----------------")
        print(f'Line {line_no}: ', statistic.traceback.format()[-1].strip())
        print('Allocates', format_size(statistic.size), 'of memory')
    print()
