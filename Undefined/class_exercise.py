class Vehicle:
    def __init__(self, max_speed, sum_km):
        self.max_speed = max_speed
        self.sum_km = sum_km

    def __str__(self):
            return f"Max speed is: {self.max_speed}\nSum of km is: {self.sum_km}"


auto = Vehicle(220, "22k")
print(auto)


class Vehicle:

    def __init__(self, name, max_speed, sum_km):
        self.name = name
        self.max_speed = max_speed
        self.sum_km = sum_km

    def __str__(self):
        return f"Vehicle name: {self.name}\nMax speed: {self.max_speed}\nSum of km is: {self.sum_km}"



class Bus(Vehicle):

    def __init__(self):
        super().__init__("Volvo",180, "36k")
    
        super().__str__()

bus = Bus()
print(bus)