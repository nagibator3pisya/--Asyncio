import asyncio

# Асинхронная функция имитирующая чтение данныъ из файла

async def read_data_file(filename):
    print(f'Начинаем чтение из файла {filename} ')
    await asyncio.sleep(2) # имитация задержки для чтени файла
    print(f'Чтение из файла {filename} завершено')
    return f'Данные из {filename}'

# Асинхронная функция имитирующая отпр данных в интер
async def send_data_to_internet(data):
    print('Начинаем отправку данных в интернет')
    await asyncio.sleep(3) # имитация задержки для отправки данных
    print('Отправка данных в интернет завершена')

# Главная асинк функция
async def main():
    filename = 'exemple.txt'
    # чтение данных из файла
    file_data = await read_data_file(filename)
    await send_data_to_internet(file_data)

if __name__ == '__main__':
    asyncio.run(main())

