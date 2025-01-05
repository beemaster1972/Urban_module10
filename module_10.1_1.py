from fileinput import filename
from multiprocessing import Pool
from time import sleep, time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line:
            line = file.readline()
            all_data.append(line.strip())


if __name__ == '__main__':
    filenames = [f'./file {_}.txt' for _ in range(1, 5)]
    # Line
    start = time()
    for filename in filenames:
        read_info(filename)
    finish = time()
    print(finish - start,'(Line)')
    #Multiprocessing
    start = time()
    with Pool(4) as pool:
        result = pool.map(read_info, filenames)
    finish = time()
    print(finish - start,'(Multiprocessing)')
