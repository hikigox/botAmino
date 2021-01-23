from threading import Thread
from queue import Queue
import time


def thread1(threadname, q):
    b = False
    # read variable "a" modify by thread 2
    while True:
        a = q.get()
        if a:  # Poison pill
            print("Se hizo la pregunta", a)
            q.put(False)

        else:
            print("other")


def thread2(threadname, q):
    a = False
    while True:
        print("Hago pregunta")
        a = True
        q.put(a)
        time.sleep(5)
        a = False
        q.put(a)


queue = Queue()
thread1 = Thread(target=thread1, args=("Thread-1", queue))
thread2 = Thread(target=thread2, args=("Thread-2", queue))

thread1.start()
thread2.start()

print("goa")
