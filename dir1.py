import asyncio

# Создание обьекта future
future = asyncio.Future()


# async def exmple_task():
#     return 'Задача выполнена'
#
#
#
# async  def main():
#     task = asyncio.create_task(exmple_task()) # создание задачи из корутины example_task()
#     await task  # запуск задачи и ожидание выполнения
#     result = task.result()  # сохранение результата в переменную result
#     print(result)
#
#
# asyncio.run(main())

# Установка результата для объектов Future. Метод set_result()


async  def simulate_long_running_task(name, dalay, future: asyncio.Future):
    print(f'Задача {name} началась, будет выполнена за {dalay} сек')
    await asyncio.sleep(dalay)
    result = f'Результат задачи {name}'
    print(f'Задача {name}, завершина')
    future.set_result(result) # УСТАНАВЛИВАЕМ результат для Future объекта


async def main():
    # объект футуры
    future = asyncio.Future()
    # запускаем корутину , передаем future объект в функцию
    await simulate_long_running_task('Задача 1',3,future)
    result = future.result()
    print(f'Результат Future: {result}')

asyncio.run(main())




