from scipy import signal
from Filter import *
from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt


class Plot:
    def __init__(self, title=None, y_label=None, x_label=None):
        self.title = title
        self.y_label = y_label
        self.x_label = x_label

    @abstractmethod
    def return_plot(self, designed_filter: Filter):
        pass


class MagnitudePlot(Plot):
    def __init__(self, title="Frequency response", y_label="Magnitude [dB]", x_label="Frequency [Hz]"):
        super().__init__(title, y_label, x_label)

    def return_plot(self, filter: Filter):
        if isinstance(filter.method, IirMethod):
            w, h = signal.freqz(filter.filter_coefficients[0], filter.filter_coefficients[1], fs=filter.params.fs)
        else:
            w, h = signal.freqz(filter.filter_coefficients, fs=filter.params.fs)
        return [w, 20 * np.log10(np.abs(h))]


class PhasePlot(Plot):
    def __init__(self, title="Phase response", y_label="Phase (radians)", x_label="Frequency [Hz]"):
        super().__init__(title, y_label, x_label)

    def return_plot(self, filter: Filter):
        if isinstance(filter.method, IirMethod):
            w, h = signal.freqz(filter.filter_coefficients[0], filter.filter_coefficients[1], fs=filter.params.fs)
        else:
            w, h = signal.freqz(filter.filter_coefficients, fs=filter.params.fs)
        # angles = np.unwrap(np.angle(h))
        angles = np.unwrap(np.arctan2(np.imag(h), np.real(h)))
        return [w, angles]

