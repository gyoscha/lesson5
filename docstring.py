from functools import wraps


def decorator(fn):
    @wraps(fn)   # чтобы не потерялась документация функций
    # wrapper.__name__ = fn.__name__
    # wrapper.__doc__ = fn.__doc__
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper


@decorator
def test(arg1, arg2):
    """
    Общее описание...

    Примеры кода...

    :param arg1: Описание параметра
    :param arg2:
    :return:
    """
    ...


@decorator
def test2(arg1, arg2):
    """ Краткое описание """
    ...


print(f'Я вызываюсь при импорте и выполении скрипта {__name__}')
if __name__ == '__main__':
    print(test.__name__)   # название
    print(test.__doc__)   # документация

    help(test)
