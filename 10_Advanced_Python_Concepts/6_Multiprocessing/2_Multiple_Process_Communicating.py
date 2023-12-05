'''
When working with multiple processes, it is often necessary to pass data between them.
One way to do this is by using a queue. A queue is a data structure that allows data to be inserted at one end and removed from the other end.
In the context of multiprocessing, a queue can be used to pass data between processes.
'''
import multiprocessing


# Using a queue to communicate between processes
def producer(queue):
    for i in range(10):
        queue.put(i)


def consumer(queue):
    while True:
        item = queue.get()
        print(item)


if __name__ == "__main__":
    queue = multiprocessing.Queue()
    p1 = multiprocessing.Process(target=producer, args=(queue,))
    p2 = multiprocessing.Process(target=consumer, args=(queue,))
    p1.start()
    p2.start()
