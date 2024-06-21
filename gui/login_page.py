# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_login_page(object):
    def setupUi(self, login_page):
        if not login_page.objectName():
            login_page.setObjectName(u"login_page")
        login_page.resize(400, 300)
        login_page.setMinimumSize(QSize(400, 300))
        login_page.setMaximumSize(QSize(400, 300))
        login_page.setSizeGripEnabled(False)
        login_page.setModal(False)
        self.gridLayoutWidget = QWidget(login_page)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 381, 281))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setBold(True)
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.pass_txtbox = QLineEdit(self.gridLayoutWidget)
        self.pass_txtbox.setObjectName(u"pass_txtbox")
        self.pass_txtbox.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

        self.gridLayout.addWidget(self.pass_txtbox, 2, 1, 1, 1)

        self.login_btn = QPushButton(self.gridLayoutWidget)
        self.login_btn.setObjectName(u"login_btn")

        self.gridLayout.addWidget(self.login_btn, 3, 1, 1, 1)

        self.sign_in_btn = QPushButton(self.gridLayoutWidget)
        self.sign_in_btn.setObjectName(u"sign_in_btn")

        self.gridLayout.addWidget(self.sign_in_btn, 3, 0, 1, 1)

        self.cancel_btn = QPushButton(self.gridLayoutWidget)
        self.cancel_btn.setObjectName(u"cancel_btn")

        self.gridLayout.addWidget(self.cancel_btn, 4, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)

        self.login_txtbox = QLineEdit(self.gridLayoutWidget)
        self.login_txtbox.setObjectName(u"login_txtbox")

        self.gridLayout.addWidget(self.login_txtbox, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Microsoft JhengHei UI"])
        font1.setPointSize(16)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.status_lbl = QLabel(self.gridLayoutWidget)
        self.status_lbl.setObjectName(u"status_lbl")
        self.status_lbl.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.status_lbl.sizePolicy().hasHeightForWidth())
        self.status_lbl.setSizePolicy(sizePolicy1)
        self.status_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.status_lbl, 5, 0, 1, 2)


        self.retranslateUi(login_page)
        self.cancel_btn.clicked.connect(login_page.close)

        QMetaObject.connectSlotsByName(login_page)
    # setupUi

    def retranslateUi(self, login_page):
        login_page.setWindowTitle(QCoreApplication.translate("login_page", u"Dialog", None))
        self.label_2.setText(QCoreApplication.translate("login_page", u"Login:", None))
        self.login_btn.setText(QCoreApplication.translate("login_page", u"Log in", None))
        self.sign_in_btn.setText(QCoreApplication.translate("login_page", u"Sign in", None))
        self.cancel_btn.setText(QCoreApplication.translate("login_page", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("login_page", u"Password:", None))
        self.label_3.setText(QCoreApplication.translate("login_page", u"Welcome to Farmer Markets DB!", None))
        self.status_lbl.setText("")
    # retranslateUi

