import asyncio

import asyncio
import random

async def waiter(future: asyncio.Future):
    await future
    print(f"future выполнен, результат {future.result()}. Корутина waiter() может продолжить работу")

async def setter(future):
    await asyncio.sleep(random.uniform(1, 3))
    future.set_result(True)


async def main():
    future = asyncio.Future()

    # Запускаем обе корутины одновременно
    await asyncio.gather(waiter(future), setter(future))

asyncio.run(main())


