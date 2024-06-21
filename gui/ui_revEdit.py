# -*- coding: utf-8 -*-
import datetime

from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QWidget, QComboBox, QHeaderView
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from sqlalchemy import create_engine, and_, text, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import update
from db_engine.model import State, City, Market, User, Country, Review
from gui.revEdit import Ui_Form


class Ui_ReviewEdit(QWidget, Ui_Form):
    def __init__(self, url, user, market, review):
        super().__init__()
        self.setupUi(self)

        self.__url = url
        self.__user = user
        # data = tuple (Market, City)
        self.__data = market
        self.__review = review

        self.fill_user_info()
        self.fill_market_info()
        self.fill_previos_review()

        self.scorePoint.setRange(0, 5)
        self.editReviewBtn.clicked.connect(self.edit_review)

    def fill_user_info(self):
        self.userLabel.setWordWrap(True)
        self.userLabel.setText(f"User_id: {self.__user.username}_{self.__user.id}\nFirst name: {self.__user.fname}"
                               f"\nLast name: {self.__user.lname}")

    def fill_market_info(self):
        self.marketLabel.setWordWrap(True)
        header = (f"Market(Id):\n{self.__data[0].name}({self.__data[0].id})\n")
        self.marketLabel.setText(header)

    def fill_previos_review(self):
        self.previousComment.setText(
            f"\"{self.__review[0].review}\"\n\n"
            f"Added on:\n"
            f"{self.__review[0].datetime.strftime("at %H:%M:%S on %m.%d.%Y")}"
        )
        self.prevGrade.setText(str(self.__review[0].score))

    def edit_review(self):
        self.previousComment.setText(
            f"\"{self.__review[0].review}\"\n"
            f"Added on:\n"
            f"{self.__review[0].datetime.strftime("at %H:%M:%S on %m.%d.%Y")}"
        )

        Session = sessionmaker(create_engine(self.__url))
        with Session() as session:
            session.execute(
                update(Review).where(Review.id == self.__review[0].id).values(
                    review=f"{self.plainTextEdit.toPlainText()}\n(edited "
                           f"on: {datetime.datetime.now().strftime("%H:%M:%S on %m.%d.%Y")})",
                    score=self.scorePoint.value()
                ))
            session.commit()
        self.close()