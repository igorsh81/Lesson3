# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func(a, b):
    try:
        c = a / b
        return c
    except ZeroDivisionError:
        return "b не может быть 0"
    except ValueError:
        return "введите число"


print(my_func((int(input("Введите a : "))), (int(input("Введите b : ")))))
