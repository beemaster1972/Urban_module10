import multiprocessing
from time import sleep
from threading import Thread


counter = 0


def first_worker(n):
    global counter
    for _ in range(n):
        sleep(1)
        counter += 1
        print(counter)

    print(f'First worker finish his task {counter}')


def second_worker(n):
    global counter
    for _ in range(n):
        sleep(1)
        counter += 1
        print(counter)

    print(f'Second worker finish his task {counter}')


if __name__ == '__main__':
    process1 = multiprocessing.Process(target=first_worker, args=(10,))
    process2 = multiprocessing.Process(target=second_worker, args=(5,))
    process1.start()
    process2.start()
    # thread_1 = Thread(target=first_worker, args=(10,))
    # thread_2 = Thread(target=second_worker, args=(5,))
    # thread_1.start()
    # thread_2.start()