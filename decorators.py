def fabric_decorators(arg_decorator):
    def decorator(fn):
        def wrapper(*args, **kwargs):
            return fn(*args, **kwargs)
        return wrapper
    return decorator


@fabric_decorators(123)   # fabric_decorators(123) -> decorator(test_1) -> wrapper(123)
def test_1(arg1):
    return arg1


if __name__ == '__main__':
    test_1(5)
