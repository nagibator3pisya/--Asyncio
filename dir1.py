import asyncio
from itertools import count

# Счётчики #1

# Counter 1 - имя счётчика
# 13 - максимальное значение для счётчика Counter_1

max_counts = {
    "Counter 1": 13,
    "Counter 2": 7
}
"""
Создайте словарь counters, где ключи — это имена счётчиков ("Counter 1" и "Counter 2"), а
 значения —  это текущие значения счётчиков, изначально равные нулю.
"""
counters = {
    "Counter 1": 0,
    "Counter 2": 0
}
'''
Напишите асинхронную функцию counter, которая принимает имя счётчика и задержку. 
В цикле эта функция должна увеличивать значение соответствующего 
счётчика в словаре counters на 1,  делать паузу на одну секунду и  
выводить сообщение с именем счетчика и его текущим значением. 
Этот цикл должен продолжаться до тех пор, 
пока значение счётчика не достигнет соответствующего значения в словаре max_counts.
'''


async def counter(name: str, delay: int)-> None:
    while counters[name] < max_counts[name]:
        counters[name] += 1 # увеличение
        await asyncio.sleep(delay)
        print(f"{name}: {counters[name]}")



async def main():
    task1 = asyncio.create_task(counter('Counter 1',1))
    task2 = asyncio.create_task(counter('Counter 2', 1))
    await task1
    await task2
asyncio.run(main())











