from abc import ABC, abstractmethod
from Filter import *
from FilterParameters import *
from FilterDesignMethod import *


class FilterFactory(ABC):
    """
    Factory that represents filter.
    The factory doesn't maintain any of the instances it creates.
    """

    def create_filter(self, params: Parameters, design_method: DesignMethod) -> Filter:
        """Retruns a new filter instance."""


class LowpassFilterFactory(FilterFactory):
    """ Factory creates lowpass filter instances"""

    def create_filter(self, params: Parameters, design_method: DesignMethod) -> Filter:
        return LowpassFilter(params, design_method)


class HighpassFilterFactory(FilterFactory):
    """ Factory creates highpass filter instances"""

    def create_filter(self, params: Parameters, design_method: DesignMethod) -> Filter:
        return HighpassFilter(params, design_method)


class BandpassFilterFactory(FilterFactory):
    """ Factory creates bandpass filter instances"""

    def create_filter(self, params: Parameters, design_method: DesignMethod) -> Filter:
        return BandpassFilter(params, design_method)


class BandstopFilterFactory(FilterFactory):
    """ Factory creates bandstop filter instances"""

    def create_filter(self, params: Parameters, design_method: DesignMethod) -> Filter:
        return BandstopFilter(params, design_method)

