import asyncio


async def wait_for_materials(delivery_time, future: asyncio.Future):
    '''
    :param delivery_time:  время доставки
    :param future:  обьект футуры
    future: asyncio.Future - используется для удобства
    вместо asyncio.Future.set_result
    :return:
    '''
    print(f'Ожидание доставки материалов. Доставка займет {delivery_time} секунд')
    await asyncio.sleep(delivery_time)
    print('Материалы доставлены.')
    future.set_result('Доставка завершина')

async def menage_construction_project():
    '''
    Менеджер строительного проекта, который ожидает поставку материалов,
    прежде чем продолжить работу над проектом
    :return:
    '''
    # Создание обьекта
    future_materials_delivery = asyncio.Future()
    # Инициирование ожидание доставки материалов
    asyncio.create_task(wait_for_materials(5,future_materials_delivery))
    # Ожидание результата
    await future_materials_delivery
    # Получение и вывод результата доставки
    delivery_result = future_materials_delivery.result()
    print(f'Результат доставки: {delivery_result}')
    print(f'Продолжение строительных работ')


asyncio.run(menage_construction_project())



















