class vehicle:
    def __init__(self, height, colour, width):
        self.height = height
        self.colour = colour
        self.width = width

class smol(vehicle):
    def __init__(self, name, speed, height, width, colour):
        self.name = name
        self.speed = speed
        super().__init__(height, width, colour)
        print(f"Ts smol car's name iz {name}.")
        print(f"Itz max speed iz {speed}.")
        print(f"Itz height iz {height} inches and itz width iz {width} inches.")
        print(f"Itz colour iz {colour}.")
        print(f"It iz an issubclass to vehicle as it shows itz {issubclass(smol, vehicle)}.")
        

info = smol("Dodger S", 105, 54, 66, "Indigo")

