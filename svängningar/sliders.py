import numpy as np
from numpy import cos, sqrt, exp
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
t = np.linspace(0, 100, 1000)
init_value = 5

fig, ax = plt.subplots()
ax.set_ylim([-5, 5])
line, = ax.plot(t, t*0)
ax.set_xlabel("x-axis")

fig.subplots_adjust(left=0.5, bottom=0.25)

def spring(k: float, m: float, b: float, A: float, phase: float) -> np.array:
    w = sqrt(k/m)
    def f(t: float) -> float:
        return A * exp(-b * t/ (2 * m)) * cos(w * t + phase)
    return f

def add_slider(valmin, valmax, init, label, axis) -> Slider:
    slider = Slider(
        ax=fig.add_axes(axis),
        label=label,
        valmin=valmin,
        valmax=valmax,
        valinit=init,
        orientation="vertical"
    )
    return slider
k_slider = add_slider(0.1, 10, 5, "k", [0.1, 0.25, 0.0225, 0.63])
m_slider = add_slider(0.1, 5, 2.5, "m", [0.2, 0.25, 0.0225, 0.63])
b_slider = add_slider(0.001, 0.2, 0.1, "b", [0.3, 0.25, 0.0225, 0.63])
phase_slider = add_slider(-np.pi*2, np.pi*2, 0, "phase", [0.4, 0.25, 0.0225, 0.63])
def update(val):
    line.set_ydata(
        spring(
            k=k_slider.val,
            m=m_slider.val,
            b=b_slider.val,
            A=4.14,
            phase=phase_slider.val
        )(t)
    )
    fig.canvas.draw_idle()
    
k_slider.on_changed(update)
m_slider.on_changed(update)
b_slider.on_changed(update)
phase_slider.on_changed(update)

update(1)

plt.show()

def getSpring(k: float, m: float, b: float, A: float, phase: float) -> float:
    w = sqrt(k/m)
    def f(t: float) -> float:
        return A * exp(-b * t/ (2 * m)) * cos(w * t + phase)
    return f