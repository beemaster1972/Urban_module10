from queue import Queue
from threading import Thread, current_thread
from time import sleep


def getter(queue):
    while True:
        sleep(5)
        item = queue.get()
        print(f'{current_thread()} get element {item}')


q = Queue(maxsize=10)
thread1 = Thread(target=getter, args=(q,), daemon=True)
thread1.start()

for _ in range(10):
    sleep(2)
    q.put(_)
    print(current_thread(), 'put in queue element', _)
