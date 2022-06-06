import time


def print_execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time}")
        return res

    return wrapper


def print_execution_time_wrapper(func, *args, **kwargs):
    start_time = time.time()
    res = func(*args, **kwargs)
    end_time = time.time()
    print(f"Execution time: {end_time - start_time}")
    return res


@print_execution_time_decorator
def calc_add(x: int, y: int) -> int:
    time.sleep(3)
    return x + y


if __name__ == '__main__':
    # calc_add(4,5) # Works
    print_execution_time_wrapper(time.sleep, 3)  # Works
