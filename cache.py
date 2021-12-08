import time


def cache(fn):
    dict_cache = {}

    def wrapper(*args):
        if args not in dict_cache:
            result = fn(*args)
            dict_cache[args] = result

        return dict_cache[args]
    return wrapper


@cache
def my_sleep():
    time.sleep(3)


if __name__ == '__main__':
    t0 = time.time()

    print(my_sleep())
    print(my_sleep())

    print(time.time() - t0)
