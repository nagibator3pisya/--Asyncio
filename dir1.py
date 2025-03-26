import asyncio

async def Coroutine1(i):
    await asyncio.sleep(1 / i)
    print(f'Coroutine {i} is done')



async def  main():
    result = [asyncio.create_task(Coroutine1(i)) for i in range(1,4)]

    await asyncio.gather(*result)


asyncio.run(main())













