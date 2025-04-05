import asyncio
# Методы done(),cancel(),cancelled()
# Pending (ожидание)

async def main():
    future = asyncio.Future()
    if not future.done():
        print('Состояние: Pending')
    try:
        result = future.result()
        print(result)
    except asyncio.InvalidStateError:
        print('Задача ещё не выполнена. Доступа к результатам нет!')


async def main_Completed():
    future = asyncio.Future()
    future.set_result('Задача завершена')
    result = future.result()

    if future.done():
        print('Состояние : Completed(завершено)')
        print(f'Результат: {result} ')


async  def main_Cancelled():
    future = asyncio.Future()
    future.cancel()
    if future.cancelled():
        print('Состояние Cancelled (Отменено)')
    try:
        result =future.result()
        print(result)
    except asyncio.CancelledError:
        print('Задача отменена. Доступа к результатам нет')

# if __name__ == '__main__':
#     # asyncio.run(main())
#     # asyncio.run(main_Completed())
#     asyncio.run(main_Cancelled())


async def set_after(fut, delay, value):
    await asyncio.sleep(delay)
    fut.set_result(value)

async def main():
    future = asyncio.Future()
    asyncio.ensure_future(set_after(future, 1, 'done'))
    result = await future
    print(result)

asyncio.run(main())