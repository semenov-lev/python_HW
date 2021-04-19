from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def amount_of_material(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Coat(Clothes):

    def __init__(self, param):
        self.v = round(param, 2)

    @property
    def amount_of_material(self):
        return round((self.v / 6.5 + 0.5), 2)

    def __add__(self, other):
        return Coat(self.amount_of_material + other.amount_of_material)

    def __str__(self):
        return str(self.v)


class Costume(Clothes):
    def __init__(self, param):
        self.h = round(param, 2)

    @property
    def amount_of_material(self):
        return round((self.h * 2 + 0.3), 2)

    def __add__(self, other):
        return Costume(self.amount_of_material + other.amount_of_material)

    def __str__(self):
        return str(self.h)


coa_1 = Coat(50)
print(coa_1.amount_of_material)

cos_1 = Costume(50)
print(cos_1.amount_of_material)

coa_2 = Coat(20)
print(coa_2.amount_of_material)

print(coa_1 + cos_1 + coa_2)
