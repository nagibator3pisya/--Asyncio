# Первый вход в асинхронное
import time
import asyncio
# async = обозначает что функция выполняется асинхронно
# await ставиться перед вызовом асинхр фукнции -  это ключевое слово,
# которое используется внутри
# асинхронной функции для ожидания результата другой асинхронной операции
# Корутины (coroutines), или сопрограммы — это блоки кода, которые работают асинхронно
# create_task() - для создания

async def fun1(x):
    print(x**2)
    await asyncio.sleep(3)
    print("fun1 finich")


async def fun2(x):
    print(x**0.5)
    await asyncio.sleep(3)
    print("fun2 finich")





async def main():
    task1 = asyncio.create_task(fun1(4))
    task2 = asyncio.create_task(fun2(4))

    await task1
    await task2

    print(type(task1))
    print(task1.__class__.__bases__)

asyncio.run(main())