import asyncio


# Счётчики #1

# Counter 1 - имя счётчика
# 13 - максимальное значение для счётчика Counter_1

# max_counts = {
#     "Counter 1": 13,
#     "Counter 2": 7
# }
max_counts = {
    "Counter 1": 10,
    "Counter 2": 5,
    "Counter 3": 15
}
#  task1 = asyncio.create_task(counter('Counter 1', delays['Counter 1']))
delays = { # нужно было добавить счётчик при вызове  delays['Counter 1']
    "Counter 1": 1,
    "Counter 2": 2,
    "Counter 3": 0.5
}
counters = {
    "Counter 1": 0,
    "Counter 2": 0,
    'Counter 3': 0
}
"""
Создайте словарь counters, где ключи — это имена счётчиков ("Counter 1" и "Counter 2"), а
 значения —  это текущие значения счётчиков, изначально равные нулю.
"""

'''
Напишите асинхронную функцию counter, которая принимает имя счётчика и задержку. 
В цикле эта функция должна увеличивать значение соответствующего 
счётчика в словаре counters на 1,  делать паузу на одну секунду и  
выводить сообщение с именем счетчика и его текущим значением. 
Этот цикл должен продолжаться до тех пор, 
пока значение счётчика не достигнет соответствующего значения в словаре max_counts.
'''


async def counter(name: str)-> None:

    while counters[name] < max_counts[name]:
        counters[name] += 1 # увеличение
        await asyncio.sleep(delays[name])
        print(f"{name}: {counters[name]}")



async def main():
    #  gether() придумать
    # task1 = asyncio.create_task(counter('Counter 1', ))
    # task2 = asyncio.create_task(counter('Counter 2', ))
    # task3 = asyncio.create_task(counter('Counter 3',))
    # await task1
    # await task2
    # await task3
    task = [asyncio.create_task(counter(name)) for name in counters]
    await asyncio.gather(*task)
asyncio.run(main())











