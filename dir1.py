import time
import asyncio

stast = time.time()


import asyncio
import time

start = time.time()  # Инициализация переменной start для измерения времени выполнения

async def sleeping(n):
    # Начало выполнения длительной операции
    print(f'Начало выполнения длительной операции № {n}: {time.time() - start:.4f}')

    # Приостановка выполнения функции на 1 секунду
    await asyncio.sleep(1)

    # Завершение длительной операции
    print(f'Длительная операция {n} завершена')

async def main():
    # Создание списка из 30 асинхронных задач
    tasks = [sleeping(i) for i in range(1, 6)]

    # Конкурентное выполнение всех задач из списка tasks
    # await asyncio.gather(*tasks) означает, что мы ждем завершения всех задач в списке
    # gather позволяет запускать несколько асинхронных задач одновременно и ждать их завершения
    all_result = await asyncio.gather(*tasks)

    # Вывод количества выполненных операций
    print(f'Выполнено {len(all_result)} операций')

    # Вывод общего времени выполнения программы
    print(f'Программа завершена за : {time.time() - start:.4f}')

# Запуск асинхронной функции main() в событийном цикле
asyncio.run(main())

# async def fetch_data():
#     print("Начинаем загрузку данных")
#     await asyncio.sleep(2)  # Имитация асинхронной операции ввода-вывода
#     print("Данные загружены")
#     return {'data': 123}
#
# async def main():
#     tasks = [fetch_data() for _ in range(5)]
#     results = await asyncio.gather(*tasks)
#     print(f"Загружено {len(results)} задач")
#
# asyncio.run(main())