import asyncio
# Ключевое слово await

# async def my_coro(num):
#     print(f'Начинаем выполнение корутины {num}')
#     await asyncio.sleep(1)
#     print(f'Закончили выполнение корутины {num}')
#
# async  def main():
#     task = [asyncio.create_task(my_coro(i)) for i in range(1,6)]
#     await asyncio.gather(*task)

# await блокирует выполнение корутины

async def coro():
    print(f'Начинает выполнение')
    await asyncio.sleep(1)  # Тут блокируется корутина сoro() до завершения asyncio.sleep().
    print(f'Закончил')

async def main():
    await coro() # Тут блокируется main() до завершения my_coroutine().
    print('Выполнение корутины закончили')

if __name__ == '__main__':
    asyncio.run(main())
