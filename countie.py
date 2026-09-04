class ind():

    def cap(self):
        print("India's capital iz Delhi.")

    def lang(self):
        print("India's most spoken language iz Hindi.")

    def type(self):
        print("India's population iz one of da biggest in da world and more airports are in construction.")

class bd():

    def cap(self):
        print("Bangladesh's capital iz Dhaka.")

    def lang(self):
        print("Bangladesh's language iz Bangla.")

    def type(self):
        print("Bangladesh iz still developing and has Cox's Bazaar.")

class us():

    def cap(self):
        print("Washington D.C iz America's capital.")

    def lang(self):
        print("American English iz America's language.")

    def type(self):
        print("They just renamed Lake Ontario to Lake America. What's next? Planet America?")

india = ind()
bangla = bd()
america = us()

for country in(india, bangla, america):
    country.cap()
    country.lang()
    country.type()
    