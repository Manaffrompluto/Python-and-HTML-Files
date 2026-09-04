from abc import ABC, abstractmethod

class ab(ABC):

    def print(self, x):
        print(f"Passed value = {x}")

    @abstractmethod
    def task(self):
        print("")

class test(ab):

    def task(self):
        print("")

testobj = test()
testobj.task()
testobj.print(100)
