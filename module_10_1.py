from time import sleep, time, localtime, strftime
import threading


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for _ in range(1, word_count + 1):
            f.write(f'Какое-то слово № {_}' + '\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


if __name__ == '__main__':
    start = time()
    write_words(10, 'example1.txt')
    write_words(30, 'example2.txt')
    write_words(200, 'example3.txt')
    write_words(100, 'example4.txt')
    finish = time()
    print(f'Работа потоков {strftime("0:%M:%S", localtime(finish - start))}')
    start = time()
    threads = [threading.Thread(target=write_words, args=(word_count[0], f'example{word_count[1]}.txt')) for word_count
               in [(10, 5), (30, 6), (200, 7), (100, 8)]]
    for thread in threads:
        thread.start()

    threads_running = True
    while threads_running:
        threads_running = False
        for thread in threads:
            threads_running = threads_running or thread.is_alive()

    finish = time()
    print(f'Работа потоков {strftime("0:%M:%S", localtime(finish - start))}')
