import matplotlib.pyplot as mipoo

d = ["Sun", "Mon", "Tue", "Wed", "Thu"]
s = [70, 85, 60, 90, 75]

mipoo.plot(d, s)
mipoo.show()


mipoo.plot(d, s)
mipoo.title("Ching chong tracker")
mipoo.xlabel("eh")
mipoo.ylabel("sca")
mipoo.grid(True)
mipoo.ylim(0, 100)

mipoo.plot(d, s, color="blue", marker="o", linestyle="dashed", linewidth=2)
mipoo.title("School performance tracker")
mipoo.xlabel("Middle day")
mipoo.ylabel("sca")
mipoo.grid(True)
mipoo.ylim(0, 100)
mipoo.show()

mipoo.bar(d, s, color="orange")
mipoo.title("School performance tracker")
mipoo.xlabel("Middle day")
mipoo.ylabel("sca")
mipoo.grid(True)
mipoo.ylim(0, 100)
mipoo.show()