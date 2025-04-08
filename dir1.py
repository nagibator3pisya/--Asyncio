import asyncio


async def first_function(x):
    print(f"Выполняется первая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 1
    print(f"Первая функция завершилась с результатом {result}")
    return result


async def second_function(x):
    print(f"Выполняется вторая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x * 2
    print(f"Вторая функция завершилась с результатом {result}")
    return result


async def third_function(x):
    print(f"Выполняется третья функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x + 3
    print(f"Третья функция завершилась с результатом {result}")
    return result

async def fourth_function(x):
    print(f"Выполняется четвертая функция с аргументом {x}")
    await asyncio.sleep(1)
    result = x ** 2
    print(f"Четвертая функция завершилась с результатом {result}")
    return result

async def main():
    print("Начало цепочки асинхронных вызовов")
    # task = asyncio.create_task(first_function(1))
    # await task
    # task = asyncio.create_task(second_function(task.result()))
    # await task
    # task = asyncio.create_task(third_function(task.result()))
    # await task
    # final_result = asyncio.create_task(fourth_function(task.result()))
    # await final_result
    # print(f"Конечный результат цепочки вызовов: {final_result.result()}")

    # второй вариант
    result1 = await first_function(1)
    result2 = await second_function(result1)
    result3 = await third_function(result2)
    final_result  = await fourth_function(result3)
    print(f"Конечный результат цепочки вызовов: {final_result}")
if __name__ == '__main__':
    asyncio.run(main())


