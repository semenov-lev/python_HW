income_dict = {"wage": 25000, "bonus": 20000}


class Worker:
    _income = income_dict

    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):
    # PyCharm ругается на повтор кода, но я не сообразил, как можно заменить функцию с унаследованием переменных:
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)
        self.wage = int(super()._income["wage"])
        self.bonus = int(super()._income["bonus"])

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self.wage + self.bonus


p_1 = Position("Александр", "Сидоров", "Инженер")
print(p_1.get_full_name())
print(p_1.wage)
print(p_1.bonus)
print(p_1.get_total_income())

p_2 = Position("Василий", "Пупкин", "Проектировщик")
print(p_2.get_full_name())
print(p_2.wage)
print(p_2.bonus)
print(p_2.get_total_income())
