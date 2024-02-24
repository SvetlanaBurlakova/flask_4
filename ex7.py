"""
Напишите программу на Python, которая будет находить сумму элементов массива из 1000000 целых чисел.
� Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
� Массив должен быть заполнен случайными целыми числами от 1 до 100.
� При решении задачи нужно использовать многопоточность, многопроцессорность и асинхронность.
� В каждом решении нужно вывести время выполнения вычислений.

"""
import random
import threading
from pathlib import Path
import time
from multiprocessing import Process, Value
import asyncio

summa = Value('i', 0)

def sum_arr(el):
    global summ
    summ += sum(el)
    return summ

def sum_arr_p(el, summa):
    with summa.get_lock():
        summa.value += sum(el)


async def sum_arr_a(el):
    global summ
    summ += sum(el)
    return summ

def task7(arr):
    start_time = time.time()
    threads = []
    size = 1000
    arr_s = [arr[i:i + size] for i in range(0, len(arr), size)]
    for el in arr_s:
        thread = threading.Thread(target=sum_arr, args=[el, ])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print(f'{summ} counted in threading method {time.time() - start_time:.2f} seconds')

def task7_p(arr):
    start_time = time.time()
    processes = []
    size = 1000
    arr_s = [arr[i:i + size] for i in range(0, len(arr), size)]
    for el in arr_s:
        process = Process(target=sum_arr_p, args=[el, summa])
        processes.append(process)
        process.start()
    for process in processes:
        process.join()
    print(f'{summa.value} counted in parallel method in {time.time() - start_time:.2f} seconds')

async def task7_a(arr):
    size = 1000
    arr_s = [arr[i:i + size] for i in range(0, len(arr), size)]
    tasks = []
    for el in arr_s:
        task = asyncio.ensure_future(sum_arr_a(el))
        tasks.append(task)
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()
    summ = 0
    arr = [random.randint(1, 100) for _ in range(100000)]
    print(f'{sum(arr)} counted in classic Python sum method {time.time() - start_time:.2f} seconds') #0.06 sec
    task7(arr) # 0.02 sec
    task7_p(arr) # 5.49 sec
    summ = 0
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(task7_a(arr))
    print(f'{summ} counted async method in {time.time() - start_time:.2f} seconds') # 0.00 sec