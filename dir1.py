import asyncio
# await может возвращать результат

# async def coro():
#     await asyncio.sleep(1)
#     return 'Задача завершена'
#
# async def main():
#     result = await coro()
#     print(result)

async def coro(num):
    print('Начало',num)
    await asyncio.sleep(1)
    return f'Задача завершена {num}'

async def main():
    task = [asyncio.create_task(coro(i) )for i in range(1,6)]
    result = await asyncio.gather(*task)
    print(result)
if __name__ == '__main__':
    asyncio.run(main())

