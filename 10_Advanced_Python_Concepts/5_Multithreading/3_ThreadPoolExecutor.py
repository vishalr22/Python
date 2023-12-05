import time
from concurrent.futures import ThreadPoolExecutor


# Indicates some task being done
def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds


def poolingDemo():
    time1 = time.perf_counter()
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 4)
        print(future1.result())
        print(future2.result())
        print(future3.result())

        print("!__________Another Method_______________!")

        seconds_list = [3, 5, 1, 2]
        results = executor.map(func, seconds_list)
        for result in results:
            print(result)
    time2 = time.perf_counter()
    print("Total Time taken for the process to complete", time2 - time1)


poolingDemo()
