# В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Нужно сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Используйте написанную ранее функцию int_func().

def int_func(a):
    a = str.title(a)
    return a


text_enter = input("Введите текст состоящий из латинских букв в нижнем регистре через пробел: ")
print(int_func(text_enter))
