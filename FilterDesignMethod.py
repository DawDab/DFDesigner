"""
This file contains classes of design methods
Calculations of filter coefficient are done by scipy functions
"""
from abc import ABC, abstractmethod
from FilterParameters import *
from scipy import signal
import numpy as np


class DesignMethod(ABC):
    """
    Abstract base class to represent design method


    Methods
    -------
    calc_coeffs(self) -> tuple:
        Abstract method:
        method calculate filter coeffs
    """

    @abstractmethod
    def calc_coeffs(self, params: Parameters, filter_type: str) -> tuple:
        pass


class IirMethod(DesignMethod):
    """Abstract class represent IIR filter design methods"""
    @abstractmethod
    def calc_coeffs(self, params: Parameters, filter_type: str) -> tuple:
        pass


class FirMethod(DesignMethod):
    """Abstract class represent FIR filter design methods"""
    @abstractmethod
    def calc_coeffs(self, params: Parameters, filter_type: str) -> tuple:
        pass


class WindowMethod(FirMethod):
    """class represent window method"""
    def __init__(self, window: str):
        self.window = window

    def calc_coeffs(self, params: Parameters, filter_type: str) -> tuple:
        # Setup cutoff for single freq
        if filter_type in ["lowpass", "highpass"]:
            cutoff = [params.fc]
        else:
            # Setup cutoff for band freq
            cutoff = [params.fc1, params.fc2]
        #calc coefficients usign scipy.signal.firwin()
        h = signal.firwin(params.filter_order, cutoff, window=self.window, pass_zero=filter_type,
                          fs=params.fs)
        return tuple(h)


class ButterworthMethod(IirMethod):
    """class represent butterworth method"""
    def calc_coeffs(self, params: Parameters, filter_type: str) -> tuple:
        if filter_type in ["lowpass", "highpass"]:
            cutoff = [params.fc]
        else:
            cutoff = [params.fc1, params.fc2]
        return signal.butter(params.filter_order, cutoff, btype=filter_type, fs=params.fs)


class Chebyshev1Method(IirMethod):

    def calc_coeffs(self, params: Parameters, filter_type: str) -> tuple:
        if filter_type in ["lowpass", "highpass"]:
            cutoff = [params.fc]
        else:
            cutoff = [params.fc1, params.fc2]
        return signal.cheby1(params.filter_order, params.r_p, cutoff, btype=filter_type, fs=params.fs)


class Chebyshev2Method(IirMethod):

    def calc_coeffs(self, params: Parameters, filter_type: str) -> tuple:
        if filter_type in ["lowpass", "highpass"]:
            cutoff = [params.fc]
        else:
            cutoff = [params.fc1, params.fc2]
        return signal.cheby2(params.filter_order, params.r_s, cutoff, btype=filter_type, fs=params.fs)


class BesselMethod(IirMethod):

    def calc_coeffs(self, params: Parameters, filter_type: str) -> tuple:
        if filter_type in ["lowpass", "highpass"]:
            cutoff = [params.fc]
        else:
            cutoff = [params.fc1, params.fc2]
        return signal.bessel(params.filter_order, cutoff, btype=filter_type, fs=params.fs)


class EllipticMethod(IirMethod):

    def calc_coeffs(self, params: Parameters, filter_type: str) -> tuple:
        if filter_type in ["lowpass", "highpass"]:
            cutoff = [params.fc]
        else:
            cutoff = [params.fc1, params.fc2]
        return signal.ellip(params.filter_order, params.r_p, params.r_s, Wn=cutoff, btype=filter_type,
                            fs=params.fs)


class EquirippleMethod(FirMethod):

    def calc_coeffs(self, params: Parameters, filter_type: str) -> np.ndarray:
        if filter_type == "lowpass":
            return signal.remez(params.filter_order, [0, params.freq_pass1, params.freq_stop1, params.fs / 2],
                                [1, 0],
                                weight=[params.weight_pass1, params.weight_stop1], fs=params.fs,
                                grid_density=params.grid_density)
        elif filter_type == "highpass":
            return signal.remez(params.filter_order, [0, params.freq_stop1, params.freq_pass1, params.fs / 2],
                                [0, 1],
                                weight=[params.weight_pass1, params.weight_stop1], fs=params.fs,
                                grid_density=params.grid_density)
        elif filter_type == "bandpass":
            return signal.remez(params.filter_order,
                                [0, params.freq_stop1, params.freq_pass1, params.freq_pass2, params.freq_stop2,
                                 params.fs / 2], [0, 1, 0],
                                weight=[params.weight_stop1, params.weight_pass1, params.weight_stop2], fs=params.fs,
                                grid_density=params.grid_density)
        elif filter_type == "bandstop":
            return signal.remez(params.filter_order,
                                [0, params.freq_pass1, params.freq_stop1, params.freq_stop2, params.freq_pass2,
                                 params.fs / 2], [1, 0, 1],
                                weight=[params.weight_pass1, params.weight_stop1, params.weight_pass2], fs=params.fs,
                                grid_density=params.grid_density)


class LeastSquaresMethod(FirMethod):

    def calc_coeffs(self, params: Parameters, filter_type: str) -> np.ndarray:
        if filter_type == "lowpass":
            return signal.firls(params.filter_order, [0, params.freq_pass1, params.freq_stop1, params.fs / 2],
                                [1, 1, 0, 0], fs=params.fs)
        # [params.weight_pass1, params.weight_stop1]
        elif filter_type == "highpass":
            return signal.firls(params.filter_order, [0, params.freq_pass1, params.freq_stop1, params.fs / 2],
                                [0, 0, 1, 1], fs=params.fs)
        elif filter_type == "bandpass":
            return signal.firls(params.filter_order,
                                [0, params.freq_stop1, params.freq_pass1, params.freq_stop2, params.freq_pass2,
                                 params.fs / 2], [0, 0, 1, 1, 0, 0], fs=params.fs
                                )
        elif filter_type == "bandstop":
            return signal.firls(params.filter_order,
                                [0, params.freq_pass1, params.freq_stop1, params.freq_stop2, params.freq_pass2,
                                 params.fs / 2], [1, 1, 0, 0, 1, 1], fs=params.fs
                                )
