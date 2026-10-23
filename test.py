import numpy as np

dt = [('name', "S15"), ('class', int), ('height', float)]
sd = [("James", 5, 48.5), ("Nail", 6, 52.5), ("Paul", 5, 42.10), ("Pit", 5, 40.11)]
s = np.array(sd, dtype=dt)

print(f"Array: {s}")
print("Sorted by height: ")
print(np.sort(s, order='height'))