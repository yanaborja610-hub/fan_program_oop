class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed, radius, color, on):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on