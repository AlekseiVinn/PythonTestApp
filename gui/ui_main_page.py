# -*- coding: utf-8 -*-
import statistics

from PySide6 import QtCore
from PySide6.QtWidgets import QMainWindow, QWidget, QComboBox, QHeaderView
from PySide6.QtCore import QAbstractTableModel, QModelIndex
from sqlalchemy import create_engine, and_, text, select
from sqlalchemy.orm import sessionmaker
from threading import Thread


from gui.main_page import Ui_MainWindow
from gui.ui_details_page import Ui_Details
from db_engine.model import State, City, Market, User, Country, Review


class UiMain(QMainWindow, Ui_MainWindow):
    def __init__(self, url, user):
        super().__init__()
        self.setupUi(self)

        #todo - по self.__user сделать проверку идентификации
        self.__user = user
        #ссылка для подключения
        self.__url = url
        # список (название штата, список (города) )
        self.__addr_guide = list()

        self.__engine = create_engine(self.__url)
        # список рынков (Market, City.name)
        self.__markets = self.init_markets()

        self.model = MarketView(self.__url)
        self.model.setitems(self.__markets)

        self.table.setModel(self.model)
        self.set_rows()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.selecte_market_bar.setWordWrap(True)
        self.radiusSlider.setRange(0, 30)
        self.radiusSlider.setSingleStep(1)
        self.radiusSlider.setValue(0)
        self.details_market_btn.setDisabled(True)

        self.get_states()
        self.fill_user_info()
        self.state_comboBox.activated.connect(self.get_cities)
        self.state_comboBox.activated.connect(self.get_markets_by_state)
        self.state_comboBox.activated.connect(self.set_rows)
        self.city_comboBox.addItems(self.get_allcities())
        self.city_comboBox.activated.connect(self.get_markets_by_city)
        self.city_comboBox.activated.connect(self.set_rows)
        self.zip_input.textChanged.connect(self.get_markets_by_zip)
        self.zip_input.textChanged.connect(self.set_rows)
        self.table.clicked.connect(self.table_selected)
        self.radiusSlider.valueChanged.connect(self.update_slider)
        self.details_market_btn.clicked.connect(self.open_details)

    def update_slider(self, value):
        self.radius.setText(f'Radius, miles: {value}')

    def get_states(self):
        # загрузка списка(название штата, список(города)) и наполнение списка штатов в интерфейс
        Session = sessionmaker(self.__engine)
        with Session() as session:
            states = session.query(State).order_by(State.name).all()
            for state in states:
                countries = session.query(Country.id).where(Country.state_id == state.id).all()
                res_cities = list()
                for country in countries:
                    cities = session.query(City).where(City.country_id == country.id).all()
                    for city in cities:
                        res_cities.append(city)
                self.__addr_guide.append(list((state, res_cities)))
        for x in self.__addr_guide:
            self.state_comboBox.addItem(x[0].name, list(map(lambda city: f"{city.id}, {city.name}", x[1])))
        self.state_comboBox.addItem('ALL STATES AND CITIES')

    def get_cities(self, index):
        # обновление списка городов по выбранному штату в интерфейс
        self.city_comboBox.clear()
        if self.state_comboBox.currentText() != 'ALL STATES AND CITIES':
            self.city_comboBox.addItems(self.state_comboBox.itemData(index))
        else:
            self.city_comboBox.addItems(self.get_allcities())

    def get_allcities(self):
        # первоначальная загрузка списка городов в интерфейс
        result = list()
        for row in self.__addr_guide:
            for city in row[1]:
                result.append(f"{city.id}, {city.name}")
        result.sort()
        return result

    def init_markets(self):
        # загрузка списка рынков из БД
        Session = sessionmaker(self.__engine)
        result = []
        with Session() as session:
            markets = list(session.query(Market, City.name).join(City).order_by(Market.id).all())
        return markets

    def get_markets_by_state(self, index):
        # загрузка списка рынков из БД по штату
        self.__markets = list()

        if self.state_comboBox.currentText() != 'ALL STATES AND CITIES':
            cities_id = list(map(lambda x: int(x.split(sep=",")[0]), self.state_comboBox.itemData(index)))
            Session = sessionmaker(self.__engine)
            with Session() as session:
                for city_id in cities_id:
                    markets = list(session.query(Market, City.name).join(City).where(Market.city_id == city_id)
                                   .order_by(Market.id).all())
                    for market in markets:
                        self.__markets.append(market)
        else:
            self.__markets = self.init_markets()

        self.model.setitems(self.__markets)

    def get_markets_by_city(self, index):
        # загрузка списка рынков из БД по городу
        self.__markets = list()
        city_id = self.city_comboBox.itemText(index).split(sep=",")[0]
        Session = sessionmaker(self.__engine)
        with Session() as session:
            markets = list(session.query(Market, City.name).join(City).where(Market.city_id == city_id)
                           .order_by(Market.id).all())
            for market in markets:
                self.__markets.append(market)
        self.model.setitems(self.__markets)

    def get_markets_by_zip(self):
        # загрузка списка рынков из БД по индексу
        self.__markets = list()
        zip = self.zip_input.text()
        Session = sessionmaker(self.__engine)
        with Session() as session:
            markets = list(
                session.query(Market, City.name).join(City).
                where(Market.zip.startswith(zip)).
                order_by(Market.id).all())
            for market in markets:
                self.__markets.append(market)
        self.model.setitems(self.__markets)

    def table_selected(self, item):
        # data = tuple (Market, City.name)
        self.data = item.data(QtCore.Qt.ItemDataRole.UserRole)
        self.details_market_btn.setEnabled(True)
        self.selecte_market_bar.setText(str(self.data[0].id) + ' - ' + self.data[0].name)

    def set_rows(self):
        self.tableTotalLabel.setText(str(len(self.table.model().markets)))

    def open_details(self):
        if self.selecte_market_bar.text() != '':
            self.detailsWidget = Ui_Details(self.__url, self.__user, self.data)
            self.detailsWidget.setWindowModality(QtCore.Qt.ApplicationModal)
            self.detailsWidget.show()

    def fill_user_info(self):
        self.userLabel.setWordWrap(True)
        self.userLabel.setText(f"User_id: {self.__user.username}_{self.__user.id}\nFirst name: {self.__user.fname}"
                               f"\nLast name: {self.__user.lname}\n")


class MarketView(QAbstractTableModel):

    def __init__(self, url):
        super().__init__()
        self.markets = []
        self.url = url

    def setitems(self, item):
        self.beginResetModel()
        self.markets = item
        self.endResetModel()

    def rowCount(self, *args, **kwargs):
        return len(self.markets)

    def columnCount(self, *args, **kwargs):
        return 7

    def data(self, index: QModelIndex, role: QtCore.Qt.ItemDataRole):
        if not index.isValid():
            return

        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            market, city = self.markets[index.row()]
            col = index.column()
            if col == 0:
                return f'{market.id}'
            elif col == 1:
                return market.name
            elif col == 2:
                return city
            elif col == 3:
                return market.street
            elif col == 4:
                return market.zip
            elif col == 5:
                return market.lat
            elif col == 6:
                return market.lon

        elif role == QtCore.Qt.ItemDataRole.UserRole:
            return self.markets[index.row()]

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                return {
                    0: "id",
                    1: "Market",
                    2: "City",
                    3: "Address",
                    4: "ZIP",
                    5: "Lat",
                    6: "Lon",
                }.get(section)
