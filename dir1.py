import asyncio
async def read_book(student, time):
    print(f"{student} начал читать книгу.")
    await asyncio.sleep(time)
    print(f"{student} закончил читать книгу за {time} секунд.")


async def main():
    task1 = asyncio.create_task(read_book('Алекс',5))
    task2 = asyncio.create_task(read_book('Мария', 3))
    task3 = asyncio.create_task(read_book('Иван', 4))
    await task1
    await task2
    await task3


if __name__ == '__main__':
    asyncio.run(main())