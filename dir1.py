import asyncio

# Использование результатов выполнения корутин.
async  def do_some_work_1(x, future:asyncio.Future):
    print(f'Выполняется работа 1: {x}')
    await asyncio.sleep(x)
    future.set_result(x * 2)


async  def do_some_work_2(x, future:asyncio.Future):
    print(f'Выполняется работа 2: {x}')
    await asyncio.sleep(x)
    future.set_result(x + 2)

async def main():
    # Обьекты для future для каждой задачи
    # И для получения результата в дальнейшем
    future_1 = asyncio.Future()
    future_2 = asyncio.Future()

    # Запус первой задачи и передаем ей Future
    asyncio.create_task(do_some_work_1(2, future_1))
    # Дожидаемся завершинеия первой задачи
    await future_1
    result_1 = future_1.result()

    # Запус второй задачи и передаем ей результат первой и обьект future
    asyncio.create_task(do_some_work_2(result_1,future_2))
    # Дожидаемся завершинеия первой задачи
    await future_2
    result_2 = future_2.result()

    print(f'Результат future_1: {result_1}')
    print(f'Результат future_2: {result_2}')

asyncio.run(main())

















