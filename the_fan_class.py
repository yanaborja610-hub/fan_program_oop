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

    # added features
    def get_mode(self):
        if self.__speed == self.slow:
            return "Gentle Breeze"
        elif self.__speed == self.medium:
            return "Comfort Mode"
        elif self.__speed == self.fast:
            return "Power Cool"

    def energy_used(self):
        if self.__speed == self.slow:
            return "25 watts"
        elif self.__speed == self.medium:
            return "50 watts"
        elif self.__speed == self.fast:
            return "80 watts"

    # displaying the methods
    def display(self):
        print("︶⊹︶︶୨୧︶︶⊹︶" * 10)
        print("Fan Properties")
        print("︶⊹︶︶୨୧︶︶⊹︶" * 10)
        print("Status:", "ON" if self.__on else "OFF")
        print("Speed:", self.__speed)
        print("Mode:", self.get_mode())
        print("Radius:", self.get_radius())
        print("Color:", self.get_color())
        print("Energy Used:", self.energy_used())
        print("︶⊹︶︶୨୧︶︶⊹︶" * 10)