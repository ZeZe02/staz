
import time


def calculate_time(func):
    def inner1(*args, **kwargs):
        begin = time.time()

        result = func(*args, **kwargs)

        end = time.time()
        print("Total time taken in : ", func.__name__, end - begin)
        return result

    return inner1
