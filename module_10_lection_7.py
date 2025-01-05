from threading import Thread, Event
from time import sleep


def first_worker():
    print('First worker start his task')
    event.wait()
    print('First worker continue his task')
    sleep(5)
    print('First worker finish his task')


def second_worker():
    print('Second worker start his task')
    sleep(10)
    print('Second worker finish his task')
    event.set()


if __name__ == '__main__':
    event = Event()
    thread_1 = Thread(target=first_worker)
    thread_2 = Thread(target=second_worker)
    thread_1.start()
    thread_2.start()
    event.wait(timeout=15)