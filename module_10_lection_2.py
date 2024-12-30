import threading
import time


class MyThread(threading.Thread):

    def __init__(self, name, counter, delay=1):
        threading.Thread.__init__(self)
        self.name = name
        self.counter = counter
        self.delay = delay

    def timer(self, name, counter, delay):
        while counter:
            time.sleep(delay)
            print(f'{name} {time.ctime(time.time())}')
            counter -= 1

    def run(self):
        print(f'Поток {self.name} запущен')
        self.timer(self.name, self.counter, self.delay)
        print(f'Поток {self.name} завершен')


if __name__ == '__main__':
    thread1 = MyThread('thread1', 5)
    thread2 = MyThread('thread2', 2)
    thread1.start()
    thread2.start()
