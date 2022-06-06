import asyncio
from datetime import time

# NOT WORKING!!!!!!!


async def main():
    print("Waiting 5 seconds. ")
    for _ in range(5):
        await asyncio.sleep(1)
    print("Finished waiting.")


async def my_task():
    await sleep_sec(5)
    return 'Banana!'


async def sleep_sec(sleep_time_sec):
    print(f"Sleeping {sleep_time_sec} seconds!")
    time.sleep(sleep_time_sec)


if __name__ == '__main__':
    task = asyncio.create_task(my_task())
    print(task)
    # asyncio.run(main())
