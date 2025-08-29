class Calculator:
    def __init__(self):
        self.walls = []

    def get_wall(self):
        wall_length = float(input("wall length: "))
        wall_width = float(input("wall width: "))
        self.walls.append({"length" : wall_length, "width" : wall_width})

    def convert_to_mm(self):
        pass
    
    def wall_area(self):
        pass

wallc = Calculator()