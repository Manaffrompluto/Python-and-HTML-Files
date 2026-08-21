class Vehicle:
    def __init__(self, maxspeed, mileage):
        self.maxspeed = maxspeed
        self.mileage = mileage

X = Vehicle(240, 15)
S = Vehicle(120, 10)
V = Vehicle(450, 25)
print("Da  Car S iz da lowest tier budget friendly car.")
print(f"Itz max speed iz {S.maxspeed} while itz mileage speed iz {S.mileage}.")
print("Da  Car X iz a middle performer car.")
print(f"Itz max speed iz {X.maxspeed} while itz mileage speed iz {X.mileage}.")
print("Da  Car V iz da highest tier car.")
print(f"Itz max speed iz {V.maxspeed} while itz mileage speed iz {V.mileage}.")
