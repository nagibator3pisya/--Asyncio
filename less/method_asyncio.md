# Методы asyncio
#методы
asyncio.wait_for() — функция ожидает завершения одного awaitable объекта, позволяет устанавливать timeout на время ожидания и, если выполнение не завершено в течение timeout секунд, вызывается TimeoutError.
```python
import  asyncio
async def long_running_task():
    await asyncio.sleep(5)
    return 'Задача выполнена'


async def main():
    try:
        result = await asyncio.wait_for(long_running_task(),timeout=6)
        print(result)
    except asyncio.TimeoutError:
        print('Время вышло')

asyncio.run(main())
'''
Задача выполнена
'''
```

**asyncio.wait()**
Этот метод позволяет запустить несколько задач и дождаться их выполнения. Он возвращает два множества: завершенные и не завершенные задачи.
```python
'''
asyncio.wait()
Этот метод позволяет запустить несколько задач и дождаться их выполнения. 
Он возвращает два множества: завершенные и не завершенные задачи.
get_name()- проверить какие задачи ожидаются
'''
import asyncio
async def task1():
    await asyncio.sleep(2)
    return "Task 1 completed"

async def task2():
    await asyncio.sleep(4)
    return "Task 2 completed"


async def main():
    tasks_1 = asyncio.create_task(task1())
    tasks_2 = asyncio.create_task(task2())
    lists = [tasks_1,tasks_2]
    done, pending = await asyncio.wait(lists, timeout=3)

    for task in done:
        print(f"Выполнились задачи: {task.result()}")

    for task in pending:
        print(f"Ожидается задача: {task.get_name()}")

asyncio.run(main())
"""
Выполнились задачи: Task 1 completed
Ожидается задача: Task-3
"""
```
# asyncio.shield()

```python


```