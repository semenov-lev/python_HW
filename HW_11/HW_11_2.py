class MyZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt


def division(a, b):
    try:
        a = float(a)
        b = float(b)
        if b == 0:
            raise MyZeroDivision("Деление на ноль! Не пытайтесь сломать вселенную!")
        else:
            return f"Результат деления: {a / b}"
    except ValueError:
        return "Ошибка: Введенные данные не являются числами."
    except MyZeroDivision as err:
        return err


print(division(50, 5))
print(division("пятьдесят", 5))
print(division(50, 0))
