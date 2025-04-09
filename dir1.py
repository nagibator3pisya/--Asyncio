import asyncio
import time
# использование await с корутиной

async def coro(num,second):
    print(f'coro {num}, начало свое выполнение')
    await asyncio.sleep(second)
    print(f'coro {num} выполнена за {second} секунд(ы)')


async def main():
    # создание объектов корутин путем вызова корутинной функции
    coro1 = coro(1,2)
    coro2 = coro(2,1)
    # запуск и ожидание выполнения объектов корутин
    await coro1
    await coro2

start = time.time()
asyncio.run(main())

print(f'ПРОГРАММА ВЫПОЛНЕНА ЗА {time.time() - start:.3f}')

# Использование корутин с использованием Task

async def coro(num,second):
    print(f'coro {num}, начало свое выполнение')
    await asyncio.sleep(second)
    print(f'coro {num} выполнена за {second} секунд(ы)')


async def main():
    # создание объектов корутин путем вызова корутинной функции
    task1 = asyncio.create_task(coro(1,2))
    task2 = asyncio.create_task(coro(2, 1))
    # запуск и ожидание выполнения объектов корутин
    await task1
    await task2


start = time.time()
asyncio.run(main())

print(f'ПРОГРАММА ВЫПОЛНЕНА ЗА {time.time() - start:.3f}')
