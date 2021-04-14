class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.is_police = is_police
        self.speed = speed

    def show_speed(self):
        return f"Текущая скорость составляет {self.speed} км/ч."

    def go(self):
        return "Машина поехала"

    def stop(self):
        return "Машина остановилась"

    def turn(self, direction):
        return f"Машина повернула {direction}"


class TownCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f"Скорость составляет {self.speed} км/ч. Скорость превышена!"
        else:
            return f"Текущая скорость составляет {self.speed} км/ч."


class SportCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)


class WorkCar(Car):
    def __init__(self, name, color, speed, is_police=False):
        super().__init__(name, color, speed, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f"Скорость составляет {self.speed} км/ч. Скорость превышена!"
        else:
            return f"Текущая скорость составляет {self.speed} км/ч."


class Police(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = Police("Полиция", "Синий", 100)
print(police_car.name)
print(police_car.color)
print(police_car.is_police)
print(police_car.show_speed())

sport_car = SportCar("Гонщик", "Красный", 160)
print(sport_car.name)
print(sport_car.color)
print(sport_car.is_police)
print(sport_car.show_speed())

work_car = WorkCar("Фургон с мороженым", "розовый", 180)
print(work_car.name)
print(work_car.color)
print(work_car.is_police)
print(work_car.show_speed())
