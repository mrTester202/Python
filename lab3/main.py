class Employee:
    def __init__(self, name, surname, age):
        """
        создание переменных (конструктор)
        """
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__bonus = 0

    def get_name(self):
        """
        метод получения имени
        """
        return self.__name

    def set_name(self, name):
        """
        метод установки имени
        """
        self.__name = name

    def get_surname(self):
        """
        метод получения фамилии
        """
        return self.__surname

    def set_surname(self, surname):
        """
        метод установки фамилии
        """
        self.__surname = surname

    def get_age(self):
        """
        метод получения возраста
        """
        return self.__age

    def set_age(self, age):
        """
        метод установки возраста
        """
        self.__age = age
        
    def get_bonus(self):
        """
        метод получения бонуса
        """
        return self.__bonus

    def set_bonus(self, name):
        """
        метод установки бонуса
        """
        self.__bonus = name
    
    def calculate_salary(self):
        return (1000*0.87)

    def calculate_bonus(self):
        """
        метод вычисления бонуса
        """
        return calculate_salary() + 2500 * get_bonus()
        
class Manager(Employee):
   def calculate_salary(self):
        """
        метод вычисления зарплаты
        """
        return (2000*0.87)


class Director(Employee):
    def calculate_salary(self):
        """
        метод вычисления зарплаты
        """
        return (6000*0.87)


class DeputyDirector(Employee):
    def calculate_salary(self):
        """
        метод вычисления зарплаты
        """
        return (4000*0.87)

if __name__ == '__main__':
    worker_1 = Employee("John", "Mitch", 30)
    salary_w_1 = worker_1.calculate_salary()
    print(salary_w_1)
