from abc import ABC, abstractmethod

class animal(ABC):

    def move(self):
        pass

class human(animal):
    def move(self):
        print("Today's humans are dumbasses, can't read or write and are ipad kids.")

class dog(animal):
    def move(self):
        print("Dogs are ur faithful friend and bodyguard.")

class cat(animal):
    def move(self):
        print("Cats are cuddlers and have deep bonds.")

class fox(animal):
    def move(self):
        print("Foxes are cheeky animals who steal chickens but are adorable.")

class snake(animal):
    def move(self):
        print("Snakes are gay, kill everyone and are somehow vertebrates.")

h = human()
h.move()

d = dog()
d.move()

c = cat()
c.move()

f = fox()
f.move()

s = snake()
s.move()