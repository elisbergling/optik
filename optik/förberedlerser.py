import math
import numpy as np
import matplotlib.pyplot as plt

def calculate_minimum_deviation(b1, wave_lenght):
    n = refraction_index(wave_lenght)
    b1 = math.radians(b1)
    b2 = math.asin(math.sin(b1) / n)
    y2 = math.radians(60) - b2
    if math.sin(y2) * n <= 1:
        y1 = math.asin(math.sin(y2) * n)
        minimum_deviation = b1 + y1 - math.radians(60)
    else:
        minimum_deviation = 0
    return math.degrees(minimum_deviation)

def generate_minimum_deviation(colour, wave_lenght):
    angles_of_incidence = np.linspace(0, 90, 100)
    minimum_deviations = [calculate_minimum_deviation(angle, wave_lenght) for angle in angles_of_incidence] 
    plt.plot(angles_of_incidence, minimum_deviations, color=colour)

def refraction_index(wave_lenght):
    return 1.522 + 4590/(wave_lenght**2)


generate_minimum_deviation("red", 700)
generate_minimum_deviation("green", 550)
generate_minimum_deviation("blue", 450)

plt.xlabel('Angle of Incidence (degrees)')
plt.ylabel('Minimum Deviation (degrees)')
plt.title('Minimum Deviation vs Angle of Incidence')
plt.grid(True)
plt.show()