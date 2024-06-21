# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteConfirmation.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QGridLayout, QLabel, QSizePolicy, QWidget)

class Ui_onDelDialog(object):
    def setupUi(self, onDelDialog):
        if not onDelDialog.objectName():
            onDelDialog.setObjectName(u"onDelDialog")
        onDelDialog.resize(352, 148)
        self.gridLayout_2 = QGridLayout(onDelDialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(onDelDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.label = QLabel(onDelDialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(onDelDialog)
        self.buttonBox.accepted.connect(onDelDialog.accept)
        self.buttonBox.rejected.connect(onDelDialog.reject)

        QMetaObject.connectSlotsByName(onDelDialog)
    # setupUi

    def retranslateUi(self, onDelDialog):
        onDelDialog.setWindowTitle(QCoreApplication.translate("onDelDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("onDelDialog", u"Delete your review?", None))
    # retranslateUi

