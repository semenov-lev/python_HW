import time


class TrafficLight:
    __color = 0

    def running(self):
        print(f"Красный")
        time.sleep(7)
        print(f"Желтый")
        time.sleep(2)
        print(f"Зеленый")
        time.sleep(7)


t = TrafficLight()
t.running()
