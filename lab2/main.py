global_variable = 0 # объявляем глобальную переменную

def increase_global_variable():
    global global_variable # используем ключевое слово global, чтобы указать, что хотим использовать глобальную переменную
    global_variable += 1 # увеличиваем значение глобальной переменной на 1
    return global_variable # возврат значения

print(increase_global_variable()) # 1
print(increase_global_variable()) # 2
print(increase_global_variable()) # 3
