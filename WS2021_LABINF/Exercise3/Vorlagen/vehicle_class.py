class car:
    def __init__(self, motor, color, doors, price, hp, rabatt):
        self.rabatt = rabatt
        self.hp = hp
        self.price = price
        self.doors = doors
        self.color = color
        self.motor = motor

        if self.rabatt == True:
            self.price *= 0.8

    def __str__(self):
        return f"{self.hp}, {self.price}, {self.doors}, {self.color}, {self.motor}"