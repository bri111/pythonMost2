# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSlider,
    QTextEdit, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1300, 800)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setAutoFillBackground(False)
        self.pushButton = QPushButton(Widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1180, 10, 100, 32))
        self.frame_2 = QFrame(Widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 1161, 51))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 41, 31))
        font = QFont()
        font.setPointSize(11)
        font.setBold(False)
        self.label.setFont(font)
        self.textEdit = QTextEdit(self.frame_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(50, 10, 51, 31))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy1)
        self.textEdit_3 = QTextEdit(self.frame_2)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setGeometry(QRect(270, 10, 51, 31))
        sizePolicy1.setHeightForWidth(self.textEdit_3.sizePolicy().hasHeightForWidth())
        self.textEdit_3.setSizePolicy(sizePolicy1)
        self.textEdit_2 = QTextEdit(self.frame_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(162, 10, 51, 31))
        sizePolicy1.setHeightForWidth(self.textEdit_2.sizePolicy().hasHeightForWidth())
        self.textEdit_2.setSizePolicy(sizePolicy1)
        self.comboBox = QComboBox(self.frame_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(590, 10, 103, 32))
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 10, 31, 31))
        self.label_4.setFont(font)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(230, 10, 31, 31))
        self.label_3.setFont(font)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(120, 10, 41, 31))
        self.label_2.setFont(font)
        self.textEdit_5 = QTextEdit(self.frame_2)
        self.textEdit_5.setObjectName(u"textEdit_5")
        self.textEdit_5.setGeometry(QRect(480, 10, 51, 31))
        sizePolicy1.setHeightForWidth(self.textEdit_5.sizePolicy().hasHeightForWidth())
        self.textEdit_5.setSizePolicy(sizePolicy1)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(440, 10, 31, 31))
        self.label_5.setFont(font)
        self.textEdit_4 = QTextEdit(self.frame_2)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setGeometry(QRect(370, 10, 51, 31))
        sizePolicy1.setHeightForWidth(self.textEdit_4.sizePolicy().hasHeightForWidth())
        self.textEdit_4.setSizePolicy(sizePolicy1)
        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(540, 10, 41, 31))
        self.label_6.setFont(font)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(740, 10, 371, 31))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.logReviewButton = QPushButton(self.frame)
        self.logReviewButton.setObjectName(u"logReviewButton")
        self.logReviewButton.setGeometry(QRect(0, 0, 81, 32))
        self.logReviewButton.setAutoFillBackground(False)
        self.logEntryButton = QPushButton(self.frame)
        self.logEntryButton.setObjectName(u"logEntryButton")
        self.logEntryButton.setGeometry(QRect(85, 0, 71, 32))
        self.logEntryButton.setAutoFillBackground(False)
        self.logOutButton = QPushButton(self.frame)
        self.logOutButton.setObjectName(u"logOutButton")
        self.logOutButton.setGeometry(QRect(160, 0, 51, 32))
        self.logOutButton.setAutoFillBackground(False)
        self.pushButton_5 = QPushButton(self.frame)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(215, 0, 61, 32))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_6 = QPushButton(self.frame)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(280, 0, 91, 32))
        self.pushButton_6.setAutoFillBackground(False)
        self.horizontalSlider = QSlider(Widget)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setGeometry(QRect(450, 60, 831, 25))
        self.horizontalSlider.setOrientation(Qt.Horizontal)
        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(10, 60, 421, 731))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 419, 729))
        self.scrollArea_2 = QScrollArea(self.scrollAreaWidgetContents)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(390, 10, 20, 711))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 18, 709))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.label_7 = QLabel(self.scrollAreaWidgetContents)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(160, 230, 51, 21))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_3 = QFrame(Widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(440, 90, 421, 701))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.label_8 = QLabel(self.frame_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(170, 50, 51, 21))
        self.frame_4 = QFrame(Widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(870, 90, 421, 701))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"PushButton", None))
        self.label.setText(QCoreApplication.translate("Widget", u"UTC", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Widget", u"Option 1", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Widget", u"Option 2", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Widget", u"Option 3", None))

        self.label_4.setText(QCoreApplication.translate("Widget", u"SLT", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"MET", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"MOC", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"MJD", None))
        self.label_6.setText(QCoreApplication.translate("Widget", u"Mode", None))
        self.logReviewButton.setText(QCoreApplication.translate("Widget", u"Log Review", None))
        self.logEntryButton.setText(QCoreApplication.translate("Widget", u"Log Entry", None))
        self.logOutButton.setText(QCoreApplication.translate("Widget", u"Log in", None))
        self.pushButton_5.setText(QCoreApplication.translate("Widget", u"Log Out", None))
        self.pushButton_6.setText(QCoreApplication.translate("Widget", u"B/G Monitor", None))
        self.label_7.setText(QCoreApplication.translate("Widget", u"MEDB", None))
        self.label_8.setText(QCoreApplication.translate("Widget", u"Earth", None))
    # retranslateUi

