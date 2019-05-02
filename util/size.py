# ----------------------------------------------------------------------------------------------------------------------

import sys

# ----------------------------------------------------------------------------------------------------------------------


def sizeof(obj):
    return sum(map(sys.getsizeof, explore(obj, set())))

# ----------------------------------------------------------------------------------------------------------------------


def explore(obj, memo):
    loc = id(obj)

    if loc not in memo:
        memo.add(loc)
        yield obj

        try:
            slots = obj.__slots__
        except AttributeError:
            pass
        else:
            for name in slots:
                try:
                    attr = getattr(obj, name)
                except AttributeError:
                    pass
                else:
                    yield from explore(attr, memo)

        try:
            attrs = obj.__dict__
        except AttributeError:
            pass
        else:
            yield from explore(attrs, memo)

        for name in 'keys', 'values', '__iter__':
            try:
                attr = getattr(obj, name)
            except AttributeError:
                pass
            else:
                for item in attr():
                    yield from explore(item, memo)

# ----------------------------------------------------------------------------------------------------------------------




