from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = round(param, 2)

    @abstractmethod
    def amount_of_material(self):
        pass


class Coat(Clothes):
    @property
    def amount_of_material(self):
        return round((self.param / 6.5 + 0.5), 2)

    def __add__(self, other):
        return self.amount_of_material + other.amount_of_material


class Costume(Clothes):
    @property
    def amount_of_material(self):
        return round((self.param * 2 + 0.3), 2)

    def __add__(self, other):
        return self.amount_of_material + other.amount_of_material


coa = Coat(50)
print(coa.amount_of_material)

cos = Costume(50)
print(cos.amount_of_material)

print(coa + cos)
