# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
    QHeaderView, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QSlider, QStatusBar, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1263, 607)
        MainWindow.setMinimumSize(QSize(1263, 0))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.userLabel = QLabel(self.centralwidget)
        self.userLabel.setObjectName(u"userLabel")
        self.userLabel.setMinimumSize(QSize(187, 0))
        self.userLabel.setMaximumSize(QSize(187, 16777215))

        self.gridLayout.addWidget(self.userLabel, 0, 0, 1, 1)

        self.city_comboBox = QComboBox(self.centralwidget)
        self.city_comboBox.setObjectName(u"city_comboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.city_comboBox.sizePolicy().hasHeightForWidth())
        self.city_comboBox.setSizePolicy(sizePolicy)
        self.city_comboBox.setMinimumSize(QSize(187, 22))
        self.city_comboBox.setMaximumSize(QSize(187, 22))

        self.gridLayout.addWidget(self.city_comboBox, 5, 0, 1, 1)

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout.addWidget(self.label_12, 20, 2, 1, 1)

        self.bestRankBtn = QPushButton(self.centralwidget)
        self.bestRankBtn.setObjectName(u"bestRankBtn")
        self.bestRankBtn.setEnabled(False)

        self.gridLayout.addWidget(self.bestRankBtn, 0, 2, 1, 1)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 9, 0, 1, 1)

        self.radius = QLabel(self.centralwidget)
        self.radius.setObjectName(u"radius")
        self.radius.setEnabled(False)

        self.gridLayout.addWidget(self.radius, 17, 0, 1, 1)

        self.searchNearestBtn = QPushButton(self.centralwidget)
        self.searchNearestBtn.setObjectName(u"searchNearestBtn")
        self.searchNearestBtn.setEnabled(False)

        self.gridLayout.addWidget(self.searchNearestBtn, 19, 0, 1, 1)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.line_2.sizePolicy().hasHeightForWidth())
        self.line_2.setSizePolicy(sizePolicy1)
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 0, 1, 21, 1)

        self.zip_input = QLineEdit(self.centralwidget)
        self.zip_input.setObjectName(u"zip_input")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.zip_input.sizePolicy().hasHeightForWidth())
        self.zip_input.setSizePolicy(sizePolicy2)

        self.gridLayout.addWidget(self.zip_input, 8, 0, 1, 1)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 16, 0, 1, 1)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.table = QTableView(self.centralwidget)
        self.table.setObjectName(u"table")

        self.gridLayout.addWidget(self.table, 1, 2, 19, 5)

        self.tableTotalLabel = QLabel(self.centralwidget)
        self.tableTotalLabel.setObjectName(u"tableTotalLabel")

        self.gridLayout.addWidget(self.tableTotalLabel, 20, 6, 1, 1)

        self.details_market_btn = QPushButton(self.centralwidget)
        self.details_market_btn.setObjectName(u"details_market_btn")

        self.gridLayout.addWidget(self.details_market_btn, 14, 0, 1, 1)

        self.selecte_market_bar = QLabel(self.centralwidget)
        self.selecte_market_bar.setObjectName(u"selecte_market_bar")
        self.selecte_market_bar.setMinimumSize(QSize(187, 0))
        self.selecte_market_bar.setMaximumSize(QSize(187, 16777215))

        self.gridLayout.addWidget(self.selecte_market_bar, 11, 0, 3, 1)

        self.radiusSlider = QSlider(self.centralwidget)
        self.radiusSlider.setObjectName(u"radiusSlider")
        self.radiusSlider.setEnabled(False)
        sizePolicy2.setHeightForWidth(self.radiusSlider.sizePolicy().hasHeightForWidth())
        self.radiusSlider.setSizePolicy(sizePolicy2)
        self.radiusSlider.setTracking(True)
        self.radiusSlider.setOrientation(Qt.Orientation.Horizontal)
        self.radiusSlider.setTickPosition(QSlider.TickPosition.TicksBelow)

        self.gridLayout.addWidget(self.radiusSlider, 18, 0, 1, 1)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.state_comboBox = QComboBox(self.centralwidget)
        self.state_comboBox.setObjectName(u"state_comboBox")
        self.state_comboBox.setLocale(QLocale(QLocale.English, QLocale.UnitedStates))

        self.gridLayout.addWidget(self.state_comboBox, 2, 0, 1, 1)

        self.worstRankBtn = QPushButton(self.centralwidget)
        self.worstRankBtn.setObjectName(u"worstRankBtn")
        self.worstRankBtn.setEnabled(False)

        self.gridLayout.addWidget(self.worstRankBtn, 0, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1263, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.userLabel.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u0440\u044b\u043d\u043a\u043e\u0432: ", None))
        self.bestRankBtn.setText(QCoreApplication.translate("MainWindow", u"Sort: Best rank first", None))
        self.radius.setText(QCoreApplication.translate("MainWindow", u"Radius, miles:", None))
        self.searchNearestBtn.setText(QCoreApplication.translate("MainWindow", u"View nearest markets", None))
        self.label_7.setText("")
        self.label_5.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Selected:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"State:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"ZIP:", None))
        self.tableTotalLabel.setText("")
        self.details_market_btn.setText(QCoreApplication.translate("MainWindow", u"View details", None))
        self.selecte_market_bar.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"City:", None))
        self.worstRankBtn.setText(QCoreApplication.translate("MainWindow", u"Sort: Worst rank first", None))
    # retranslateUi

