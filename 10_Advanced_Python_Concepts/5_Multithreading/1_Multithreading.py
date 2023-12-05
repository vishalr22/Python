'''
Multithreading is a technique in programming that allows multiple threads of execution to run concurrently within a single process.
It allows you to take advantage of multiple CPU cores and process tasks in parallel.

To create a thread, we need to create a Thread object and then call its start() method to runs the thread and then to stop the execution, we use the join() method.

Following are some of the most commonly used functions in the threading module:
1. threading.Thread(target, args): This function creates a new thread that runs the target function with the specified arguments.
2. thread.start(): This function starts the thread.
3. thread.join(): This function stops the thread.
'''
import threading


# Creating Single Thread
def my_func():
    print("Hello from thread", threading.current_thread().name)


# Creating Multiple Thread
def thread_task(task):
    # Do some work here
    print("Task processed:", task)


if __name__ == '__main__':
    thread = threading.Thread(target=my_func)  # Creating a thread
    thread.start()  # It runs the thread
    thread.join()  # It stops the thread

    tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    threads = []
    for task in tasks:
        thread = threading.Thread(target=thread_task, args=(task,))  # Creating a thread
        threads.append(thread)
        # thread.start()

    for thread in threads:
        thread.start()  # It runs the thread
        thread.join()  # It stops the thread
