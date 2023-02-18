"""
Author: Dawid Dabrowski
Maintainer: Dawid Dabrowski
Contact: d.dabrowski1999@gmail.com
"""

from PySide6.QtWidgets import QApplication
from Viewmodel import Viewmodel
import sys

# GLOABL VARIABLES
# All implemented methods in FilterDesignMethod.py
DESIGN_METHODS = {'FIR': ["Window Method", "Equiripple", "Least Squares"],
                  'IIR': ["Bessel", "Butterworth", "Elliptic", "Chebyshev 1", "Chebyshev 2"]
                  }
# All implemented filters in Filter.py
FILTER_TYPES = ["Lowpass", "Highpass", "Bandpass", "Bandstop"]

# Defined windows in Scipy
WINDOWS = ["Hamming", "Hann", "Blackman", "Bohman", "Blackmanharris", "Taylor", "Boxcar"]

app = QApplication(sys.argv)
window = Viewmodel(DESIGN_METHODS, FILTER_TYPES, WINDOWS)
app.exec_()
