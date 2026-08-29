class computer:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print(f"Da selling price iz {format(self.__maxprice)}.")

    def set(self, price):
        self.__maxprice = price

c = computer()
c.sell()

c.__maxprice = 1000
c.sell()

c.set(1200)
c.sell()