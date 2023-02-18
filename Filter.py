from abc import ABC, abstractmethod
from FilterParameters import Parameters
from FilterDesignMethod import *


class Filter(ABC):
    """
    Abstract base class to represent filter

    Attributes
    ----------
    params : Parameters
        filter parameters
    method : DesignMethod
        filter design method
    filter_coefficients : tuple


    Methods
    -------
    design_filter(self):
        Abstract method:
        preform calculations using defined design method.
    """
    def __init__(self, params: Parameters, design_method: DesignMethod):
        self.params = params
        self.method = design_method
        self.filter_coefficients = self.design_filter()

    @abstractmethod
    def design_filter(self) -> tuple:
        pass


class LowpassFilter(Filter):
    """Class represent lowpass filter

    """
    def __init__(self, params: Parameters, design_method: DesignMethod):
        self.filter_type = "lowpass"
        super().__init__(params, design_method)

    def design_filter(self) -> tuple:
        return self.method.calc_coeffs(self.params, self.filter_type)


class HighpassFilter(Filter):
    """Class represent highpass filter"""
    def __init__(self, params: Parameters, design_method: DesignMethod):
        self.filter_type = "highpass"
        super().__init__(params, design_method)

    def design_filter(self) -> tuple:
        return self.method.calc_coeffs(self.params, self.filter_type)


class BandpassFilter(Filter):
    """Class represent bandpass filter"""
    def __init__(self, params: Parameters, design_method: DesignMethod):
        self.filter_type = "bandpass"
        super().__init__(params, design_method)

    def design_filter(self) -> tuple:
        return self.method.calc_coeffs(self.params, self.filter_type)


class BandstopFilter(Filter):
    """Class represent bandstop filter"""
    def __init__(self, params: Parameters, design_method: DesignMethod):
        self.filter_type = "bandstop"
        super().__init__(params, design_method)

    def design_filter(self) -> tuple:
        return self.method.calc_coeffs(self.params, self.filter_type)
