import asyncio


# async def ex_cor():
#     await asyncio.sleep(1)
#     print('Корутина')
#
#
# async def main():
#     for i in range(10):
#         await ex_cor() # запускается и ждем выполнения
#
# asyncio.run(main())# точка входа


# async def cor_1():
#     print('coro_1 says')
#     await asyncio.sleep(2)
#     print('hello coro_2')
#
#
# async def cor_2():
#     print('coro_2 says')
#     await asyncio.sleep(2)
#     print('hello coro_1')
#
#
# async def main():
#     await cor_1()
#     await cor_2()
#
#
# asyncio.run(main())



# async def generate(n):
#     await asyncio.sleep(0.1)
#     print(f"Корутина generate с аргументом {n}")
#
#
# async def main():
#     for i in range(0,10):
#         await generate(i)
#
# asyncio.run(main())

async def coro_1():
    print("Вызываю корутину 0")


async def coro_5():
    print("Вызываю корутину 3")
    await coro_3()


async def coro_3():
    print("Вызываю корутину 2")
    await coro_2()


async def coro_4():
    print("Вызываю корутину 1")
    await coro_1()


async def coro_2():
    print("Вызываю корутину 4")
    await coro_4()
'''
Вызываю корутину 3
Вызываю корутину 2
Вызываю корутину 4
Вызываю корутину 1
Вызываю корутину 0
'''
async def main():
    await coro_5()

asyncio.run(main())