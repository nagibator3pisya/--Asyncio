import asyncio
"""#  asyncio.create_task"""

# async def example_coroutine():
#     await asyncio.sleep(1)
#     print("Hello from coroutine!")
#
# async def main():
#     task = asyncio.create_task(example_coroutine())
#     await task
#     print('Задачи finih')
#
# asyncio.run(main())

"""asyncio.gether"""

# async def example_coroutine():
#     await asyncio.sleep(5)
#     print("Hello from coroutine!")
#
#
# async def main():
#     tasks = []
#     for _ in range(10):
#         task = asyncio.create_task(example_coroutine()) # 10 задач создаем
#         tasks.append(task)
#     await asyncio.gather(*tasks) #  запускаем все задачи из списка tasks
#
# asyncio.run(main())


# async def log_data(data):
#     await asyncio.sleep(1)
#     print(f"Logged: {data}")
#
#
# async def main():
#     data_to_log = ["Data 1", "Data 2", "Data 3"]
#
#     # задачи для логирования данных в фоновом режиме
#     tasks = [asyncio.create_task(log_data(data)) for data in data_to_log]
#     print('Продолжение выполнения других задач')
#     await asyncio.gather(*tasks)
#
# asyncio.run(main())


# список поваров
# chef_list = ['','Франсуа', 'Жан', 'Марсель']
#
#
# async def cook_order(order_number: int, dish: str) -> list[tuple[int, str]]:
#     """
#     Фуннкция для приготовления заказов
#     :param order_number: - номер заказа
#     :param dish: - блюдо
#     :return:
#     """
#     print(f'Повар {chef_list[order_number]} начинает готовить заказ №{order_number}: {dish}')
#     await asyncio.sleep(2) # имитация готовки, загрузка данных из бз
#     print(f'Заказ № {order_number}: {dish} готов')
#     return f'{dish} для заказа № {order_number}'
#
#
# async def serve_order(order_number: int, dish: str) -> list[tuple[int, str]]:
#     """
#
#     :param order_number: - номер заказа
#     :param dish: - блюдо
#     """
#     await cook_order(order_number,dish) # подождать пока оно приготовиться
#     print(f'Официант подает {dish}')
#
#
# async def manager():
#     '''
#     Менеджер событный цикл назначение задачи
#     :return:
#     '''
#     orders = [(1,'салат'),(2,'стейк'),(3,'суп')]
#     tasks = [asyncio.create_task(serve_order(order_number,dish)) for order_number,dish in orders]
#     await asyncio.gather(*tasks)
#
# asyncio.run(manager())













