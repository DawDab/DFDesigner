from View import *
from Custom_Widgets.Widgets import *
from DesignProcessor import *
import numpy as np
from Plot import *
from matplotlib import patches


class Viewmodel(QMainWindow):
    def __init__(self, design_methods, filter_types, windows):
        super(Viewmodel, self).__init__()
        self.view = View()
        self.view.setupView(self)
        self.design_methods = design_methods
        self.filter_types = filter_types
        self.designed_filter = Filter

        # Setup globals
        for i in design_methods:
            self.view.responseComboBox.addItem(i, design_methods[i])
        for i in filter_types:
            self.view.typeComboBox.addItem(i)
        for i in windows:
            self.view.windowComboBox.addItem(i)
        for i in self.view.centralWidget.findChildren(QLineEdit):
            i.setValidator(QIntValidator())

        # Signals and slots
        self.view.responseComboBox.currentIndexChanged.connect(self.update_methods)
        self.view.typeComboBox.currentIndexChanged.connect(self.switch_freq_params)
        self.view.methodComboBox.currentIndexChanged.connect(self.switch_page_methods)
        self.view.methodComboBox.currentIndexChanged.connect(self.switch_freq_params)
        self.update_methods(self.view.responseComboBox.currentIndex())
        self.view.designButton.clicked.connect(self.design_button_clicked)
        self.view.saveFileButton.clicked.connect(self.save_to_csv)

        # JsonStyle load
        loadJsonStyle(self, self.view)

        # view show
        self.show()

    # Method which update View (methods depends on type FIR or IIR)
    def update_methods(self, index):
        self.view.methodComboBox.clear()
        methods = self.view.responseComboBox.itemData(index)
        if methods:
            self.view.methodComboBox.addItems(methods)

    # Method which update View (frequency parameters)
    def switch_freq_params(self):
        type_index = self.view.typeComboBox.currentText()
        method = self.view.methodComboBox.currentText()
        if method == "Least Squares":
            if type_index == "Lowpass" or type_index == "Highpass":
                self.view.freqParams.setCurrentWidget(self.view.single_band_page)
            else:
                self.view.freqParams.setCurrentWidget(self.view.multi_band_freqs)
        elif method == "Equiripple":
            if type_index == "Lowpass" or type_index == "Highpass":
                self.view.freqParams.setCurrentWidget(self.view.single_band_page)
                self.view.w_pb2_frame.hide()
                self.view.w_sb2_frame.hide()
            elif type_index == "Bandpass":
                self.view.w_sb2_frame.hide()
                self.view.w_pb2_frame.show()
                self.view.freqParams.setCurrentWidget(self.view.multi_band_freqs)
            elif type_index == "Bandstop":
                self.view.w_pb2_frame.hide()
                self.view.w_sb2_frame.show()#SB2
                self.view.freqParams.setCurrentWidget(self.view.multi_band_freqs)
            else:
                self.view.freqParams.setCurrentWidget(self.view.multi_band_freqs)
        else:
            if type_index == "Lowpass" or type_index == "Highpass":
                self.view.freqParams.setCurrentWidget(self.view.singleFreq)
            else:
                self.view.freqParams.setCurrentWidget(self.view.multiFreq)

    # Method which update View (input parameters for specific method)
    def switch_page_methods(self, index):
        methods = {
            "Window Method": self.view.windowParamsWidget,
            "Equiripple": self.view.equirippleParamsWidget,
            "Least Squares": self.view.leastSquaresParamsWidget,
            "Chebyshev 1": self.view.cheby1ParamsWidget,
            "Chebyshev 2": self.view.cheby2ParamsWidget,
            "Elliptic": self.view.ellipticParamsWidget,
            "Bessel": self.view.besselParamsWidget,
            "Butterworth": self.view.butterworthParamsWidget
        }
        if self.view.methodComboBox.itemText(index) in methods:
            self.view.methodParams.setCurrentWidget(methods[self.view.methodComboBox.itemText(index)])

    # Method which returns current set design method (takes valus from ComboBox)
    def get_method(self) -> DesignMethod:
        methods = {
            "Window Method": WindowMethod(self.view.windowComboBox.currentText().lower()),
            "Equiripple": EquirippleMethod(),
            "Least Squares": LeastSquaresMethod(),
            "Chebyshev 1": Chebyshev1Method(),
            "Chebyshev 2": Chebyshev2Method(),
            "Elliptic": EllipticMethod(),
            "Bessel": BesselMethod(),
            "Butterworth": ButterworthMethod()
        }
        if self.view.methodComboBox.currentText() in methods:
            return methods[self.view.methodComboBox.currentText()]

    # Method which return current set filter type (takes value from ComboBox)
    def get_filter_type(self):
        return self.view.typeComboBox.currentText()

    # Method which return current set filter type (takes value from ComboBox)
    def collect_params(self):
        # Dict to contain collected params
        params = {}
        # Collect common params ( Order, sampling freq ...)
        for i in self.view.common_params_Frame.findChildren(QLineEdit):
            if i.text() == '':
                if i.isVisible():
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setWindowTitle("Error")
                    error_txt = i.objectName() + " parameter cannot be empty!"
                    msg_box.setText(error_txt)
                    msg_box.exec_()
                else:
                    continue
            else:
                # Convert string to int
                params[i.objectName()] = int(i.text())
        for i in self.view.freqParams.currentWidget().findChildren(QLineEdit):
            if i.text() == '':
                if i.isVisible():
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setWindowTitle("Error")
                    error_txt = i.objectName() + " parameter cannot be empty!"
                    msg_box.setText(error_txt)
                    msg_box.exec_()
                else:
                    continue
            else:
                params[i.objectName()] = int(i.text())
        for i in self.view.methodParams.currentWidget().findChildren(QComboBox):
            params[i.objectName()] = i.currentText()
        for i in self.view.methodParams.currentWidget().findChildren(QLineEdit):
            if i.text() == '':
                if i.isVisible():
                    msg_box = QMessageBox()
                    msg_box.setIcon(QMessageBox.Critical)
                    msg_box.setWindowTitle("Error")
                    error_txt = i.objectName() + " parameter cannot be empty!"
                    msg_box.setText(error_txt)
                    msg_box.exec_()
                else:
                    continue
            else:
                params[i.objectName()] = int(i.text())
        return params

    def design_button_clicked(self):
        # Design section
        collected = self.collect_params()
        params = Parameters(**collected)
        method = self.get_method()
        filter_type = self.get_filter_type()
        designer = DesignProcessor(params, method, filter_type)
        try:
            self.designed_filter = designer.get_filter()
            self.plot_filter(self.designed_filter, MagnitudePlot(), self.view.MagnitudePlotWidget)
            self.plot_filter(self.designed_filter, PhasePlot(), self.view.phasePlotWidget)
            self.plot_zeros_poles(self.designed_filter)
            self.plot_impulse(self.designed_filter)
            self.load_data_to_table(self.designed_filter)

        except ValueError as e:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Critical)
            msg_box.setWindowTitle("Error")
            error_txt = str(e)
            msg_box.setText(error_txt)
            msg_box.exec_()

    def plot_filter(self, filter: Filter, plt: Plot, plt_widget: PlotWidget):
        plt_widget.canvas.axes.cla()
        val = plt.return_plot(filter)
        plt_widget.canvas.axes.plot(val[0], val[1], color='g')
        plt_widget.canvas.axes.set_title(plt.title)
        plt_widget.canvas.axes.set_ylabel(plt.y_label, color='g')
        plt_widget.canvas.axes.set_xlabel(plt.x_label)
        plt_widget.canvas.axes.grid(visible=True)
        plt_widget.canvas.draw()

    def plot_zeros_poles(self, filter: Filter):

        uc = patches.Circle((0, 0), radius=1, fill=False,
                            color='black', ls='dashed')
        self.view.pole_zeroPlotWidget.canvas.axes.cla()
        if isinstance(filter.method, IirMethod):
            z, p, k = signal.tf2zpk(filter.filter_coefficients[0], filter.filter_coefficients[1])
        else:
            z, p, k = signal.tf2zpk(filter.filter_coefficients, 1)
        self.view.pole_zeroPlotWidget.canvas.axes.grid(visible=True)
        self.view.pole_zeroPlotWidget.canvas.axes.plot(np.real(z), np.imag(z), 'og', markerfacecolor='none')
        self.view.pole_zeroPlotWidget.canvas.axes.plot(np.real(p), np.imag(p), 'xr')
        self.view.pole_zeroPlotWidget.canvas.axes.add_patch(uc)
        self.view.pole_zeroPlotWidget.canvas.axes.set_xlabel("Real Part")
        self.view.pole_zeroPlotWidget.canvas.axes.set_ylabel("Imaginary Part")
        self.view.pole_zeroPlotWidget.canvas.axes.set_title("Pole-zero plot")
        self.view.pole_zeroPlotWidget.canvas.draw()

    def plot_impulse(self, filter: Filter):
        self.view.ImpulsePlotWidget.canvas.axes.cla()
        self.view.ImpulsePlotWidget.canvas.axes.grid(visible=True)
        self.view.ImpulsePlotWidget.canvas.axes.set_xlabel("Samples")
        self.view.ImpulsePlotWidget.canvas.axes.set_ylabel("Amplitude")
        self.view.ImpulsePlotWidget.canvas.axes.set_title("Impulse response")
        if isinstance(filter.method, IirMethod):
            imp = signal.lfilter(filter.filter_coefficients[0], filter.filter_coefficients[1], signal.unit_impulse(80))
            self.view.ImpulsePlotWidget.canvas.axes.stem(imp, 'g')
        else:
            self.view.ImpulsePlotWidget.canvas.axes.stem(filter.filter_coefficients, 'g')

        self.view.ImpulsePlotWidget.canvas.draw()

    def load_data_to_table(self, filter: Filter):
        self.view.coeffsTableWidget.clear()
        self.view.coeffsTableWidget.setColumnCount(2)
        self.view.coeffsTableWidget.setHorizontalHeaderLabels(["b", "a"])
        b = self.view.coeffsTableWidget.horizontalHeaderItem(0)
        a = self.view.coeffsTableWidget.horizontalHeaderItem(1)
        b.setToolTip("Numerator coefficients")
        a.setToolTip("Denumerator coefficients")
        if isinstance(filter.method, FirMethod):
            self.view.coeffsTableWidget.setRowCount(len(filter.filter_coefficients))
            for i in range(len(filter.filter_coefficients)):
                self.view.coeffsTableWidget.setItem(i, 0,
                                                    QtWidgets.QTableWidgetItem(f'{filter.filter_coefficients[i]:.5f}'))

        elif isinstance(filter.method, IirMethod):
            self.view.coeffsTableWidget.setRowCount(len(filter.filter_coefficients[0]))
            for i in range(len(filter.filter_coefficients[0])):
                self.view.coeffsTableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(
                    f'{filter.filter_coefficients[0][i]:.5f}'))
                for j in range(len(filter.filter_coefficients[1])):
                    self.view.coeffsTableWidget.setItem(j, 1, QtWidgets.QTableWidgetItem(
                        f'{filter.filter_coefficients[1][j]:.5f}'))
        self.view.coeffsTableWidget.resizeColumnsToContents()

    def save_to_csv(self):
        file_name, _ = QFileDialog.getSaveFileName(self, 'Save File', '', 'CSV Files (*.csv)')

        if file_name:
            np.savetxt(file_name, self.designed_filter.filter_coefficients, delimiter=',')
