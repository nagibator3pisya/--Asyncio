import asyncio
# методы asyncio

# asyncio.wait_for

"""
Этот метод позволяет установить тайм-аут на выполнение асинхронной задачи. 
Если задача не завершится в указанное время, будет выброшено исключение TimeoutError.
"""

# async def long_running_task():
#     await asyncio.sleep(5)
#     return 'Задача выполнена'
#
#
# async def main():
#     try:
#         result = await asyncio.wait_for(long_running_task(),timeout=6)
#         print(result)
#     except asyncio.TimeoutError:
#         print('Время вышло')
#
# asyncio.run(main())

# '''
# asyncio.wait()
# Этот метод позволяет запустить несколько задач и дождаться их выполнения.
# Он возвращает два множества: завершенные и не завершенные задачи.
# get_name()- проверить какие задачи ожидаются
# '''
# async def task1():
#     await asyncio.sleep(2)
#     return "Task 1 completed"
#
# async def task2():
#     await asyncio.sleep(4)
#     return "Task 2 completed"
# async def task3():
#     await asyncio.sleep(10)
#     return "Task 3 completed"
#
# async def main():
#     tasks_1 = asyncio.create_task(task1())
#     tasks_2 = asyncio.create_task(task2())
#     lists = [tasks_1,tasks_2]
#     done, pending = await asyncio.wait(lists, timeout=3)
#
#     for task in done:
#         print(f"Выполнились задачи: {task.result()}")
#
#     for task in pending:
#         print(f"Ожидается задача: {task.get_name()}")
#
# asyncio.run(main())
# """
# Выполнились задачи: Task 1 completed
# Ожидается задача: Task-3
# """

# asyncio.shield()
async def protected_task():
    try:
        await asyncio.sleep(5)
        print('Задание выполнено')
    except asyncio.CancelledError:
        print('Задача отменена')
        raise

async  def main():
    task = asyncio.create_task(protected_task())
    shilded_task = asyncio.shield(task)
    await  asyncio.sleep(2)
    shilded_task.cancel() # попытка отменить защищенную задачу

    try:
        await shilded_task
    except asyncio.CancelledError:
        print('Основная задача была отменена, но защищенная задача продолжается')
    await task

asyncio.run(main(),debug=True)