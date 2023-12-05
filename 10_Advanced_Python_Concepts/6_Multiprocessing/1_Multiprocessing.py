'''
Multiprocessing is a Python module that provides a simple way to run multiple processes in parallel.
It allows you to take advantage of multiple cores or processors on your system and can significantly improve the performance of your code.

To use multiprocessing we need to create a process object which calls a start() method.
The start() method runs the process and then to stop the execution, we use the join() method.

Some of the most commonly used functions in the multiprocessing module are:
1. multiprocessing.Process(target, args): This function creates a new process that runs the target function with the specified arguments.
2. multiprocessing.Pool(processes): This function creates a pool of worker processes that can be used to parallelize the execution of a function across multiple input values.
3. multiprocessing.Queue(): This function creates a queue that can be used to communicate data between processes.
4. multiprocessing.Lock(): This function creates a lock that can be used to synchronize access to shared resources between processes.
'''
import multiprocessing
from multiprocessing import Pool


# Creating Single Process
def my_func():
    print("Hello from process", multiprocessing.current_process().name)


# Creating a pool of worker processes (Multiple Process)
def process_task(task):
    # Do some work here
    print("Task processed:", task)


if __name__ == "__main__":
    process = multiprocessing.Process(target=my_func)  # Create the process
    process.start()
    process.join()

    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    with Pool(processes=10) as pool:
        results = pool.map(process_task, tasks)
