GLOBAL_VARIABLE = 0


def increase_global_variable():
    """
    функция которая увеличивает значение глобальной переменной
    """
    global GLOBAL_VARIABLE 
    GLOBAL_VARIABLE += 1 
    return GLOBAL_VARIABLE 

if __name__ == "__main__":
    print(increase_global_variable()) 
    print(increase_global_variable()) 
    print(increase_global_variable()) 
