import asyncio

students = {
    "Алекс": {"course": "Асинхронный Python", "steps": 515, "speed": 78},
    "Мария": {"course": "Многопоточный Python", "steps": 431, "speed": 62},
    "Иван": {"course": "WEB Парсинг на Python", "steps": 491, "speed": 57}
}

async def study_course(student, course, steps, speed):
    reading_time = round(steps / speed,2)
    print(f'{student} начал проходить курс {course}.')
    await asyncio.sleep(reading_time)
    print(f"{student} прошел курс {course} за {reading_time} ч.")



async def main():
    task = []
    for student,deteil in students.items():
        tt = asyncio.create_task(study_course(student,deteil['course'],deteil['steps'],deteil['speed']))
        task.append(tt)
    await asyncio.gather(*task)

if __name__ == '__main__':
    asyncio.run(main())

