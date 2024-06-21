# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'details_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(848, 630)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.deleteReviewBtn = QPushButton(Form)
        self.deleteReviewBtn.setObjectName(u"deleteReviewBtn")
        self.deleteReviewBtn.setEnabled(False)

        self.gridLayout.addWidget(self.deleteReviewBtn, 7, 1, 1, 1)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 1, 0, 1, 7)

        self.reviewsView = QTableView(Form)
        self.reviewsView.setObjectName(u"reviewsView")

        self.gridLayout.addWidget(self.reviewsView, 4, 0, 1, 7)

        self.editReviewBtn = QPushButton(Form)
        self.editReviewBtn.setObjectName(u"editReviewBtn")
        self.editReviewBtn.setEnabled(False)

        self.gridLayout.addWidget(self.editReviewBtn, 7, 2, 1, 1)

        self.marketLabel = QLabel(Form)
        self.marketLabel.setObjectName(u"marketLabel")

        self.gridLayout.addWidget(self.marketLabel, 3, 0, 1, 3)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 5, 0, 1, 1)

        self.rankLabel = QLabel(Form)
        self.rankLabel.setObjectName(u"rankLabel")

        self.gridLayout.addWidget(self.rankLabel, 2, 6, 1, 1)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 2, 3, 2, 1)

        self.addReviewBtn = QPushButton(Form)
        self.addReviewBtn.setObjectName(u"addReviewBtn")

        self.gridLayout.addWidget(self.addReviewBtn, 7, 0, 1, 1)

        self.headerMarket = QLabel(Form)
        self.headerMarket.setObjectName(u"headerMarket")

        self.gridLayout.addWidget(self.headerMarket, 2, 0, 1, 3)

        self.categoriesLabel = QLabel(Form)
        self.categoriesLabel.setObjectName(u"categoriesLabel")

        self.gridLayout.addWidget(self.categoriesLabel, 2, 4, 2, 1)

        self.userLabel = QLabel(Form)
        self.userLabel.setObjectName(u"userLabel")

        self.gridLayout.addWidget(self.userLabel, 0, 0, 1, 2)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 6, 0, 1, 1)

        self.line_3 = QFrame(Form)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 2, 5, 2, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.deleteReviewBtn.setText(QCoreApplication.translate("Form", u"Delete review", None))
        self.editReviewBtn.setText(QCoreApplication.translate("Form", u"Edit review", None))
        self.marketLabel.setText(QCoreApplication.translate("Form", u"marketLabel", None))
        self.label_3.setText("")
        self.rankLabel.setText(QCoreApplication.translate("Form", u"rankLabel", None))
        self.addReviewBtn.setText(QCoreApplication.translate("Form", u"Add review", None))
        self.headerMarket.setText(QCoreApplication.translate("Form", u"headerMarket", None))
        self.categoriesLabel.setText(QCoreApplication.translate("Form", u"categoriesLabel", None))
        self.userLabel.setText(QCoreApplication.translate("Form", u"userLabel", None))
        self.label_2.setText("")
    # retranslateUi

