# -*- coding: utf-8 -*-
import datetime

from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QWidget, QComboBox, QHeaderView
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from sqlalchemy import create_engine, and_, text, select
from sqlalchemy.orm import sessionmaker
from db_engine.model import State, City, Market, User, Country, Review
from gui.revCreate import Ui_Form


class Ui_ReviewAdd(QWidget, Ui_Form):
    def __init__(self, url, user, market):
        super().__init__()
        self.setupUi(self)

        self.__url = url
        self.__user = user
        # data = tuple (Market, City)
        self.__data = market
        self.__review = []

        self.fill_user_info()
        self.fill_market_info()

        self.scorePoint.setRange(0, 5)
        self.addReviewBtn.clicked.connect(self.create_review)

    def fill_user_info(self):
        self.userLabel.setWordWrap(True)
        self.userLabel.setText(f"User_id: {self.__user.username}_{self.__user.id}\nFirst name: {self.__user.fname}"
                               f"\nLast name: {self.__user.lname}")

    def fill_market_info(self):
        self.marketLabel.setWordWrap(True)
        header = (f"Market(Id):\n{self.__data[0].name}({self.__data[0].id})\n")
        self.marketLabel.setText(header)

    def create_review(self):
        Session = sessionmaker(create_engine(self.__url))
        with Session() as session:
            session.add(Review(
                user_id=self.__user.id,
                market_id=self.__data[0].id,
                datetime=datetime.datetime.now(),
                score=self.scorePoint.value(),
                review=self.plainTextEdit.toPlainText()
            )
            )
            session.commit()
        self.close()