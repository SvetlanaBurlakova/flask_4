"""
Создать программу, которая будет производить подсчет количества слов в каждом файле в указанной директории и
выводить результаты в консоль. � Используйте потоки.

"""
import threading
from pathlib import Path
import time
from multiprocessing import Process, Pool
import asyncio

def count(file, start_time):
    with open(file, "r", encoding='utf-8') as f:
        result = f.read().split()
        print(f"Number of words in {file.name} is {len(result)} counted in {time.time() - start_time:.2f} seconds")

async def count_a(file, start_time):
    with open(file, "r", encoding='utf-8') as f:
        result = f.read().split()
        print(f"Number of words in {file.name} is {len(result)} counted in {time.time() - start_time:.2f} seconds")


def task4(path: Path):
    files = [file for file in path.iterdir() if file.is_file()]
    start_time = time.time()
    threads = []
    for file in files:
        thread = threading.Thread(target=count, args=[file, start_time])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

def task4_p(path: Path):
    files = [file for file in path.iterdir() if file.is_file()]
    start_time = time.time()
    processes = []
    for file in files:
        process = Process(target=count, args=[file, start_time])
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

def task4_p(path: Path):
    files = [file for file in path.iterdir() if file.is_file()]
    start_time = time.time()
    processes = []
    for file in files:
        process = Process(target=count, args=[file, start_time])
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

async def task4_a(path):
    files = [file for file in path.iterdir() if file.is_file()]
    start_time = time.time()
    tasks = []
    for file in files:
        task = asyncio.ensure_future(count_a(file, start_time))
        tasks.append(task)
    await asyncio.gather(*tasks)



def main():
    path = Path(Path.cwd()/'upload')
    task4(path) #потоки
    task4_p(path)  #процессы


async def main_a():
    path = Path(Path.cwd() / 'upload')
    task4_a(path)


if __name__ == '__main__':
    #main()
    path = Path(Path.cwd() / 'upload')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task4_a(path))