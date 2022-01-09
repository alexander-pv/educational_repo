import datetime as dt


def timeit(func):
    def timed(*args, **kw):
        t0 = dt.datetime.now()
        result = func(*args, **kw)
        t1 = dt.datetime.now()
        print(f"Execution time: {(t1 - t0).total_seconds()}s")
        return result

    return timed
