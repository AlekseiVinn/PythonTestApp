# -*- coding: utf-8 -*-
import statistics
from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QWidget, QComboBox, QHeaderView, QDialog
from PySide6.QtCore import QAbstractTableModel, QModelIndex, Qt
from sqlalchemy import create_engine, and_, text, select
from sqlalchemy.orm import sessionmaker
from db_engine.model import State, City, Market, User, Country, Review
from gui.details_page import Ui_Form
from gui.ui_revCreate import Ui_ReviewAdd
from gui.ui_revEdit import Ui_ReviewEdit
from gui.deleteConfirmation import Ui_onDelDialog


class Ui_Details(QWidget, Ui_Form):
    def __init__(self, url, user, market):
        super().__init__()
        self.setupUi(self)

        self.__url = url
        self.__user = user
        # data = tuple (Market, City.name)
        self.__data = market
        self.__review = []

        self.fill_user_info()
        self.fill_market_info()
        self.fill_rank_info()


        self.model = ReviewView(self.__url)
        self.model.setitems(self.__data[0])
        self.reviewsView.setModel(self.model)
        self.reviewsView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        self.reviewsView.clicked.connect(self.table_selected)
        self.addReviewBtn.clicked.connect(self.add_review)
        self.editReviewBtn.clicked.connect(self.edit_review)
        self.deleteReviewBtn.clicked.connect(self.delite_review)


    def fill_user_info(self):
        self.userLabel.setWordWrap(True)
        self.userLabel.setText(f"User_id: {self.__user.username}_{self.__user.id}\nFirst name: {self.__user.fname}"
                               f"\nLast name: {self.__user.lname}")

    def fill_market_info(self):
        self.headerMarket.setWordWrap(True)
        header = (f"Market(Id):\n{self.__data[0].name}({self.__data[0].id})\n"
                  f"*last updated: {self.__data[0].lastupdated}")
        self.headerMarket.setText(header)
        self.marketLabel.setWordWrap(True)
        catehories = list(map(lambda x: f"-{x.name}\n", self.__data[0].categories))
        catehories = ''.join(catehories)
        self.categoriesLabel.setText(f"Categories:\n"
                                     f"{catehories}")
        res_string = (f"ZIP, City: {self.__data[0].zip}, {self.__data[1]}\n"
                      f"Street: {self.__data[0].street} "
                      f"(location:  {self.__data[0].lat:10.6f}, {self.__data[0].lon:10.6f})\n"
                      f"Media:\n"
                      f"\twebsite: {self.__data[0].website if self.__data[0].website != '' else '-'}\n"
                      f"\tfacebook: {self.__data[0].facebook if self.__data[0].facebook != '' else '–'}\n"
                      f"\ttwitter: {self.__data[0].twitter if self.__data[0].twitter != '' else '-'}\n"
                      f"\tyoutube: {self.__data[0].youtube if self.__data[0].youtube != '' else '-'}\n"
                      f"\tother: {self.__data[0].media if self.__data[0].media != '' else '-'}\n"
                      f"Season date | time\n"
                      f"\tseason 1: {self.__data[0].season1date if self.__data[0].season1date != '' else '-'} |"
                      f" {self.__data[0].season1time if self.__data[0].season1time != '' else '–'}\n"
                      f"\tseason 2: {self.__data[0].season2date if self.__data[0].season2date != '' else '-'} |"
                      f" {self.__data[0].season2time if self.__data[0].season2time != '' else '–'}\n"
                      f"\tseason 3: {self.__data[0].season3date if self.__data[0].season3date != '' else '-'} |"
                      f" {self.__data[0].season3time if self.__data[0].season3time != '' else '–'}\n"
                      f"\tseason 4: {self.__data[0].season4date if self.__data[0].season4date != '' else '-'} |"
                      f" {self.__data[0].season4time if self.__data[0].season4time != '' else '–'}\n"
                      f"Other info:\t"
                      f"{'Credit, ' if self.__data[0].credit else ' '}"
                      f"{'WIC, ' if self.__data[0].wic else ' '}"
                      f"{'WICCash, ' if self.__data[0].wiccsah else ' '}"
                      f"{'SFMNP, ' if self.__data[0].sfmnp else ' '}"
                      f"{'SNAP' if self.__data[0].snap else ' '}\n")
        self.marketLabel.setText(res_string)

    def fill_rank_info(self):
        ranks = []
        Session = sessionmaker(create_engine(self.__url))
        ranking = "-"
        with Session() as session:
            reviews = session.query(Review.score).where(Review.market_id == self.__data[0].id).all()
            if len(reviews) > 0:
                rev = list(map(lambda x: x[0],reviews))
                ranking = statistics.mean(list(rev))
        self.rankLabel.setText(f"Market rating:\n{ranking}")

    def table_selected(self, item):
        self.editReviewBtn.setDisabled(True)
        self.deleteReviewBtn.setDisabled(True)
        # reviews - список формы [(Review, User),]
        self.__review = item.data(QtCore.Qt.ItemDataRole.UserRole)
        if self.__review[1].id == self.__user.id:
            self.editReviewBtn.setEnabled(True)
            self.deleteReviewBtn.setEnabled(True)

    def add_review(self):
        # self.__data = tuple (Market, City.name)
        self.addWidget = Ui_ReviewAdd(self.__url, self.__user, self.__data)
        self.addWidget.setWindowModality(QtCore.Qt.ApplicationModal)
        self.addWidget.show()
        self.addWidget.closeEvent = self.update_table

    def edit_review(self):
        # self.__data = tuple (Market, City.name)
        self.editWidget = Ui_ReviewEdit(self.__url, self.__user, self.__data, self.__review)
        self.editWidget.setWindowModality(QtCore.Qt.ApplicationModal)
        self.editWidget.show()
        self.editWidget.closeEvent = self.update_table

    def delite_review(self):
        # self.__data = tuple (Market, City.name)
        self.DeleteDialog = QDialog()
        self.uiDel = Ui_onDelDialog()
        self.uiDel.setupUi(self.DeleteDialog)
        self.DeleteDialog.setWindowModality(QtCore.Qt.ApplicationModal)
        self.check = self.DeleteDialog.exec()
        if self.check:
            Session = sessionmaker(create_engine(self.__url))
            with Session() as session:
                session.delete(self.__review[0])
                session.commit()
            self.update_table(None)



    def update_table(self, e):
        self.model.setitems(self.__data[0])
        self.fill_rank_info()


class ReviewView(QAbstractTableModel):

    def __init__(self, url):
        super().__init__()
        # reviews - список формы [(Review, User),]
        self.reviews = []
        self.url = url

    def setitems(self, items):
        self.reviews = []
        self.beginResetModel()

        Session = sessionmaker(create_engine(self.url))
        with Session() as session:
            reviews = (session.query(Review, User).
                            join(User).
                            where(Review.market_id == items.id).all())
            if len(reviews) > 0:
                for review in reviews:
                    self.reviews.append(review)
        self.endResetModel()

    def rowCount(self, *args, **kwargs):
        return len(self.reviews)

    def columnCount(self, *args, **kwargs):
        return 5

    def data(self, index: QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            review = self.reviews[index.row()]
            col = index.column()
            if col == 0:
                return f"Review №{review[0].id}"
            elif col == 1:
                return f"User_{review[1].id}: {review[1].fname} {review[1].lname}"
            elif col == 2:
                return review[0].review
            elif col == 3:
                return f"{review[0].score}"
            elif col == 4:
                return f"{review[0].datetime.strftime("at %H:%M:%S on %m.%d.%Y")}"
        elif role == QtCore.Qt.ItemDataRole.UserRole:
            return self.reviews[index.row()]

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: "id",
                    1: "User",
                    2: "Commentary",
                    3: "Score",
                    4: "Commented",
                }.get(section)
