class Employee:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age



class Manager(Employee):
    def calculate_bonus(self):
        return 2000



class Director(Employee):
    def calculate_bonus(self):
        return 6000


class DeputyDirector(Employee):
    def calculate_bonus(self):
        return 4000
