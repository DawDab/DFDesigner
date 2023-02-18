# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceEZBdcB.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
                           QFont, QFontDatabase, QGradient, QIcon,
                           QImage, QKeySequence, QLinearGradient, QPainter,
                           QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
                               QHBoxLayout, QHeaderView, QLabel, QLineEdit,
                               QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
                               QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
                               QVBoxLayout, QWidget)

from Custom_Widgets.Widgets import (QCustomSlideMenu, QCustomStackedWidget)
from PlotWidget import PlotWidget
import icons.resources_rc


class View(object):
    def setupView(self, View):
        if not View.objectName():
            View.setObjectName(u"View")
        View.resize(1049, 787)
        View.setStyleSheet(u"*{\n"
                           "font:solid Segoe UI;\n"
                           "font-weight:bold;\n"
                           "background-color:transparent;\n"
                           "background: none;\n"
                           "padding: 0;\n"
                           "margin: 0;\n"
                           "\n"
                           "}\n"
                           "#centralwidget{\n"
                           "	background-color:#f5f6fa;\n"
                           "}\n"
                           "#leftMenuSubContainer{\n"
                           "	background-color:#a5d6a7;\n"
                           "}\n"
                           "#leftMenuSubContainer QPushButton{\n"
                           "	text-align: left;\n"
                           "	padding:5px 10px;\n"
                           "	border-top-left-radius:15px;\n"
                           "    border-bottom-left-radius:15px;\n"
                           "}\n"
                           "\n"
                           "")
        self.centralWidget = QWidget(View)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setMinimumSize(QSize(0, 700))
        self.centralWidget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.centralWidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralWidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setMinimumSize(QSize(0, 300))
        self.leftMenuContainer.setMaximumSize(QSize(45, 16777215))
        self.gridLayout = QGridLayout(self.leftMenuContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.leftMenuSubContainer.setStyleSheet(u"*{border:none;}")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuFrame = QFrame(self.leftMenuSubContainer)
        self.menuFrame.setObjectName(u"menuFrame")
        self.menuFrame.setFrameShape(QFrame.StyledPanel)
        self.menuFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.menuFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuButton = QPushButton(self.menuFrame)
        self.menuButton.setObjectName(u"menuButton")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setBold(True)
        font.setItalic(False)
        self.menuButton.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuButton.setIcon(icon)
        self.menuButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.menuButton)

        self.verticalLayout_2.addWidget(self.menuFrame, 0, Qt.AlignTop)

        self.contentFrame = QFrame(self.leftMenuSubContainer)
        self.contentFrame.setObjectName(u"contentFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.contentFrame.sizePolicy().hasHeightForWidth())
        self.contentFrame.setSizePolicy(sizePolicy)
        self.contentFrame.setFrameShape(QFrame.StyledPanel)
        self.contentFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.contentFrame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.specificationButton = QPushButton(self.contentFrame)
        self.specificationButton.setObjectName(u"specificationButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.specificationButton.sizePolicy().hasHeightForWidth())
        self.specificationButton.setSizePolicy(sizePolicy1)
        self.specificationButton.setFont(font)
        self.specificationButton.setStyleSheet(u"background-color: #d7ffd9;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/sliders.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.specificationButton.setIcon(icon1)
        self.specificationButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.specificationButton)

        self.coefficientsButton = QPushButton(self.contentFrame)
        self.coefficientsButton.setObjectName(u"coefficientsButton")
        self.coefficientsButton.setFont(font)
        icon2 = QIcon()
        icon2.addFile(u":/icons/slack.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.coefficientsButton.setIcon(icon2)
        self.coefficientsButton.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.coefficientsButton)

        self.verticalLayout_2.addWidget(self.contentFrame, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.helpFrame = QFrame(self.leftMenuSubContainer)
        self.helpFrame.setObjectName(u"helpFrame")
        sizePolicy.setHeightForWidth(self.helpFrame.sizePolicy().hasHeightForWidth())
        self.helpFrame.setSizePolicy(sizePolicy)
        self.helpFrame.setFrameShape(QFrame.StyledPanel)
        self.helpFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.helpFrame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.helpButton = QPushButton(self.helpFrame)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setFont(font)
        icon3 = QIcon()
        icon3.addFile(u":/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon3)
        self.helpButton.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.helpButton)

        self.verticalLayout_2.addWidget(self.helpFrame, 0, Qt.AlignBottom)

        self.gridLayout.addWidget(self.leftMenuSubContainer, 0, 0, 1, 1)

        self.horizontalLayout.addWidget(self.leftMenuContainer)

        self.centerMenuContainer = QWidget(self.centralWidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.centerMenuContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuContainer.setSizePolicy(sizePolicy2)
        self.centerMenuContainer.setMinimumSize(QSize(0, 300))
        self.centerMenuContainer.setMaximumSize(QSize(500, 16777215))
        self.centerMenuContainer.setStyleSheet(u"background-color: #d7ffd9;")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        sizePolicy.setHeightForWidth(self.centerMenuSubContainer.sizePolicy().hasHeightForWidth())
        self.centerMenuSubContainer.setSizePolicy(sizePolicy)
        self.centerMenuSubContainer.setStyleSheet(u"background-color: #d7ffd9;\n"
                                                  "")
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.mainMenu = QCustomStackedWidget(self.centerMenuSubContainer)
        self.mainMenu.setObjectName(u"mainMenu")
        self.specificationPage = QWidget()
        self.specificationPage.setObjectName(u"specificationPage")
        self.verticalLayout_9 = QVBoxLayout(self.specificationPage)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.titleFrame = QFrame(self.specificationPage)
        self.titleFrame.setObjectName(u"titleFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.titleFrame.sizePolicy().hasHeightForWidth())
        self.titleFrame.setSizePolicy(sizePolicy3)
        self.titleFrame.setFrameShape(QFrame.StyledPanel)
        self.titleFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.titleFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 30, -1, -1)
        self.titleLabel = QLabel(self.titleFrame)
        self.titleLabel.setObjectName(u"titleLabel")
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(False)
        self.titleLabel.setFont(font1)
        self.titleLabel.setAlignment(Qt.AlignHCenter | Qt.AlignTop)

        self.horizontalLayout_4.addWidget(self.titleLabel, 0, Qt.AlignLeft)

        self.verticalLayout_9.addWidget(self.titleFrame, 0, Qt.AlignTop)

        self.specsFrame = QFrame(self.specificationPage)
        self.specsFrame.setObjectName(u"specsFrame")
        sizePolicy3.setHeightForWidth(self.specsFrame.sizePolicy().hasHeightForWidth())
        self.specsFrame.setSizePolicy(sizePolicy3)
        self.specsFrame.setStyleSheet(u"")
        self.specsFrame.setFrameShape(QFrame.StyledPanel)
        self.specsFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.specsFrame)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 2, 10, 2)
        self.typeComboBox = QComboBox(self.specsFrame)
        self.typeComboBox.setObjectName(u"typeComboBox")
        self.typeComboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.typeComboBox)

        self.responseComboBox = QComboBox(self.specsFrame)
        self.responseComboBox.setObjectName(u"responseComboBox")
        self.responseComboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.responseComboBox)

        self.methodComboBox = QComboBox(self.specsFrame)
        self.methodComboBox.setObjectName(u"methodComboBox")
        self.methodComboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.methodComboBox)

        self.verticalLayout_9.addWidget(self.specsFrame)

        self.designBtnFrame = QFrame(self.specificationPage)
        self.designBtnFrame.setObjectName(u"designBtnFrame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.designBtnFrame.sizePolicy().hasHeightForWidth())
        self.designBtnFrame.setSizePolicy(sizePolicy4)
        self.designBtnFrame.setMaximumSize(QSize(16777215, 16777215))
        self.designBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.designBtnFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.designBtnFrame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.designButton = QPushButton(self.designBtnFrame)
        self.designButton.setObjectName(u"designButton")
        self.designButton.setFont(font)
        self.designButton.setStyleSheet(u"QPushButton {\n"
                                        "    background-color: lightgray;\n"
                                        "    border-style: outset;\n"
                                        "    border-width: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: black;\n"
                                        "    font: bold 14px;\n"
                                        "    min-width: 10em;\n"
                                        "    padding: 6px;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: #32CC99;\n"
                                        "    border-style: inset;\n"
                                        "}\n"
                                        "")

        self.horizontalLayout_14.addWidget(self.designButton)

        self.verticalLayout_9.addWidget(self.designBtnFrame)

        self.frame_2 = QFrame(self.specificationPage)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy4.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy4)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.common_params_Frame = QFrame(self.frame_2)
        self.common_params_Frame.setObjectName(u"common_params_Frame")
        sizePolicy.setHeightForWidth(self.common_params_Frame.sizePolicy().hasHeightForWidth())
        self.common_params_Frame.setSizePolicy(sizePolicy)
        self.common_params_Frame.setFrameShape(QFrame.StyledPanel)
        self.common_params_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.common_params_Frame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_5 = QFrame(self.common_params_Frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.orderLabel_4 = QLabel(self.frame_5)
        self.orderLabel_4.setObjectName(u"orderLabel_4")
        self.orderLabel_4.setFont(font)
        self.orderLabel_4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.orderLabel_4)

        self.orderLineEdit_4 = QLineEdit(self.frame_5)
        self.orderLineEdit_4.setObjectName(u"filter_order")
        self.orderLineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.orderLineEdit_4)

        self.verticalLayout_10.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.common_params_Frame)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 1, 0)
        self.sampFreqLabel_4 = QLabel(self.frame_6)
        self.sampFreqLabel_4.setObjectName(u"sampFreqLabel_4")
        self.sampFreqLabel_4.setFont(font)
        self.sampFreqLabel_4.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.sampFreqLabel_4)

        self.sampFreqLineEdit_4 = QLineEdit(self.frame_6)
        self.sampFreqLineEdit_4.setObjectName(u"fs")
        self.sampFreqLineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.sampFreqLineEdit_4)

        self.verticalLayout_10.addWidget(self.frame_6)

        self.horizontalLayout_15.addWidget(self.common_params_Frame)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_11)
        self.verticalLayout_31.setSpacing(6)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(9, 9, 9, 9)
        self.freqParams = QStackedWidget(self.frame_11)
        self.freqParams.setObjectName(u"freqParams")
        sizePolicy.setHeightForWidth(self.freqParams.sizePolicy().hasHeightForWidth())
        self.freqParams.setSizePolicy(sizePolicy)
        self.singleFreq = QWidget()
        self.singleFreq.setObjectName(u"singleFreq")
        sizePolicy4.setHeightForWidth(self.singleFreq.sizePolicy().hasHeightForWidth())
        self.singleFreq.setSizePolicy(sizePolicy4)
        self.verticalLayout_28 = QVBoxLayout(self.singleFreq)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.fc11Frame = QFrame(self.singleFreq)
        self.fc11Frame.setObjectName(u"fc11Frame")
        sizePolicy.setHeightForWidth(self.fc11Frame.sizePolicy().hasHeightForWidth())
        self.fc11Frame.setSizePolicy(sizePolicy)
        self.fc11Frame.setFrameShape(QFrame.StyledPanel)
        self.fc11Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.fc11Frame)
        self.horizontalLayout_31.setSpacing(5)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 9, 0)
        self.fc11Label = QLabel(self.fc11Frame)
        self.fc11Label.setObjectName(u"fc11Label")
        self.fc11Label.setFont(font)

        self.horizontalLayout_31.addWidget(self.fc11Label)

        self.Fc = QLineEdit(self.fc11Frame)
        self.Fc.setObjectName(u"fc")
        self.Fc.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_31.addWidget(self.Fc)

        self.verticalLayout_28.addWidget(self.fc11Frame)

        self.frame_3 = QFrame(self.singleFreq)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")

        self.verticalLayout_28.addWidget(self.frame_3)

        self.freqParams.addWidget(self.singleFreq)
        self.single_band_page = QWidget()
        self.single_band_page.setObjectName(u"single_band_page")
        self.verticalLayout_11 = QVBoxLayout(self.single_band_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 5, 0)
        self.frame_7 = QFrame(self.single_band_page)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.fc2Label_8 = QLabel(self.frame_7)
        self.fc2Label_8.setObjectName(u"fc2Label_8")
        self.fc2Label_8.setFont(font)

        self.horizontalLayout_11.addWidget(self.fc2Label_8)

        self.fc2lineEdit_12 = QLineEdit(self.frame_7)
        self.fc2lineEdit_12.setObjectName(u"freq_stop1")
        self.fc2lineEdit_12.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.fc2lineEdit_12)

        self.verticalLayout_11.addWidget(self.frame_7)

        self.frame_15 = QFrame(self.single_band_page)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, -1, 0, -1)
        self.fc2Label_12 = QLabel(self.frame_15)
        self.fc2Label_12.setObjectName(u"fc2Label_12")
        self.fc2Label_12.setFont(font)

        self.horizontalLayout_12.addWidget(self.fc2Label_12)

        self.fc2lineEdit_13 = QLineEdit(self.frame_15)
        self.fc2lineEdit_13.setObjectName(u"freq_pass1")
        self.fc2lineEdit_13.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_12.addWidget(self.fc2lineEdit_13)

        self.verticalLayout_11.addWidget(self.frame_15)

        self.freqParams.addWidget(self.single_band_page)
        self.multi_band_freqs \
            = QWidget()
        self.multi_band_freqs \
            .setObjectName(u"multi_band_freqs"
                           u"")
        sizePolicy4.setHeightForWidth(self.multi_band_freqs
                                      .sizePolicy().hasHeightForWidth())
        self.multi_band_freqs \
            .setSizePolicy(sizePolicy4)
        self.verticalLayout_29 = QVBoxLayout(self.multi_band_freqs
                                             )
        self.verticalLayout_29.setSpacing(0)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(0, -1, 0, -1)
        self.frame_18 = QFrame(self.multi_band_freqs
                               )
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_32.setSpacing(4)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(5, 4, 8, 4)
        self.fc2Label_6 = QLabel(self.frame_18)
        self.fc2Label_6.setObjectName(u"fc2Label_6")
        self.fc2Label_6.setFont(font)

        self.horizontalLayout_32.addWidget(self.fc2Label_6)

        self.fc2lineEdit_7 = QLineEdit(self.frame_18)
        self.fc2lineEdit_7.setObjectName(u"freq_stop1")
        self.fc2lineEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_32.addWidget(self.fc2lineEdit_7)

        self.verticalLayout_29.addWidget(self.frame_18)

        self.frame_19 = QFrame(self.multi_band_freqs
                               )
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_33.setSpacing(4)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(5, 4, 8, 4)
        self.fc2Label_2 = QLabel(self.frame_19)
        self.fc2Label_2.setObjectName(u"fc2Label_2")
        self.fc2Label_2.setFont(font)

        self.horizontalLayout_33.addWidget(self.fc2Label_2)

        self.fc2lineEdit_6 = QLineEdit(self.frame_19)
        self.fc2lineEdit_6.setObjectName(u"freq_pass1")
        self.fc2lineEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_33.addWidget(self.fc2lineEdit_6)

        self.verticalLayout_29.addWidget(self.frame_19)

        self.frame_20 = QFrame(self.multi_band_freqs
                               )
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_34.setSpacing(4)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(5, 4, 8, 4)
        self.fc2Label_17 = QLabel(self.frame_20)
        self.fc2Label_17.setObjectName(u"fc2Label_17")
        self.fc2Label_17.setFont(font)

        self.horizontalLayout_34.addWidget(self.fc2Label_17)

        self.fc2lineEdit_2 = QLineEdit(self.frame_20)
        self.fc2lineEdit_2.setObjectName(u"freq_stop2")
        self.fc2lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_34.addWidget(self.fc2lineEdit_2)

        self.verticalLayout_29.addWidget(self.frame_20)

        self.frame_21 = QFrame(self.multi_band_freqs
                               )
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_21)
        self.horizontalLayout_35.setSpacing(4)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(5, 4, 8, 4)
        self.fc2Label = QLabel(self.frame_21)
        self.fc2Label.setObjectName(u"fc2Label")
        self.fc2Label.setFont(font)

        self.horizontalLayout_35.addWidget(self.fc2Label)

        self.fc2lineEdit = QLineEdit(self.frame_21)
        self.fc2lineEdit.setObjectName(u"freq_pass2")
        self.fc2lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_35.addWidget(self.fc2lineEdit)

        self.verticalLayout_29.addWidget(self.frame_21)

        self.freqParams.addWidget(self.multi_band_freqs
                                  )
        self.multiFreq = QWidget()
        self.multiFreq.setObjectName(u"multiFreq")
        sizePolicy4.setHeightForWidth(self.multiFreq.sizePolicy().hasHeightForWidth())
        self.multiFreq.setSizePolicy(sizePolicy4)
        self.verticalLayout_30 = QVBoxLayout(self.multiFreq)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.fc1Frame = QFrame(self.multiFreq)
        self.fc1Frame.setObjectName(u"fc1Frame")
        sizePolicy.setHeightForWidth(self.fc1Frame.sizePolicy().hasHeightForWidth())
        self.fc1Frame.setSizePolicy(sizePolicy)
        self.fc1Frame.setFrameShape(QFrame.StyledPanel)
        self.fc1Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_36 = QHBoxLayout(self.fc1Frame)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.fc1Label = QLabel(self.fc1Frame)
        self.fc1Label.setObjectName(u"fc1Label")
        self.fc1Label.setFont(font)

        self.horizontalLayout_36.addWidget(self.fc1Label)

        self.fc1lineEdit = QLineEdit(self.fc1Frame)
        self.fc1lineEdit.setObjectName(u"fc1")
        self.fc1lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_36.addWidget(self.fc1lineEdit)

        self.verticalLayout_30.addWidget(self.fc1Frame)

        self.fc2Frame = QFrame(self.multiFreq)
        self.fc2Frame.setObjectName(u"fc2Frame")
        sizePolicy.setHeightForWidth(self.fc2Frame.sizePolicy().hasHeightForWidth())
        self.fc2Frame.setSizePolicy(sizePolicy)
        self.fc2Frame.setFrameShape(QFrame.StyledPanel)
        self.fc2Frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.fc2Frame)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.fc2Label_7 = QLabel(self.fc2Frame)
        self.fc2Label_7.setObjectName(u"fc2Label_7")
        self.fc2Label_7.setFont(font)

        self.horizontalLayout_37.addWidget(self.fc2Label_7)

        self.fc2lineEdit_8 = QLineEdit(self.fc2Frame)
        self.fc2lineEdit_8.setObjectName(u"fc2")
        self.fc2lineEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_37.addWidget(self.fc2lineEdit_8)

        self.verticalLayout_30.addWidget(self.fc2Frame)

        self.freqParams.addWidget(self.multiFreq)

        self.verticalLayout_31.addWidget(self.freqParams)

        self.horizontalLayout_15.addWidget(self.frame_11)

        self.verticalLayout_9.addWidget(self.frame_2)

        self.methodParams = QStackedWidget(self.specificationPage)
        self.methodParams.setObjectName(u"methodParams")
        sizePolicy4.setHeightForWidth(self.methodParams.sizePolicy().hasHeightForWidth())
        self.methodParams.setSizePolicy(sizePolicy4)
        self.windowParamsWidget = QWidget()
        self.windowParamsWidget.setObjectName(u"windowParamsWidget")
        self.verticalLayout_8 = QVBoxLayout(self.windowParamsWidget)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 50)
        self.windowFrame = QFrame(self.windowParamsWidget)
        self.windowFrame.setObjectName(u"windowFrame")
        sizePolicy3.setHeightForWidth(self.windowFrame.sizePolicy().hasHeightForWidth())
        self.windowFrame.setSizePolicy(sizePolicy3)
        self.windowFrame.setFrameShape(QFrame.StyledPanel)
        self.windowFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.windowFrame)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.windowLabel = QLabel(self.windowFrame)
        self.windowLabel.setObjectName(u"windowLabel")
        self.windowLabel.setFont(font)
        self.windowLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.windowLabel)

        self.windowComboBox = QComboBox(self.windowFrame)
        # self.windowComboBox.addItem("")
        self.windowComboBox.setObjectName(u"window")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.windowComboBox.sizePolicy().hasHeightForWidth())
        self.windowComboBox.setSizePolicy(sizePolicy5)
        self.windowComboBox.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_5.addWidget(self.windowComboBox)

        self.verticalLayout_8.addWidget(self.windowFrame)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_5)

        self.methodParams.addWidget(self.windowParamsWidget)
        self.leastSquaresParamsWidget = QWidget()
        self.leastSquaresParamsWidget.setObjectName(u"leastSquaresParamsWidget")
        self.verticalLayout_19 = QVBoxLayout(self.leastSquaresParamsWidget)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.methodParams.addWidget(self.leastSquaresParamsWidget)
        self.equirippleParamsWidget = QWidget()
        self.equirippleParamsWidget.setObjectName(u"equirippleParamsWidget")
        self.verticalLayout_20 = QVBoxLayout(self.equirippleParamsWidget)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_14 = QFrame(self.equirippleParamsWidget)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, -1, -1, -1)
        self.fc2Label_11 = QLabel(self.frame_14)
        self.fc2Label_11.setObjectName(u"fc2Label_11")
        self.fc2Label_11.setFont(font)

        self.horizontalLayout_21.addWidget(self.fc2Label_11)

        self.fc2lineEdit_11 = QLineEdit(self.frame_14)
        self.fc2lineEdit_11.setObjectName(u"grid_density")
        self.fc2lineEdit_11.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_21.addWidget(self.fc2lineEdit_11)

        self.verticalLayout_20.addWidget(self.frame_14)

        self.label_2 = QLabel(self.equirippleParamsWidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_20.addWidget(self.label_2)

        self.frame_8 = QFrame(self.equirippleParamsWidget)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_17.setSpacing(12)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, -1, -1, -1)
        self.fc2Label_3 = QLabel(self.frame_8)
        self.fc2Label_3.setObjectName(u"fc2Label_3")
        self.fc2Label_3.setFont(font)

        self.horizontalLayout_17.addWidget(self.fc2Label_3)

        self.fc2lineEdit_3 = QLineEdit(self.frame_8)
        self.fc2lineEdit_3.setObjectName(u"weight_pass1")
        self.fc2lineEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_17.addWidget(self.fc2lineEdit_3)

        self.verticalLayout_20.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.equirippleParamsWidget)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_18.setSpacing(15)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, -1, -1, -1)
        self.fc2Label_4 = QLabel(self.frame_9)
        self.fc2Label_4.setObjectName(u"fc2Label_4")
        self.fc2Label_4.setFont(font)

        self.horizontalLayout_18.addWidget(self.fc2Label_4)

        self.fc2lineEdit_4 = QLineEdit(self.frame_9)
        self.fc2lineEdit_4.setObjectName(u"weight_stop1")
        self.fc2lineEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.fc2lineEdit_4)

        self.verticalLayout_20.addWidget(self.frame_9)

        self.w_pb2_frame = QFrame(self.equirippleParamsWidget)
        self.w_pb2_frame.setObjectName(u"w_pb2_frame")
        self.w_pb2_frame.setFrameShape(QFrame.StyledPanel)
        self.w_pb2_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.w_pb2_frame)
        self.horizontalLayout_20.setSpacing(12)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, -1, -1, -1)
        self.fc2Label_5 = QLabel(self.w_pb2_frame)
        self.fc2Label_5.setObjectName(u"fc2Label_5")
        self.fc2Label_5.setFont(font)

        self.horizontalLayout_20.addWidget(self.fc2Label_5)

        self.fc2lineEdit_5 = QLineEdit(self.w_pb2_frame)
        self.fc2lineEdit_5.setObjectName(u"weight_pass2")
        self.fc2lineEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_20.addWidget(self.fc2lineEdit_5)

        self.verticalLayout_20.addWidget(self.w_pb2_frame)

        self.w_sb2_frame = QFrame(self.equirippleParamsWidget)
        self.w_sb2_frame.setObjectName(u"w_sb2_frame")
        self.w_sb2_frame.setFrameShape(QFrame.StyledPanel)
        self.w_sb2_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.w_sb2_frame)
        self.horizontalLayout_24.setSpacing(15)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, -1, -1, -1)
        self.fc2Label_15 = QLabel(self.w_sb2_frame)
        self.fc2Label_15.setObjectName(u"fc2Label_15")
        self.fc2Label_15.setFont(font)

        self.horizontalLayout_24.addWidget(self.fc2Label_15)

        self.fc2lineEdit_16 = QLineEdit(self.w_sb2_frame)
        self.fc2lineEdit_16.setObjectName(u"weight_stop2")
        self.fc2lineEdit_16.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_24.addWidget(self.fc2lineEdit_16)

        self.verticalLayout_20.addWidget(self.w_sb2_frame)

        self.methodParams.addWidget(self.equirippleParamsWidget)
        self.butterworthParamsWidget = QWidget()
        self.butterworthParamsWidget.setObjectName(u"butterworthParamsWidget")
        self.verticalLayout_22 = QVBoxLayout(self.butterworthParamsWidget)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.methodParams.addWidget(self.butterworthParamsWidget)
        self.ellipticParamsWidget = QWidget()
        self.ellipticParamsWidget.setObjectName(u"ellipticParamsWidget")
        self.verticalLayout_18 = QVBoxLayout(self.ellipticParamsWidget)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_16 = QFrame(self.ellipticParamsWidget)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy4.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy4)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.fc2Label_13 = QLabel(self.frame_16)
        self.fc2Label_13.setObjectName(u"fc2Label_13")
        self.fc2Label_13.setFont(font)

        self.horizontalLayout_22.addWidget(self.fc2Label_13)

        self.fc2lineEdit_14 = QLineEdit(self.frame_16)
        self.fc2lineEdit_14.setObjectName(u"r_p")
        self.fc2lineEdit_14.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_22.addWidget(self.fc2lineEdit_14)

        self.verticalLayout_18.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.ellipticParamsWidget)
        self.frame_17.setObjectName(u"frame_17")
        sizePolicy4.setHeightForWidth(self.frame_17.sizePolicy().hasHeightForWidth())
        self.frame_17.setSizePolicy(sizePolicy4)
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.fc2Label_14 = QLabel(self.frame_17)
        self.fc2Label_14.setObjectName(u"fc2Label_14")
        self.fc2Label_14.setFont(font)

        self.horizontalLayout_23.addWidget(self.fc2Label_14)

        self.fc2lineEdit_15 = QLineEdit(self.frame_17)
        self.fc2lineEdit_15.setObjectName(u"r_s")
        self.fc2lineEdit_15.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_23.addWidget(self.fc2lineEdit_15)

        self.verticalLayout_18.addWidget(self.frame_17)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_6)

        self.methodParams.addWidget(self.ellipticParamsWidget)
        self.cheby1ParamsWidget = QWidget()
        self.cheby1ParamsWidget.setObjectName(u"cheby1ParamsWidget")
        self.verticalLayout_16 = QVBoxLayout(self.cheby1ParamsWidget)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_12 = QFrame(self.cheby1ParamsWidget)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy4.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy4)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.fc2Label_9 = QLabel(self.frame_12)
        self.fc2Label_9.setObjectName(u"fc2Label_9")
        self.fc2Label_9.setFont(font)

        self.horizontalLayout_7.addWidget(self.fc2Label_9)

        self.fc2lineEdit_9 = QLineEdit(self.frame_12)
        self.fc2lineEdit_9.setObjectName(u"r_p")
        self.fc2lineEdit_9.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.fc2lineEdit_9)

        self.verticalLayout_16.addWidget(self.frame_12)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)

        self.methodParams.addWidget(self.cheby1ParamsWidget)
        self.cheby2ParamsWidget = QWidget()
        self.cheby2ParamsWidget.setObjectName(u"cheby2ParamsWidget")
        self.verticalLayout_17 = QVBoxLayout(self.cheby2ParamsWidget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_13 = QFrame(self.cheby2ParamsWidget)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy4.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy4)
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.fc2Label_10 = QLabel(self.frame_13)
        self.fc2Label_10.setObjectName(u"fc2Label_10")
        self.fc2Label_10.setFont(font)

        self.horizontalLayout_8.addWidget(self.fc2Label_10)

        self.fc2lineEdit_10 = QLineEdit(self.frame_13)
        self.fc2lineEdit_10.setObjectName(u"r_s")
        self.fc2lineEdit_10.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.fc2lineEdit_10)

        self.verticalLayout_17.addWidget(self.frame_13)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_17.addItem(self.verticalSpacer_4)

        self.methodParams.addWidget(self.cheby2ParamsWidget)
        self.besselParamsWidget = QWidget()
        self.besselParamsWidget.setObjectName(u"besselParamsWidget")
        self.methodParams.addWidget(self.besselParamsWidget)

        self.verticalLayout_9.addWidget(self.methodParams)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.mainMenu.addWidget(self.specificationPage)
        self.coefficientsPage = QWidget()
        self.coefficientsPage.setObjectName(u"coefficientsPage")
        self.coefficientsPage.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_12 = QVBoxLayout(self.coefficientsPage)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.tableFrame = QFrame(self.coefficientsPage)
        self.tableFrame.setObjectName(u"tableFrame")
        self.tableFrame.setFrameShape(QFrame.StyledPanel)
        self.tableFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.tableFrame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(25, 10, 0, 0)
        self.saveBtnFrame = QFrame(self.tableFrame)
        self.saveBtnFrame.setObjectName(u"saveBtnFrame")
        sizePolicy4.setHeightForWidth(self.saveBtnFrame.sizePolicy().hasHeightForWidth())
        self.saveBtnFrame.setSizePolicy(sizePolicy4)
        self.saveBtnFrame.setFrameShape(QFrame.StyledPanel)
        self.saveBtnFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.saveBtnFrame)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.saveFileButton = QPushButton(self.saveBtnFrame)
        self.saveFileButton.setObjectName(u"saveFileButton")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.saveFileButton.sizePolicy().hasHeightForWidth())
        self.saveFileButton.setSizePolicy(sizePolicy6)
        self.saveFileButton.setStyleSheet(u"QPushButton {\n"
                                          "    background-color: lightgray;\n"
                                          "    border-style: outset;\n"
                                          "    border-width: 2px;\n"
                                          "    border-radius: 10px;\n"
                                          "    border-color: black;\n"
                                          "    font: bold 14px;\n"
                                          "    min-width: 10em;\n"
                                          "    padding: 6px;\n"
                                          "}\n"
                                          "QPushButton:pressed {\n"
                                          "    background-color: #32CC99;\n"
                                          "    border-style: inset;\n"
                                          "}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.saveFileButton.setIcon(icon4)
        self.saveFileButton.setIconSize(QSize(24, 24))

        self.verticalLayout_15.addWidget(self.saveFileButton)

        self.gridLayout_2.addWidget(self.saveBtnFrame, 2, 0, 1, 1)

        self.coeffsTableWidget = QTableWidget(self.tableFrame)
        if (self.coeffsTableWidget.rowCount() < 1):
            self.coeffsTableWidget.setRowCount(1)
        self.coeffsTableWidget.setObjectName(u"coeffsTableWidget")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.coeffsTableWidget.sizePolicy().hasHeightForWidth())
        self.coeffsTableWidget.setSizePolicy(sizePolicy7)
        self.coeffsTableWidget.setStyleSheet(u"QTableWidget{\n"
                                             "color: black;\n"
                                             "background-color: white;\n"
                                             "gridline-color:black;\n"
                                             "font: 700 15pt \"Arial\";\n"
                                             "selection-background-color: green;\n"
                                             "border: none;\n"
                                             "}\n"
                                             "QTableWidget::item::selected{\n"
                                             "color:black;\n"
                                             "background-color:#32CC99;\n"
                                             "}\n"
                                             "QHeaderView\n"
                                             "{\n"
                                             "border:none;\n"
                                             "font: 700 15pt \"Arial\";\n"
                                             "background-color: #a5d6a7;\n"
                                             "color:green;\n"
                                             "border: 1px solid;\n"
                                             "}\n"
                                             "QHeaderView::section\n"
                                             "{\n"
                                             "border:none;\n"
                                             "font: 700 16pt \"Arial\";\n"
                                             "background-color: #a5d6a7;\n"
                                             "color:black;\n"
                                             "border: 1px solid;\n"
                                             "}\n"
                                             "QTableWidget QTableCornerButton::section{\n"
                                             "background-color: #d7ffd9;\n"
                                             "border: none;}\n"
                                             "\n"
                                             "QScrollBar:vertical {\n"
                                             "border-color: #424242;\n"
                                             "border-width: 1px;\n"
                                             "border-style: solid;\n"
                                             "background-color: white;\n"
                                             "width: 25px;\n"
                                             "margin: 21px 0 21px 0;}\n"
                                             "QScrollBar::handle:vertical {\n"
                                             "background-color:#a5d6a7 ;\n"
                                             "min-height: 25px;}\n"
                                             "    QScrollBar::add-line:vertical {border: 2px solid black;background-color: #32CC99;\n"
                                             ""
                                             "    height: 25px;subcontrol-position: bottom;subcontrol-origin: margin;}\n"
                                             "    QScrollBar::sub-line:vertical {border: 2px solid black;\n"
                                             "background-color:#32CC99;\n"
                                             "    height: 25px;subcontrol-position: top;subcontrol-origin: margin;}\n"
                                             "")
        self.coeffsTableWidget.setShowGrid(True)
        self.coeffsTableWidget.setGridStyle(Qt.SolidLine)
        self.coeffsTableWidget.setWordWrap(True)
        self.coeffsTableWidget.setRowCount(1)
        self.coeffsTableWidget.setColumnCount(0)
        self.coeffsTableWidget.horizontalHeader().setVisible(True)
        self.coeffsTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.coeffsTableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.coeffsTableWidget.horizontalHeader().setStretchLastSection(False)
        self.coeffsTableWidget.verticalHeader().setVisible(True)
        self.coeffsTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.coeffsTableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.coeffsTableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_2.addWidget(self.coeffsTableWidget, 1, 0, 1, 1)

        self.coeffsTitleLabel = QLabel(self.tableFrame)
        self.coeffsTitleLabel.setObjectName(u"coeffsTitleLabel")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.coeffsTitleLabel.sizePolicy().hasHeightForWidth())
        self.coeffsTitleLabel.setSizePolicy(sizePolicy8)
        self.coeffsTitleLabel.setFont(font1)
        self.coeffsTitleLabel.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.coeffsTitleLabel, 0, 0, 1, 1)

        self.verticalLayout_12.addWidget(self.tableFrame)

        self.mainMenu.addWidget(self.coefficientsPage)

        self.verticalLayout_6.addWidget(self.mainMenu)

        self.verticalLayout_5.addWidget(self.centerMenuSubContainer)

        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainContainer = QWidget(self.centralWidget)
        self.mainContainer.setObjectName(u"mainContainer")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.mainContainer.sizePolicy().hasHeightForWidth())
        self.mainContainer.setSizePolicy(sizePolicy9)
        self.mainContainer.setMinimumSize(QSize(0, 300))
        self.mainContainer.setStyleSheet(u"background-color: #fff;")
        self.verticalLayout_7 = QVBoxLayout(self.mainContainer)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.headerContainer.setStyleSheet(u"*{border:none;}")
        self.horizontalLayout_16 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 9, 9, 9)
        self.buttonFrame = QFrame(self.headerContainer)
        self.buttonFrame.setObjectName(u"buttonFrame")
        self.buttonFrame.setFrameShape(QFrame.StyledPanel)
        self.buttonFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.buttonFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.minimizeButton = QPushButton(self.buttonFrame)
        self.minimizeButton.setObjectName(u"minimizeButton")
        icon5 = QIcon()
        icon5.addFile(u":/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeButton.setIcon(icon5)
        self.minimizeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.minimizeButton)

        self.restoreButton = QPushButton(self.buttonFrame)
        self.restoreButton.setObjectName(u"restoreButton")
        icon6 = QIcon()
        icon6.addFile(u":/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restoreButton.setIcon(icon6)
        self.restoreButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.restoreButton)

        self.closeButton = QPushButton(self.buttonFrame)
        self.closeButton.setObjectName(u"closeButton")
        icon7 = QIcon()
        icon7.addFile(u":/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeButton.setIcon(icon7)
        self.closeButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_6.addWidget(self.closeButton)

        self.horizontalLayout_16.addWidget(self.buttonFrame, 0, Qt.AlignRight)

        self.verticalLayout_7.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.plotTabWidget = QTabWidget(self.mainContainer)
        self.plotTabWidget.setObjectName(u"plotTabWidget")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.plotTabWidget.sizePolicy().hasHeightForWidth())
        self.plotTabWidget.setSizePolicy(sizePolicy10)
        self.plotTabWidget.setMinimumSize(QSize(0, 300))
        self.plotTabWidget.setFont(font)
        self.plotTabWidget.setStyleSheet(u"QTabBar::tab {\n"
                                         "  background: white;\n"
                                         "  color: black;\n"
                                         "  \n"
                                         " }\n"
                                         "\n"
                                         " QTabBar::tab:selected {\n"
                                         "  background: #a5d6a7;\n"
                                         " }")
        self.plotTabWidget.setTabPosition(QTabWidget.North)
        self.plotTabWidget.setTabShape(QTabWidget.Triangular)
        self.plotTabWidget.setTabsClosable(False)
        self.plotTabWidget.setTabBarAutoHide(False)
        self.magnitudeTab = QWidget()
        self.magnitudeTab.setObjectName(u"magnitudeTab")
        self.verticalLayout_13 = QVBoxLayout(self.magnitudeTab)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.MagnitudePlotWidget = PlotWidget(self.magnitudeTab)
        self.MagnitudePlotWidget.setObjectName(u"MagnitudePlotWidget")
        self.MagnitudePlotWidget.setMaximumSize(QSize(16777215, 16777215))

        self.verticalLayout_13.addWidget(self.MagnitudePlotWidget)

        self.plotTabWidget.addTab(self.magnitudeTab, "")
        self.phaseTab = QWidget()
        self.phaseTab.setObjectName(u"phaseTab")
        self.verticalLayout = QVBoxLayout(self.phaseTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.phasePlotWidget = PlotWidget(self.phaseTab)
        self.phasePlotWidget.setObjectName(u"phasePlotWidget")

        self.verticalLayout.addWidget(self.phasePlotWidget)

        self.plotTabWidget.addTab(self.phaseTab, "")
        self.impulseTab = QWidget()
        self.impulseTab.setObjectName(u"impulseTab")
        self.verticalLayout_14 = QVBoxLayout(self.impulseTab)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.ImpulsePlotWidget = PlotWidget(self.impulseTab)
        self.ImpulsePlotWidget.setObjectName(u"ImpulsePlotWidget")
        self.pole_zeroTab = QWidget()
        self.pole_zeroTab.setObjectName(u"pole_zeroTab")
        self.pole_zeroVL = QVBoxLayout(self.pole_zeroTab)
        self.pole_zeroPlotWidget = PlotWidget(self.pole_zeroTab)
        self.pole_zeroVL.addWidget(self.pole_zeroPlotWidget)

        self.plotTabWidget.addTab(self.pole_zeroTab, "")
        self.verticalLayout_14.addWidget(self.ImpulsePlotWidget)

        self.plotTabWidget.addTab(self.impulseTab, "")

        self.verticalLayout_7.addWidget(self.plotTabWidget)

        self.frame = QFrame(self.mainContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_13.addWidget(self.label)

        self.sizeGrip = QWidget(self.frame)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(30, 30))
        self.sizeGrip.setMaximumSize(QSize(30, 30))
        self.sizeGrip.setStyleSheet(u"background: transparent;\n"
                                    "image: url(:/icons/resize2-svgrepo-com.svg);")

        self.horizontalLayout_13.addWidget(self.sizeGrip)

        self.verticalLayout_7.addWidget(self.frame)

        self.horizontalLayout.addWidget(self.mainContainer)

        View.setCentralWidget(self.centralWidget)

        self.retranslateUi(View)

        self.mainMenu.setCurrentIndex(0)
        self.freqParams.setCurrentIndex(0)
        self.methodParams.setCurrentIndex(0)
        self.plotTabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(View)

    # setupUi

    def retranslateUi(self, View):
        View.setWindowTitle(QCoreApplication.translate("View", u"MainWindow", None))
        self.menuButton.setText("")
        self.specificationButton.setText(QCoreApplication.translate("View", u"Filter Specification", None))
        self.coefficientsButton.setText(QCoreApplication.translate("View", u"Coefficients", None))
        self.helpButton.setText(QCoreApplication.translate("View", u"Help", None))
        self.titleLabel.setText(QCoreApplication.translate("View", u"Filter design parameters:", None))
        # if QT_CONFIG(tooltip)
        self.typeComboBox.setToolTip(
            QCoreApplication.translate("View", u"<html><head/><body><p>Choose filter response type.</p></body></html>",
                                       None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.responseComboBox.setToolTip(QCoreApplication.translate("View",
                                                                    u"<html><head/><body><p>Choose filter type. FIR ( Finite Impulse Response) or IIR (Infinite Impulse Response)</p></body></html>",
                                                                    None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.methodComboBox.setToolTip(
            QCoreApplication.translate("View", u"<html><head/><body><p>Choose design method.</p></body></html>", None))
        # endif // QT_CONFIG(tooltip)
        # if QT_CONFIG(tooltip)
        self.designButton.setToolTip(
            QCoreApplication.translate("View", u"<html><head/><body><p>Press to design filter!</p></body></html>",
                                       None))
        # endif // QT_CONFIG(tooltip)
        self.designButton.setText(QCoreApplication.translate("View", u"Design Filter", None))
        self.orderLabel_4.setText(QCoreApplication.translate("View", u"N:", None))
        # if QT_CONFIG(tooltip)
        self.orderLineEdit_4.setToolTip(
            QCoreApplication.translate("View", u"<html><head/><body><p>Filter order.</p></body></html>", None))
        # endif // QT_CONFIG(tooltip)
        self.sampFreqLabel_4.setText(QCoreApplication.translate("View", u"Fs:", None))
        # if QT_CONFIG(tooltip)
        self.sampFreqLineEdit_4.setToolTip(QCoreApplication.translate("View",
                                                                      u"<html><head/><body><p>Sampling frequency</p><p><span style=\" color:#005500;\">Units: Hz</span></p></body></html>",
                                                                      None))
        # endif // QT_CONFIG(tooltip)
        self.fc11Label.setText(QCoreApplication.translate("View", u"Fc:", None))
        # if QT_CONFIG(tooltip)
        self.Fc.setToolTip(QCoreApplication.translate("View",
                                                      u"<html><head/><body><p>Cutoff frequency</p><p><span style=\" color:#005500;\">Units: Hz</span></p></body></html>",
                                                      None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_8.setText(QCoreApplication.translate("View", u"Fstop:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_12.setToolTip(QCoreApplication.translate("View",
                                                                  u"<html><head/><body><p>Cutoff frequency for band.</p><p><span style=\" color:#005500;\">Units: Hz</span></p></body></html>",
                                                                  None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_12.setText(QCoreApplication.translate("View", u"Fpass", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_13.setToolTip(QCoreApplication.translate("View",
                                                                  u"<html><head/><body><p>Cutoff frequency for band.</p><p><span style=\" color:#005500;\">Units: Hz</span></p></body></html>",
                                                                  None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_6.setText(QCoreApplication.translate("View", u"Fstop1:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_7.setToolTip(QCoreApplication.translate("View",
                                                                 u"<html><head/><body><p>Cutoff frequency for band.</p><p><span style=\" color:#005500;\">Units: Hz</span></p></body></html>",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_2.setText(QCoreApplication.translate("View", u"Fpass1:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_6.setToolTip(QCoreApplication.translate("View",
                                                                 u"<html><head/><body><p>Cutoff frequency for band.</p><p><span style=\" color:#005500;\">Units: Hz</span></p></body></html>",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_17.setText(QCoreApplication.translate("View", u"Fstop2:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_2.setToolTip(QCoreApplication.translate("View",
                                                                 u"<html><head/><body><p>Cutoff frequency for band.</p><p><span style=\" color:#005500;\">Units: Hz</span></p></body></html>",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label.setText(QCoreApplication.translate("View", u"Fpass2:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit.setToolTip(QCoreApplication.translate("View",
                                                               u"<html><head/><body><p>Cutoff frequency for band.</p><p><span style=\" color:#005500;\">Units: Hz</span></p></body></html>",
                                                               None))
        # endif // QT_CONFIG(tooltip)
        self.fc1Label.setText(QCoreApplication.translate("View", u"Fc1:", None))
        # if QT_CONFIG(tooltip)
        self.fc1lineEdit.setToolTip(QCoreApplication.translate("View",
                                                               u"<html><head/><body><p>Cutoff frequency for band.</p><p><span style=\" color:#005500;\">Units: Hz</span></p></body></html>",
                                                               None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_7.setText(QCoreApplication.translate("View", u"Fc2:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_8.setToolTip(QCoreApplication.translate("View",
                                                                 u"<html><head/><body><p>Cutoff frequency for band.</p><p><span style=\" color:#005500;\">Units: Hz</span></p></body></html>",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.windowLabel.setText(QCoreApplication.translate("View", u"Window:", None))
        # self.windowComboBox.setItemText(0, QCoreApplication.translate("View", u"Hamming", None))

        self.fc2Label_11.setText(QCoreApplication.translate("View", u"Grid density:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_11.setToolTip(QCoreApplication.translate("View",
                                                                  u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                  "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                                  "p, li { white-space: pre-wrap; }\n"
                                                                  "hr { height: 1px; border-width: 0; }\n"
                                                                  "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                                  "li.checked::marker { content: \"\\2612\"; }\n"
                                                                  "</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
                                                                  "<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Grid density. The dense grid is of size (numtaps + 1) * grid_density.</p></body></html>",
                                                                  None))
        # endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("View", u"Weight specification:", None))
        self.fc2Label_3.setText(QCoreApplication.translate("View", u"Wpb1:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_3.setToolTip(QCoreApplication.translate("View",
                                                                 u"<html><head/><body><p>A relative weighting to pass band.</p><p><br/></p></body></html>",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_4.setText(QCoreApplication.translate("View", u"Wsb1:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_4.setToolTip(QCoreApplication.translate("View",
                                                                 u"<html><head/><body><p>A relative weighting to stop band.</p></body></html>",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_5.setText(QCoreApplication.translate("View", u"Wpb2:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_5.setToolTip(QCoreApplication.translate("View",
                                                                 u"<html><head/><body><p>A relative weighting to 2nd pass band.</p><p><br/></p></body></html>",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_15.setText(QCoreApplication.translate("View", u"Wsb2:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_16.setToolTip(QCoreApplication.translate("View",
                                                                  u"<html><head/><body><p>A relative weighting to 2nd stop band.</p></body></html>",
                                                                  None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_13.setText(QCoreApplication.translate("View", u"Rp:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_14.setToolTip(QCoreApplication.translate("View",
                                                                  u"The maximum ripple allowed below unity gain in the passband. Specified in decibels, as a positive number.",
                                                                  None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_14.setText(QCoreApplication.translate("View", u"Rs:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_15.setToolTip(QCoreApplication.translate("View",
                                                                  u"The minimum attenuation required in the stop band. Specified in decibels, as a positive number.",
                                                                  None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_9.setText(QCoreApplication.translate("View", u"Rp:", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_9.setToolTip(QCoreApplication.translate("View",
                                                                 u"The maximum ripple allowed below unity gain in the passband. Specified in decibels, as a positive number.",
                                                                 None))
        # endif // QT_CONFIG(tooltip)
        self.fc2Label_10.setText(QCoreApplication.translate("View", u"Rs", None))
        # if QT_CONFIG(tooltip)
        self.fc2lineEdit_10.setToolTip(QCoreApplication.translate("View",
                                                                  u"The minimum attenuation required in the stop band. Specified in decibels, as a positive number.",
                                                                  None))
        # endif // QT_CONFIG(tooltip)
        self.saveFileButton.setText(QCoreApplication.translate("View", u"Save to file", None))
        self.coeffsTitleLabel.setText(QCoreApplication.translate("View", u"Filter Coefficients:", None))
        self.minimizeButton.setText("")
        self.restoreButton.setText("")
        self.closeButton.setText("")
        self.plotTabWidget.setTabText(self.plotTabWidget.indexOf(self.magnitudeTab),
                                      QCoreApplication.translate("View", u"Frequency Response", None))
        self.plotTabWidget.setTabText(self.plotTabWidget.indexOf(self.phaseTab),
                                      QCoreApplication.translate("View", u"Phase Response", None))
        self.plotTabWidget.setTabText(self.plotTabWidget.indexOf(self.impulseTab),
                                      QCoreApplication.translate("View", u"Impulse Response", None))
        self.plotTabWidget.setTabText(self.plotTabWidget.indexOf(self.pole_zeroTab),
                                      QCoreApplication.translate("View", u"Poles and zeros", None))
        self.label.setText(QCoreApplication.translate("View", u"Digital Filter Designer v.1.0", None))
        # if QT_CONFIG(tooltip)
        self.sizeGrip.setToolTip(
            QCoreApplication.translate("View", u"<html><head/><body><p>Resize in windowed mode</p></body></html>",
                                       None))
# endif // QT_CONFIG(tooltip)
# retranslateUi
