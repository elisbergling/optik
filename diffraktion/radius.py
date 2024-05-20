import math

data = [(6e-3, 14),
        (8e-3, 12),
        (10e-3, 10),
        (14e-3, 8),
        (18e-3, 6)]


def calculate_hole_diamiter(p, n):
    wavelength = 641.3e-9  # wavelength of the laser in meters

    radius = math.sqrt((p + n * wavelength / 2)**2 - p**2)
    return radius * 2

def average():
    return sum([calculate_hole_diamiter(*d) for d in data]) / len(data)

print(average() * 1e3, "mm")