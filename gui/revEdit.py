# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'revEdit.ui'
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
        Form.resize(504, 296)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.scorePoint = QSpinBox(Form)
        self.scorePoint.setObjectName(u"scorePoint")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scorePoint.sizePolicy().hasHeightForWidth())
        self.scorePoint.setSizePolicy(sizePolicy)

        self.gridLayout.addWidget(self.scorePoint, 6, 4, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4.setWordWrap(True)

        self.gridLayout.addWidget(self.label_4, 5, 3, 1, 1)

        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.gridLayout.addWidget(self.plainTextEdit, 6, 1, 1, 2)

        self.previousComment = QLabel(Form)
        self.previousComment.setObjectName(u"previousComment")
        self.previousComment.setWordWrap(True)

        self.gridLayout.addWidget(self.previousComment, 6, 0, 1, 1)

        self.editReviewBtn = QPushButton(Form)
        self.editReviewBtn.setObjectName(u"editReviewBtn")

        self.gridLayout.addWidget(self.editReviewBtn, 7, 1, 1, 1)

        self.prevGrade = QLabel(Form)
        self.prevGrade.setObjectName(u"prevGrade")
        self.prevGrade.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.prevGrade, 6, 3, 1, 1)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 5, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 5, 1, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.label, 5, 4, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 7, 2, 1, 1)

        self.userLabel = QLabel(Form)
        self.userLabel.setObjectName(u"userLabel")

        self.gridLayout.addWidget(self.userLabel, 3, 0, 1, 3)

        self.marketLabel = QLabel(Form)
        self.marketLabel.setObjectName(u"marketLabel")

        self.gridLayout.addWidget(self.marketLabel, 1, 0, 1, 3)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 3)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line, 4, 0, 1, 5)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)
        self.pushButton_2.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Review edit", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Previous grade:", None))
        self.previousComment.setText(QCoreApplication.translate("Form", u"previousComment", None))
        self.editReviewBtn.setText(QCoreApplication.translate("Form", u"Edit reivew", None))
        self.prevGrade.setText(QCoreApplication.translate("Form", u"prevGrade", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Previous commentary: ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Your commentary:", None))
        self.label.setText(QCoreApplication.translate("Form", u"Market grade:", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.userLabel.setText(QCoreApplication.translate("Form", u"userLabel", None))
        self.marketLabel.setText(QCoreApplication.translate("Form", u"marketLabel", None))
    # retranslateUi

