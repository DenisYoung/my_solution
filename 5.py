import os
import time
import multiprocessing
def task1(current_dir):
    # в папке test найти все файлы filenames вывести количество
    count = 0
    for directory, _, files in os.walk(current_dir):
        for file_name in files:
            if "filename" in file_name:
                count += 1
    print(f"Кол-во файлов которые содержат 'filenames' в названии: {count}")



def task2(current_dir):
    # в папке test найти все email адреса записанные в файлы
    count = 0
    for directory, _, files in os.walk(current_dir+f'\{""}test'):
        for file_name in files:
            with open(os.path.join(directory, file_name), "r", encoding='ISO-8859-1') as file:
                for word in file.read().split():
                    if "@" in word and "." in word:
                        count += 1
    print(f"Кол-во email адресов записанных в файлы: {count}")


def finder(paths):
    count = 0
    with open(paths, "r", encoding='ISO-8859-1') as file:
        for word in file.read().split():
            if "@" in word and "." in word:
                count += 1
    return count
                


def processesed(current_dir):
    file_paths = []
    for directory, _, files in os.walk(current_dir+f'\{""}test'):
        for file_name in files:
            file_paths.append(os.path.join(directory, file_name))

    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    email_counts = pool.map(finder, file_paths)
    pool.close()
    pool.join()

    count = sum(email_counts)
    print(f"Кол-во email адресов записанных в файлы: {count}")



def main():
    current_dir = os.getcwd()
    task1(current_dir)

    start = time.time()
    task2(current_dir)
    end = time.time()
    print(f"Время выполнения программы: {end-start} секунд")
    # дополнительно: придумать над механизмом оптимизации 2-й задачи (параллелизация)

    start = time.time()
    processesed(current_dir)
    end = time.time()
    print(f"Время выполнения программы: {end-start} секунд")


if __name__ == '__main__':
    main()
