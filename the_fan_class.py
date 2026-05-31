class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed, radius, color, on):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    # getters
    def get_speed(self):
        return self.__speed

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    def get_power(self):
        return self.__on

    # setters
    def set_speed(self, speed):
        self.__speed = speed

    def set_radius(self, radius):
        self.__radius = radius

    def set_color(self, color):
        self.__color = color

    def set_power(self, power):
        self.__on = power

    def turn_on(self):
        self.__on = True

    def turn_off(self):
        self.__on = False
