from FilterFactory import *
from Filter import *


class DesignProcessor:
    def __init__(self, params: Parameters, design_method: DesignMethod, filter_type: str):
        self.params = params
        self.design_method = design_method
        self.factory = self.get_factory(filter_type)

    @staticmethod
    def get_factory(filter_type) -> FilterFactory:
        factories = {
            "Lowpass": LowpassFilterFactory(),
            "Highpass": HighpassFilterFactory(),
            "Bandpass": BandpassFilterFactory(),
            "Bandstop": BandstopFilterFactory()
        }
        if filter_type in factories:
            return factories[filter_type]

    def get_filter(self) -> Filter:
        return self.factory.create_filter(self.params, self.design_method)


