# ----------------------------------------------------------------------------------------------------------------------

from time import time
from util.size import *

# ----------------------------------------------------------------------------------------------------------------------


class Timem(object):
    last_time = 0
    start_time = time()
    last_memory_usage = 0
    total_memory_usage = 0

# ----------------------------------------------------------------------------------------------------------------------


def timeit(method):

    def timed(*args, **kw):
        ts = time()
        result = method(*args, **kw)
        te = time()
        Timem.last_time = te - ts
        return result

    return timed

# ----------------------------------------------------------------------------------------------------------------------


def memit(obj):

    Timem.last_memory_usage = sizeof(obj)
    Timem.total_memory_usage += Timem.last_memory_usage


# ----------------------------------------------------------------------------------------------------------------------
