import requests
import time
import os
import threading
from multiprocessing import Process, Pool
import asyncio
import aiohttp



"""Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные файлы.
� Используйте потоки. """
def task1(urls):
    start_time = time.time()
    for url in urls:
        response = requests.get(url)
        filename = 'sync_' + url.replace('https://', '').replace('.',
    '_').replace('/', '') + '.html'
        with open(os.path.join('./upload/', filename), "w", encoding='utf-8') as f:
            f.write(response.text)
            print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

def download(url):
    start_time = time.time()
    response = requests.get(url)
    filename = 'threading_' + url.replace('https://',
                                          '').replace('.', '_').replace('/', '') + '.html'
    with open(os.path.join('./upload/', filename), "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

def download_p(url):
    start_time = time.time()
    response = requests.get(url)
    filename = 'multiprocessing_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(os.path.join('./upload/', filename), "w", encoding='utf-8') as f:
        f.write(response.text)
        print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")

async def download_a(url):
    start_time = time.time()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            text = await response.text()
            filename = 'asyncio_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(filename, "w", encoding='utf-8') as f:
                f.write(text)
                print(f"Downloaded {url} in {time.time() - start_time:.2f} seconds")


def task1_1(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download, args=[url])
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


"""
Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
� После загрузки данных нужно записать их в отдельные файлы.
� Используйте процессы.
"""
def task2(urls):
    processes = []

    for url in urls:
        process = Process(target=download_p, args=(url,))
        processes.append(process)
        process.start()
    for process in processes:
        process.join()

"""
Написать программу, которая считывает список из 10 URLадресов и одновременно загружает данные с каждого
адреса.
После загрузки данных нужно записать их в отдельные файлы.
Используйте асинхронный подход.
"""
def task3():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_a())

def main():
    urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://mail.ru',
        'https://vk.ru',
        'https://rbc.ru',
        'https://rambler.ru',
        'https://wikipedia.org'    ]

    #task1(urls)
    #task1_1(urls)
    task2(urls)

async def main_a():
    urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/',
        'https://mail.ru',
        'https://vk.ru',
        'https://rbc.ru',
        'https://rambler.ru',
        'https://wikipedia.org'    ]
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_a(url))
        tasks.append(task)
    await asyncio.gather(*tasks)




if __name__ == '__main__':
    task3()



