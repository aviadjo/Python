import sys
import time
import random

from joblib import Parallel, delayed
from multiprocessing import pool, Pool
import logging as log

log.basicConfig(format='%(asctime)s [%(module)s] [%(threadName)s] [%(levelname)s] %(message)s',
                datefmt='%Y/%m/%d %H:%M:%S',
                level=log.INFO,
                handlers=[
                    log.StreamHandler(sys.stdout),
                ])

THREADS_NUM = 10
DELEY_MAX_SEC = 10


def run_regular(my_list: list):
    log.info(f"{'*' * 20}\nRegular processing{'*' * 20}")
    for i, element in enumerate(my_list, start=1):
        process_element(element)


def run_parallel_using_joblib(my_list: list):
    log.info(f"{'*' * 20}\nParallel processing{'*' * 20}")
    results = Parallel(
        n_jobs=THREADS_NUM,
        verbose=10,
        prefer='threads'
    )(delayed(process_element)(
        index=i,
        total=len(my_list),
        element=x
    ) for i, x in enumerate(my_list, start=1))
    log.info(f"Results: {results}")

def run_parallel_using_joblib2(my_list: list):
    log.info(f"{'*' * 20}\nParallel processing{'*' * 20}")
    results = Parallel(
        n_jobs=THREADS_NUM,
        verbose=10,
        prefer='threads'
    )(delayed(process_return_2_elements)(
        index=i,
        total=len(my_list),
        element=x
    ) for i, x in enumerate(my_list, start=1))

    x,y = zip(*results)

    log.info(f"Results: {results}")


def process_element(index: int, total: int, element: int) -> int:
    iteration_id = f"{index}/{total}"
    log.info(f"({iteration_id}) Started processing element: {element}")
    sleep_time_sec = random.randrange(0, DELEY_MAX_SEC)
    time.sleep(sleep_time_sec)
    log.info(f"({iteration_id}) Finished processing element: {element}")
    # if random.uniform(0, 1) > 0.5:
    return element ** 2

def process_return_2_elements(index: int, total: int, element: int) -> (int, int):
    iteration_id = f"{index}/{total}"
    log.info(f"({iteration_id}) Started processing element: {element}")
    sleep_time_sec = random.randrange(0, DELEY_MAX_SEC)
    time.sleep(sleep_time_sec)
    log.info(f"({iteration_id}) Finished processing element: {element}")
    # if random.uniform(0, 1) > 0.5:
    return element ** 2, element**3


def run_parallel_using_pool(my_list: list):
    pool = Pool(THREADS_NUM)
    results = pool.map(process_element,
                       my_list)
    log.info(f"Results: {results}")


if __name__ == '__main__':
    my_list = list(range(10))
    # run_regular(my_list)
    # log.info(f"{'#'*20}")
    run_parallel_using_joblib(my_list)
    # run_parallel_using_pool(my_list)
