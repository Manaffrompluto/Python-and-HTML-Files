class Parrot:
    species = "Bird"

    def __init__(self, name, age):
        self.name = name
        self.age = age

hyacinthmacaw = Parrot("Hyacinth Macaw", 50)
sunconure = Parrot("Sun Conure", 15)

print("Da gentle giant of da parrot world iz {}".format(hyacinthmacaw.name) + str(" and they generally live around {}".format(hyacinthmacaw.age)) + str(" years."))
print("Da sunset yellowish parrot iz {}".format(sunconure.name) + str(" and they generally live around {}".format(sunconure.age)) + str(" years."))