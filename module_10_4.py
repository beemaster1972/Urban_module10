from queue import Queue, LifoQueue
from random import randint
from threading import Thread
from time import sleep


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        sleep(randint(3,10))


class Cafe:

    def __init__(self, *args, **kwargs):
        self.tables = {table.number:table for table in args if isinstance(table,Table)}
        self.tables_number = len(self.tables)
        self.empty_tables = Queue(self.tables_number)
        for table_number in self.tables.keys():
            self.empty_tables.put(table_number)
        self.queue = Queue()

    def guest_arrival(self,*guests):
        for guest in guests:
            if not isinstance(guest,Guest):
                continue
            if self.empty_tables.empty():
                self.queue.put(guest)
                print(f'{guest.name} в очереди')
                continue
            empty_table = self.empty_tables.get()
            self.tables[empty_table].guest = guest
            print(f'{guest.name} сел(-а) за стол номер {empty_table}')
            print(f'{self.empty_tables.qsize()} свободных столов осталось')
            guest.start()

    def discuss_guests(self):
        while not self.queue.empty() or self.empty_tables.qsize()<self.tables_number:
            for table_number, table in self.tables.items():
                if table.guest is None:
                    if not self.queue.empty():
                        guest = self.queue.get()
                        self.tables[table_number].guest = guest
                        guest.start()
                        print(f'{guest.name} сел(-а) за стол номер {table_number}')
                        print(f'{self.empty_tables.qsize()} свободных столов осталось')
                    else:
                        break
                    continue
                if not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table_number} свободен")
                    self.tables[table_number].guest = None
                    self.empty_tables.put(table_number)
            else:
                break



if __name__ == '__main__':
    tables = [Table(number) for number in range(1, 6)]
    # Имена гостей
    guests_names = [
        'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
        'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
    ]
    # Создание гостей
    guests = [Guest(name) for name in guests_names]
    # Заполнение кафе столами
    cafe = Cafe(*tables)
    # print(cafe.empty_tables.qsize())
    cafe.guest_arrival(*guests)
    # print(cafe.empty_tables.qsize())
    cafe.discuss_guests()