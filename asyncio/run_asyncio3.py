import asyncio
import time

def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(myWork())
    finally:
        loop.close()


async def myWork():
    print("Starting Work")
    time.sleep(5)
    print("Finishing Work")


if __name__ == '__main__':
    main()

