# Первый вход в асинхронное
import time


def fun1(x):
    print(x**2)
    time.sleep(3)
    print("fun1 finich")


def fun2(x):
    print(x**0.5)
    time.sleep(3)
    print("fun2 finich")




def main():
    fun1(2)
    fun2(5)




print(time.strftime('%X'))

main()

print(time.strftime('%X'))


