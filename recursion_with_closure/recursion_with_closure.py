import logging as log
import sys
import time

log.basicConfig(format='%(asctime)s.%(msecs)03d[%(levelname)s] %(message)s',
                datefmt='%Y/%m/%d %H:%M:%S',
                level=log.INFO,
                handlers=[
                    log.StreamHandler(sys.stdout),
                ])


# <editor-fold desc="Timeit Decorator">
def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        if 'log_time' in kw:
            name = kw.get('log_name', method.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            log.info(f"Func = '{method.__name__}' Time: {(te - ts) * 1000:.2f} ms")
        return result
    return timed
# </editor-fold>

# <editor-fold desc="Fib Closure">
def fib():
    x1 = 0
    x2 = 1

    def get_next_number():
        nonlocal x1, x2
        x1, x2 = x2, x1 + x2
        return x2

    return get_next_number


def fib_closure(n):
    f = fib()
    for i in range(2, n + 1):
        num = f()
    return num


# </editor-fold>

# <editor-fold desc="Fib Recursion">
def fib_recursion(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursion(n - 1) + fib_recursion(n - 2)


# </editor-fold>
@timeit
def apply_fib_closure(n: int):
    log.info(f"Fig({n}) = {fib_closure(n):,}")

@timeit
def apply_fib_recursion(n: int):
    log.info(f"Fig({n}) = {fib_recursion(n):,}")


if __name__ == '__main__':
    apply_fib_closure(n=20)
    apply_fib_recursion(n=20)
