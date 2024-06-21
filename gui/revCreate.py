# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'revCreate.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QPlainTextEdit, QPushButton, QSizePolicy, QSpinBox,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(439, 300)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 3, 0, 1, 3)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 6, 1, 1, 1)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 1, 0, 1, 3)

        self.marketLabel = QLabel(Form)
        self.marketLabel.setObjectName(u"marketLabel")

        self.gridLayout.addWidget(self.marketLabel, 0, 0, 1, 3)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 5, 0, 1, 2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 4, 2, 1, 1)

        self.userLabel = QLabel(Form)
        self.userLabel.setObjectName(u"userLabel")

        self.gridLayout.addWidget(self.userLabel, 2, 0, 1, 2)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 4, 0, 1, 1)

        self.addReviewBtn = QPushButton(Form)
        self.addReviewBtn.setObjectName(u"addReviewBtn")

        self.gridLayout.addWidget(self.addReviewBtn, 6, 0, 1, 1)

        self.scorePoint = QSpinBox(Form)
        self.scorePoint.setObjectName(u"scorePoint")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scorePoint.sizePolicy().hasHeightForWidth())
        self.scorePoint.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.scorePoint, 5, 2, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Review", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.marketLabel.setText(QCoreApplication.translate("Form", u"marketLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"Market grade:", None))
        self.userLabel.setText(QCoreApplication.translate("Form", u"userLabel", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Your commentary:", None))
        self.addReviewBtn.setText(QCoreApplication.translate("Form", u"Add reivew", None))
    # retranslateUi

