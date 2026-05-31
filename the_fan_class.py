class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed, radius, color, on):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_power(self):
        return self.__on