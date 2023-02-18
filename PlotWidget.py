from PySide6.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvas, NavigationToolbar2QT
from matplotlib.figure import Figure


class NavigationToolbar2QTT(NavigationToolbar2QT):
    # only display the buttons we need
    NavigationToolbar2QT.toolitems = (
        ('Home', 'Reset original view', 'home', 'home'),
        ('Back', 'Back to previous view', 'back', 'back'),
        ('Forward', 'Forward to next view', 'forward', 'forward'),
        (None, None, None, None),
        ('Pan',
         'Left button pans, Right button zooms\n'
         'x/y fixes axis, CTRL fixes aspect',
         'move', 'pan'),
        ('Zoom', 'Zoom to rectangle\nx/y fixes axis', 'zoom_to_rect', 'zoom'),
        #('Subplots', 'Configure subplots', 'subplots', 'configure_subplots'),
        (None, None, None, None),
        ("Customize", "Edit axis, curve and image parameters",
         "qt4_editor_options", "edit_parameters"),
        ('Save', 'Save the figure', 'filesave', 'save_figure'),
    )

class PlotWidget(QWidget):

    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.toolbar)
        vertical_layout.addWidget(self.canvas)
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)
