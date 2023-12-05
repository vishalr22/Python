'''
When working with multiprocessing in python, locks can be used to synchronize access to shared resources among multiple processes.
A lock is an object that acts as a semaphore, allowing only one process at a time to execute a critical section of code.
The lock is released when the process finishes executing the critical section.
'''
import multiprocessing


# Using a lock to synchronize access to shared resources
def increment(counter, lock):
    for i in range(10000):
        lock.acquire()
        counter.value += 1
        lock.release()


if __name__ == '__main__':
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()

    p1 = multiprocessing.Process(target=increment, args=(counter, lock))
    p2 = multiprocessing.Process(target=increment, args=(counter, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Counter value:", counter.value)
