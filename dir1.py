import asyncio
# Секундный интервал



async def print_with_delay(num: int):

    print(f'Coroutine {num} is done')
    await asyncio.sleep(1)

async def main():
    tasks = [asyncio.create_task(print_with_delay(i)) for i in range(10)]
    await asyncio.gather(*tasks)
    # for e in range(10):
    #     task = asyncio.create_task(print_with_delay(e))
    #     tasks.append(task)
asyncio.run(main())














