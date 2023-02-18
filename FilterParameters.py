from dataclasses import dataclass


@dataclass
class Parameters:
    """This dataclass represents filter parameters"""
    fs: float = None              # sampling frequency
    filter_order: int = None      # filter order
    fc: int = None                # cutoff frequency
    fc1: int = None               # lower cutoff frequency
    fc2: int = None               # upper cutoff frequency
    freq_pass1: float = None      # passband frequency
    freq_stop1: float = None      # stopband frequency
    freq_pass2: float = None      # upper passband frequency
    freq_stop2: float = None      # upper stopband frequency
    grid_density: int = None      # density of the frequency grid
    weight_pass1: float = None    # weight for the passband
    weight_stop1: float = None    # weight for the stopband
    weight_pass2: float = None    # upper weight for the passband
    weight_stop2: float = None    # upper weight for the stopband
    r_p: float = None             # maximum passband ripple in dB
    r_s: float = None             # minimum stopband attenuation in dB
    window: str = None            # window

