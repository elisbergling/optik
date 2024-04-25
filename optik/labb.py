import math
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data = [
    (80, 58.32),
    (75, 55.30),
    (70, 52.84),
    (65, 51.13),
    (60, 49.73),
    (55, 49.17),
    (50, 49.73),
    (45, 51.55),
    (40, 54.96),
]


x_values = np.array([item[0] for item in data])
y_values = np.array([item[1] for item in data])

def calculate_refraction_index(min_emerge):
    return 2*math.sin(math.radians((min_emerge+60)/2))


def calculate_deviation(b1, min_div):
    n = calculate_refraction_index(min_div)
    b1 = np.radians(b1)
    b2 = np.arcsin(np.sin(b1) / n)
    y2 = np.radians(60) - b2
    y1 = np.arcsin(np.sin(y2) * n)
    deviation = b1 + y1 - np.radians(60)
    return np.degrees(deviation)

x_curve = np.linspace(min(x_values), max(x_values), 100)
y_curve = [calculate_deviation(x, 49.17) for x in x_curve]

coefficients = np.polyfit(x_values, y_values, 2)
y_curve_poly = np.polyval(coefficients, x_curve)

popt, pcov = curve_fit(calculate_deviation, x_values, y_values, p0=49.17)
y_curve_fit = [calculate_deviation(x, popt) for x in x_curve]

print(f"Fixed Min Refraction Index: {calculate_refraction_index(49.17):.3f}")
print(f"Fitted Min Refraction Index: {calculate_refraction_index(popt):.3f}")
print(f"Fitted Poly Refraction Index: {calculate_refraction_index(np.min(y_curve_poly)):.3f}")

plt.scatter(x_values, y_values, label='Data')
plt.plot(x_curve, y_curve, label='Fixed Min')
plt.plot(x_curve, y_curve_fit, label='Fitted Min')
plt.plot(x_curve, y_curve_poly, label='Fitted Poly')
plt.xlabel('Infallsvinkel')
plt.ylabel('Avlänkningsvinkel')
plt.title('Prismans Avlänkningsvinklar')
plt.legend()
plt.grid(True)
plt.show()



