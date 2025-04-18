import asyncio
# Задачи

# Пример данных
log_events = [
    {"event": "Запрос на вход", "delay": 0.5},
    {"event": "Запрос данных пользователя", "delay": 1.0},
    {"event": "Обновление данных пользователя", "delay": 1.5},
    {"event": "Обновление конфигурации сервера", "delay": 5.0}
    ]

async def fetch_log(event):
    delay = event.get('delay')
    await asyncio.sleep(delay)
    print(f"Событие: '{event['event']}' обработано с задержкой {delay} сек.")

async def main():
    task = [asyncio.create_task(fetch_log(i)) for i in log_events]
    result = await asyncio.gather(*task)

asyncio.run(main())