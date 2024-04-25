import pandas as pd
import os
import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

TIME_HEADER = "Time (s)"
X_ACCELERATION_HEADER = "Linear Acceleration x (m/s^2)"
Y_ACCELERATION_HEADER = "Linear Acceleration y (m/s^2)"
Z_ACCELERATION_HEADER = "Linear Acceleration z (m/s^2)"

def parse_string_to_float(to_be_parsed: str, mantissa_splitter: str = '×') -> float:
    mantissa, tail = to_be_parsed.split(mantissa_splitter)
    _, exponent = tail.split("^")
    return float(mantissa) * 10**int(exponent)

def read_freq(fil, begin, end):
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, fil)
    df = pd.read_csv(file_path)
    times = df[TIME_HEADER].apply(parse_string_to_float)
    ys = df[Y_ACCELERATION_HEADER].apply(parse_string_to_float).values

    ys_filter = ys[begin:end]
    times_filter = times[begin:end]

    params, _ = curve_fit(sin_function, times_filter, ys_filter)

    amplitude, frequency, phase = params

    print(f"Amplitude: {amplitude}") 
    print(f"Frequency: {frequency}")  
    print(f"Phase: {phase}")

    fitted_ys = sin_function(times_filter, *params)
    plt.plot(times_filter, ys_filter, label='Original Data')
    plt.plot(times_filter, fitted_ys, label='Fitted Sin Curve')
    plt.legend()
    plt.show()

    return frequency


def sin_function(x, amplitude, frequency, phase):
    return amplitude * np.sin(2 * np.pi * frequency * x + phase)

if __name__ == "__main__":
    freq1 = read_freq('Raw Data 1.csv', 400, 900)
    freq2 = read_freq('Raw Data 2.csv', 100, 1500)

    mass = (0.2 * freq2**2)/(freq1**2-freq2**2) - 0.12

    print(f'Mass: {mass}')