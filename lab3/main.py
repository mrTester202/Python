class Employee:
    def __init__(self, name: str, surname: str, age: int, classter) -> None:
        """
        Создание переменных (конструктор)
        """
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__bonus = 0
        self.__classter = classter

    def get_name(self) -> str:
        """
        Метод получения имени
        """
        return self.__name

    def set_name(self, name: str) -> None:
        """
        Метод установки имени
        """
        self.__name = name

    def get_surname(self) -> str:
        """
        Метод получения фамилии
        """
        return self.__surname

    def set_surname(self, surname: str) -> None:
        """
        Метод установки фамилии
        """
        self.__surname = surname

    def get_age(self) -> int:
        """
        Метод получения возраста
        """
        return self.__age

    def set_age(self, age: int) -> None:
        """
        Метод установки возраста
        """
        self.__age = age

    def get_bonus(self) -> int:
        """
        Метод получения бонуса
        """
        return self.__bonus

    def set_bonus(self, bonus: int) -> None:
        """
        Метод установки бонуса
        """
        self.__bonus = bonus

    def calculate_salary(self) -> float:
        """
        Метод расчета зарплаты
        """
        return self.__classter.calculate_salary(self)

    def calculate_bonus(self) -> float:
        """
        Метод расчета бонуса
        """
        return self.calculate_salary() + 2500 * self.__bonus

class Manager(Employee):
    def calculate_salary(self) -> float:
        """
        Метод расчета зарплаты
        """
        return 2000 * 0.87

class Director(Employee):
    def calculate_salary(self) -> float:
        """
        Метод расчета зарплаты
        """
        return 6000 * 0.87

class DeputyDirector(Employee):
    def calculate_salary(self) -> float:
        """
        Метод расчета зарплаты
        """
        return 4000 * 0.87

if __name__ == '__main__':
    while True:
        choose = input("Выберите кто вы:\n1 - менеджер\n2 - директор\n3 - зам.директора\n--> ")
        if choose == '1':
            worker_1 = Employee("John", "Mitch", 30, Manager)  # Передайте экземпляр класса, а не класс
            salary_w_1 = worker_1.calculate_salary()
            print(salary_w_1)
        elif choose == '2':
            worker_2 = Employee("John", "Mitch", 30, Director)  # Передайте экземпляр класса, а не класс
            salary_w_2 = worker_2.calculate_salary()
            print(salary_w_2)
        elif choose == '3':
            worker_3 = Employee("John", "Mitch", 30, DeputyDirector)  # Передайте экземпляр класса, а не класс
            salary_w_3 = worker_3.calculate_salary()
            print(salary_w_3)
        else:
            print("error!\n")
