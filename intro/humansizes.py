SUFFIXES = {1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
            1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']}


def approximate_size(size, a_kilobyte_is_1024_bytes=True):
    '''Convert a file size to human-readable form.

    (this is a docstring)

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

# one line conditional much like ternary. multiple is variable.
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000
    # access dictionary SUFFIXS and give me anything accociated with this key
    # suffix is "taco" whatever you want
    for suffix in SUFFIXES[multiple]:
        # same as saying size = size divided by multiple.
        size /= multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)
            # .1f (floating point) for numbers, give me 1 digit after decimal sign

    raise ValueError('number too large')


# checking to see if this is file that is specified when running the application
if __name__ == '__main__':
    print(approximate_size(16384, False))
    print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=False))
    print(approximate_size(16384))
