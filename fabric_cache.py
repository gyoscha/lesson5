import time
from collections import OrderedDict
from functools import lru_cache


def cache(maxsize=3):
    def decorator(fn):
        dict_cache = OrderedDict()

        def wrapper(*args):
            if args not in dict_cache:
                if len(dict_cache) == maxsize:
                    dict_cache.popitem(last=False)
                result = fn(*args)
                dict_cache[args] = result

            return dict_cache[args]
        return wrapper
    return decorator


@cache(3)
def my_sleep():
    time.sleep(3)


@lru_cache(maxsize=None)   # Это тоже самое, что и @cache. Просто готовое решение, которое не нужно писать.
def my_sleep_1():
    time.sleep(3)


if __name__ == '__main__':
    t0 = time.time()

    print(my_sleep())
    print(my_sleep())

    print(time.time() - t0)
