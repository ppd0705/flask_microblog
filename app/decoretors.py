from threading import Thread
from functools import wraps


def async(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        thr = Thread(target=func, args=args, kwargs=kwargs)
        thr.start()

    return wrapper
