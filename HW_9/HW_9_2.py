class Road:
    __length = 1500
    __width = 6

    def calculate_asphalt(self):
        mass_per_cm = 2.42 * 100 / 10
        mass_for_road = float(self.__length * self.__width * mass_per_cm * 6 / 1000)
        return f"{mass_for_road} тонн"


r = Road()
print(r.calculate_asphalt())
