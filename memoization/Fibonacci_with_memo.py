import functools
import timeit
import time


def main():
    index = 10
    print(f"Fibonacci {index}: {calc_fib(index=index)}")


@functools.lru_cache(maxsize=128)
def calc_fib(index):
    print(f"Calculating Fib of {index}")
    if index in [1, 2]:
        return 1
    else:
        return calc_fib(index - 1) + calc_fib(index - 2)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(f"Time: {(end - start) * 1000.0} seconds!")
