class FamilyMember:
    def __init__(self, eyecolour, height):
        self.eyecolour = eyecolour
        self.height = height

class Kiddo(FamilyMember):
    def __init__(self, eyecolour, height, name, age, hobby):
        self.name = name
        self.age = age
        super().__init__(eyecolour, height)
        print(f"Ts kiddo's name iz {self.name}.")
        print(f"His age iz {self.age}.")
        print(f"{self.name} likes {hobby}.")
        print(f"His eye colour iz {eyecolour} and his height iz {height}cm.")
        print(issubclass(Kiddo, FamilyMember))
        print("He iz a subclass family member as it shows.")

kiddo = Kiddo("black", 140, "Frank", 10, "gaming")


        
        