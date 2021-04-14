class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        return print("Отрисовка при помощи ручки")


class Pencil(Stationery):
    def draw(self):
        return print("Отрисовка при помощи карандаша")


class Handle(Stationery):
    def draw(self):
        return print("Отрисовка при помощи маркера")


a = Pen("Ручка")
print(a.title)
a.draw()

b = Stationery("Инструмент")
print(b.title)
b.draw()

c = Handle("Маркер")
print(c.title)
c.draw()
