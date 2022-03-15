# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'falcon.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 780)
        MainWindow.setMinimumSize(QSize(450, 780))
        MainWindow.setMaximumSize(QSize(450, 780))
        MainWindow.setStyleSheet(u"background: rgb(9, 54, 55)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"linear-gradient (to right, #110E13, #2B1E2B)\n"
"\n"
"\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.NAme = QTextEdit(self.centralwidget)
        self.NAme.setObjectName(u"NAme")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NAme.sizePolicy().hasHeightForWidth())
        self.NAme.setSizePolicy(sizePolicy)
        self.NAme.setMinimumSize(QSize(428, 100))
        self.NAme.setMaximumSize(QSize(428, 100))
        self.NAme.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.NAme.setMouseTracking(True)
        self.NAme.setTabletTracking(True)
        self.NAme.setStyleSheet(u"QTextEdit{\n"
"	background:rgb(68, 160, 141);\n"
"	border: 2px solid rgb(37,39,48);\n"
"	border-radius: 15px\n"
"\n"
"}\n"
"")
        self.NAme.setReadOnly(True)

        self.verticalLayout.addWidget(self.NAme)

        self.OTVET = QTextEdit(self.centralwidget)
        self.OTVET.setObjectName(u"OTVET")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(5)
        sizePolicy1.setVerticalStretch(100)
        sizePolicy1.setHeightForWidth(self.OTVET.sizePolicy().hasHeightForWidth())
        self.OTVET.setSizePolicy(sizePolicy1)
        self.OTVET.setMinimumSize(QSize(428, 200))
        self.OTVET.setMaximumSize(QSize(428, 200))
        self.OTVET.viewport().setProperty("cursor", QCursor(Qt.ArrowCursor))
        self.OTVET.setMouseTracking(True)
        self.OTVET.setTabletTracking(True)
        self.OTVET.setStyleSheet(u"QTextEdit{\n"
"	background:rgb(68, 160, 141);\n"
"	border: 2px solid rgb(37,39,48);\n"
"	border-radius: 15px\n"
"\n"
"}\n"
"")
        self.OTVET.setReadOnly(True)

        self.verticalLayout.addWidget(self.OTVET)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.YPAVNENIE = QLineEdit(self.centralwidget)
        self.YPAVNENIE.setObjectName(u"YPAVNENIE")
        self.YPAVNENIE.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.YPAVNENIE.sizePolicy().hasHeightForWidth())
        self.YPAVNENIE.setSizePolicy(sizePolicy2)
        self.YPAVNENIE.setMaximumSize(QSize(360, 50))
        palette = QPalette()
        brush = QBrush(QColor(68, 160, 141, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        brush2 = QBrush(QColor(120, 120, 120, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.YPAVNENIE.setPalette(palette)
        font = QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(False)
        self.YPAVNENIE.setFont(font)
        self.YPAVNENIE.setMouseTracking(False)
        self.YPAVNENIE.setContextMenuPolicy(Qt.PreventContextMenu)
        self.YPAVNENIE.setStyleSheet(u"QLineEdit{\n"
"	background:rgb(68, 160, 141);\n"
"	border: 2px solid rgb(37,39,48);\n"
"	border-radius: 15px\n"
"\n"
"}")
        self.YPAVNENIE.setText(u"0")
        self.YPAVNENIE.setMaxLength(50)
        self.YPAVNENIE.setFrame(True)
        self.YPAVNENIE.setAlignment(Qt.AlignCenter)
        self.YPAVNENIE.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.YPAVNENIE)

        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.spinBox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_CE = QPushButton(self.centralwidget)
        self.btn_CE.setObjectName(u"btn_CE")
        sizePolicy2.setHeightForWidth(self.btn_CE.sizePolicy().hasHeightForWidth())
        self.btn_CE.setSizePolicy(sizePolicy2)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Button, brush)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_CE.setPalette(palette1)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.btn_CE.setFont(font1)
        self.btn_CE.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_CE.setMouseTracking(True)
        self.btn_CE.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_CE, 0, 1, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy3)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Button, brush)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_2.setPalette(palette2)
        self.btn_2.setFont(font1)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_2.setMouseTracking(True)
        self.btn_2.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_2, 5, 1, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy3.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy3)
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.Button, brush)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_7.setPalette(palette3)
        self.btn_7.setFont(font1)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_7.setMouseTracking(True)
        self.btn_7.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_7, 2, 0, 1, 1)

        self.btn_skobka1 = QPushButton(self.centralwidget)
        self.btn_skobka1.setObjectName(u"btn_skobka1")
        sizePolicy3.setHeightForWidth(self.btn_skobka1.sizePolicy().hasHeightForWidth())
        self.btn_skobka1.setSizePolicy(sizePolicy3)
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_skobka1.setPalette(palette4)
        self.btn_skobka1.setFont(font1)
        self.btn_skobka1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_skobka1.setMouseTracking(True)
        self.btn_skobka1.setFocusPolicy(Qt.StrongFocus)
        self.btn_skobka1.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"	border-bottom-left-radius: 15px\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_skobka1, 6, 0, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy3.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy3)
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.Button, brush)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_1.setPalette(palette5)
        self.btn_1.setFont(font1)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_1.setMouseTracking(True)
        self.btn_1.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_1, 5, 0, 1, 1)

        self.btn_otv = QPushButton(self.centralwidget)
        self.btn_otv.setObjectName(u"btn_otv")
        sizePolicy3.setHeightForWidth(self.btn_otv.sizePolicy().hasHeightForWidth())
        self.btn_otv.setSizePolicy(sizePolicy3)
        palette6 = QPalette()
        brush3 = QBrush(QColor(0, 0, 0, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_otv.setPalette(palette6)
        font2 = QFont()
        font2.setFamilies([u"MS Shell Dlg 2"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.btn_otv.setFont(font2)
        self.btn_otv.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_otv.setMouseTracking(True)
        self.btn_otv.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"	border-bottom-right-radius: 15px\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_otv, 6, 3, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy3.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy3)
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.Button, brush)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Active, QPalette.Base, brush)
        palette7.setBrush(QPalette.Active, QPalette.Window, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette7.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette7.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_9.setPalette(palette7)
        self.btn_9.setFont(font1)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_9.setMouseTracking(True)
        self.btn_9.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_9, 2, 2, 1, 1)

        self.btn_plus = QPushButton(self.centralwidget)
        self.btn_plus.setObjectName(u"btn_plus")
        sizePolicy3.setHeightForWidth(self.btn_plus.sizePolicy().hasHeightForWidth())
        self.btn_plus.setSizePolicy(sizePolicy3)
        palette8 = QPalette()
        palette8.setBrush(QPalette.Active, QPalette.Button, brush)
        palette8.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette8.setBrush(QPalette.Active, QPalette.Base, brush)
        palette8.setBrush(QPalette.Active, QPalette.Window, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette8.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette8.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette8.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette8.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_plus.setPalette(palette8)
        self.btn_plus.setFont(font1)
        self.btn_plus.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_plus.setMouseTracking(True)
        self.btn_plus.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_plus, 5, 3, 1, 1)

        self.btn_skobka2 = QPushButton(self.centralwidget)
        self.btn_skobka2.setObjectName(u"btn_skobka2")
        sizePolicy3.setHeightForWidth(self.btn_skobka2.sizePolicy().hasHeightForWidth())
        self.btn_skobka2.setSizePolicy(sizePolicy3)
        palette9 = QPalette()
        palette9.setBrush(QPalette.Active, QPalette.Button, brush)
        palette9.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Active, QPalette.Base, brush)
        palette9.setBrush(QPalette.Active, QPalette.Window, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette9.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette9.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette9.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette9.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_skobka2.setPalette(palette9)
        self.btn_skobka2.setFont(font1)
        self.btn_skobka2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_skobka2.setMouseTracking(True)
        self.btn_skobka2.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"}")

        self.gridLayout.addWidget(self.btn_skobka2, 6, 2, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy3.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy3)
        palette10 = QPalette()
        palette10.setBrush(QPalette.Active, QPalette.Button, brush)
        palette10.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette10.setBrush(QPalette.Active, QPalette.Base, brush)
        palette10.setBrush(QPalette.Active, QPalette.Window, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette10.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette10.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette10.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette10.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_0.setPalette(palette10)
        self.btn_0.setFont(font1)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_0.setMouseTracking(True)
        self.btn_0.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_0, 6, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy3.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy3)
        palette11 = QPalette()
        palette11.setBrush(QPalette.Active, QPalette.Button, brush)
        palette11.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette11.setBrush(QPalette.Active, QPalette.Base, brush)
        palette11.setBrush(QPalette.Active, QPalette.Window, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette11.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette11.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette11.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette11.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_3.setPalette(palette11)
        self.btn_3.setFont(font1)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_3.setMouseTracking(True)
        self.btn_3.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_3, 5, 2, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy3.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy3)
        palette12 = QPalette()
        palette12.setBrush(QPalette.Active, QPalette.Button, brush)
        palette12.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Active, QPalette.Base, brush)
        palette12.setBrush(QPalette.Active, QPalette.Window, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette12.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette12.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette12.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette12.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_5.setPalette(palette12)
        self.btn_5.setFont(font1)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_5.setMouseTracking(True)
        self.btn_5.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_5, 3, 1, 1, 1)

        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy3.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy3)
        palette13 = QPalette()
        palette13.setBrush(QPalette.Active, QPalette.Button, brush)
        palette13.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Active, QPalette.Base, brush)
        palette13.setBrush(QPalette.Active, QPalette.Window, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette13.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette13.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette13.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette13.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_4.setPalette(palette13)
        self.btn_4.setFont(font1)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_4.setMouseTracking(True)
        self.btn_4.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_4, 3, 0, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy3.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy3)
        palette14 = QPalette()
        palette14.setBrush(QPalette.Active, QPalette.Button, brush)
        palette14.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette14.setBrush(QPalette.Active, QPalette.Base, brush)
        palette14.setBrush(QPalette.Active, QPalette.Window, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette14.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette14.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette14.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette14.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_8.setPalette(palette14)
        self.btn_8.setFont(font1)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_8.setMouseTracking(True)
        self.btn_8.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_8, 2, 1, 1, 1)

        self.btn_C = QPushButton(self.centralwidget)
        self.btn_C.setObjectName(u"btn_C")
        self.btn_C.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.btn_C.sizePolicy().hasHeightForWidth())
        self.btn_C.setSizePolicy(sizePolicy2)
        palette15 = QPalette()
        palette15.setBrush(QPalette.Active, QPalette.Button, brush)
        palette15.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette15.setBrush(QPalette.Active, QPalette.Base, brush)
        palette15.setBrush(QPalette.Active, QPalette.Window, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette15.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette15.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette15.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette15.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_C.setPalette(palette15)
        self.btn_C.setFont(font1)
        self.btn_C.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_C.setMouseTracking(True)
        self.btn_C.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"	border-top-left-radius: 15px\n"
"\n"
"}\n"
"	")

        self.gridLayout.addWidget(self.btn_C, 0, 0, 1, 1)

        self.btn_delenie = QPushButton(self.centralwidget)
        self.btn_delenie.setObjectName(u"btn_delenie")
        sizePolicy2.setHeightForWidth(self.btn_delenie.sizePolicy().hasHeightForWidth())
        self.btn_delenie.setSizePolicy(sizePolicy2)
        palette16 = QPalette()
        palette16.setBrush(QPalette.Active, QPalette.Button, brush)
        palette16.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette16.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette16.setBrush(QPalette.Active, QPalette.Base, brush)
        palette16.setBrush(QPalette.Active, QPalette.Window, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette16.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette16.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette16.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette16.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_delenie.setPalette(palette16)
        self.btn_delenie.setFont(font1)
        self.btn_delenie.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_delenie.setMouseTracking(True)
        self.btn_delenie.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"	border-top-right-radius: 15px\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_delenie, 0, 3, 1, 1)

        self.btn_stepen = QPushButton(self.centralwidget)
        self.btn_stepen.setObjectName(u"btn_stepen")
        sizePolicy2.setHeightForWidth(self.btn_stepen.sizePolicy().hasHeightForWidth())
        self.btn_stepen.setSizePolicy(sizePolicy2)
        palette17 = QPalette()
        palette17.setBrush(QPalette.Active, QPalette.Button, brush)
        palette17.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette17.setBrush(QPalette.Active, QPalette.Base, brush)
        palette17.setBrush(QPalette.Active, QPalette.Window, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette17.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette17.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette17.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette17.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_stepen.setPalette(palette17)
        self.btn_stepen.setFont(font1)
        self.btn_stepen.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_stepen.setMouseTracking(True)
        self.btn_stepen.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_stepen, 0, 2, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy3.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy3)
        palette18 = QPalette()
        palette18.setBrush(QPalette.Active, QPalette.Button, brush)
        palette18.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette18.setBrush(QPalette.Active, QPalette.Base, brush)
        palette18.setBrush(QPalette.Active, QPalette.Window, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette18.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette18.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette18.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette18.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_6.setPalette(palette18)
        self.btn_6.setFont(font1)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_6.setMouseTracking(True)
        self.btn_6.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_6, 3, 2, 1, 1)

        self.btn_minus = QPushButton(self.centralwidget)
        self.btn_minus.setObjectName(u"btn_minus")
        sizePolicy3.setHeightForWidth(self.btn_minus.sizePolicy().hasHeightForWidth())
        self.btn_minus.setSizePolicy(sizePolicy3)
        palette19 = QPalette()
        palette19.setBrush(QPalette.Active, QPalette.Button, brush)
        palette19.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette19.setBrush(QPalette.Active, QPalette.Base, brush)
        palette19.setBrush(QPalette.Active, QPalette.Window, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette19.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette19.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette19.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette19.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_minus.setPalette(palette19)
        self.btn_minus.setFont(font1)
        self.btn_minus.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_minus.setMouseTracking(True)
        self.btn_minus.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_minus, 3, 3, 1, 1)

        self.btn_x = QPushButton(self.centralwidget)
        self.btn_x.setObjectName(u"btn_x")
        sizePolicy3.setHeightForWidth(self.btn_x.sizePolicy().hasHeightForWidth())
        self.btn_x.setSizePolicy(sizePolicy3)
        palette20 = QPalette()
        palette20.setBrush(QPalette.Active, QPalette.Button, brush)
        palette20.setBrush(QPalette.Active, QPalette.ButtonText, brush1)
        palette20.setBrush(QPalette.Active, QPalette.Base, brush)
        palette20.setBrush(QPalette.Active, QPalette.Window, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.ButtonText, brush1)
        palette20.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette20.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette20.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette20.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.btn_x.setPalette(palette20)
        self.btn_x.setFont(font1)
        self.btn_x.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_x.setMouseTracking(True)
        self.btn_x.setStyleSheet(u"QPushButton{\n"
"	background: #44A08D;\n"
"	border: 2px solid rgb(37,39,48);\n"
"\n"
"}")

        self.gridLayout.addWidget(self.btn_x, 2, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.NAme.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">\u0420\u0435\u0448\u0435\u043d\u0438\u0435 14 \u0437\u0430\u0434\u0430\u0447\u0438</span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">\u0415\u0413\u042d \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0442\u0438\u043a\u0430</span></p></body></html>", None))
        self.OTVET.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btn_CE.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
#if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
#if QT_CONFIG(shortcut)
        self.btn_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_skobka1.setText(QCoreApplication.translate("MainWindow", u"(", None))
#if QT_CONFIG(shortcut)
        self.btn_skobka1.setShortcut(QCoreApplication.translate("MainWindow", u"(", None))
#endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
#if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_otv.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0432\u0435\u0442", None))
#if QT_CONFIG(shortcut)
        self.btn_otv.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
#if QT_CONFIG(shortcut)
        self.btn_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
#if QT_CONFIG(shortcut)
        self.btn_plus.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
#endif // QT_CONFIG(shortcut)
        self.btn_skobka2.setText(QCoreApplication.translate("MainWindow", u")", None))
#if QT_CONFIG(shortcut)
        self.btn_skobka2.setShortcut(QCoreApplication.translate("MainWindow", u")", None))
#endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
#if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
#endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
#if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
#if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
#if QT_CONFIG(shortcut)
        self.btn_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
#endif // QT_CONFIG(shortcut)
        self.btn_C.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_delenie.setText(QCoreApplication.translate("MainWindow", u"/", None))
#if QT_CONFIG(shortcut)
        self.btn_delenie.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
#endif // QT_CONFIG(shortcut)
        self.btn_stepen.setText(QCoreApplication.translate("MainWindow", u"X^y", None))
#if QT_CONFIG(shortcut)
        self.btn_stepen.setShortcut(QCoreApplication.translate("MainWindow", u"^", None))
#endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
#if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
#if QT_CONFIG(shortcut)
        self.btn_minus.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
#endif // QT_CONFIG(shortcut)
        self.btn_x.setText(QCoreApplication.translate("MainWindow", u"x", None))
#if QT_CONFIG(shortcut)
        self.btn_x.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

