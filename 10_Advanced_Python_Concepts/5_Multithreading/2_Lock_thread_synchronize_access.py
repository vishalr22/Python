'''
When working with multithreading in python, locks can be used to synchronize access to shared resources among multiple threads.
A lock is an object that acts as a semaphore, allowing only one thread at a time to execute a critical section of code.
The lock is released when the thread finishes executing the critical section.

threading.Lock(): This function creates a lock that can be used to synchronize access to shared resources between threads.
'''
import threading


# Using a lock to synchronize access to shared resources
def increment(counter, lock):
    for i in range(10000):
        lock.acquire()
        counter += 1
        lock.release()


if __name__ == '__main__':
    counter = 0
    lock = threading.Lock()

    threads = []
    for i in range(2):
        thread = threading.Thread(target=increment, args=(counter, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("Counter value:", counter)
