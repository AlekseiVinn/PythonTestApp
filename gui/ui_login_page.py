# -*- coding: utf-8 -*-
import sys
import hashlib
import random
from db_engine.db_urls import app_db_url
from gui.login_page import Ui_login_page
from gui.ui_main_page import UiMain
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDialog, QApplication, QMainWindow
from sqlalchemy import create_engine, and_, select
from sqlalchemy.orm import sessionmaker
from db_engine.model import User


def hashpass(text):
    hash_object = hashlib.sha256(text.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig


class UI_login(QDialog, Ui_login_page):
    def __init__(self, url):
        super().__init__()
        self.setupUi(self)
        self.__url = url
        self.__user = User()

        self.login_btn.clicked.connect(self.login)

        self.login_btn.clicked.connect(self.close)

        self.sign_in_btn.clicked.connect(self.register)
        self.login_txtbox.textChanged.connect(lambda: self.status_lbl.setText(''))
        self.pass_txtbox.textChanged.connect(lambda: self.status_lbl.setText(''))

    def login(self):
        usern = self.login_txtbox.text()
        userp = self.pass_txtbox.text()

        if usern != '' and userp !='':
            userp = hashpass(userp)

            engine = create_engine(self.__url)
            Session = sessionmaker(engine)

            with Session() as session:
                try:
                    userlog = session.scalar(select(User).where(and_(User.username == usern, User.passhash == userp)))
                    if userlog is not None:
                        self.__user = userlog
                        #todo - open main window
                        #print("зашел")
                        self.openMain()
                    else:
                        self.login_txtbox.setText('')
                        self.pass_txtbox.setText('')
                        self.status_lbl.setText("Incorrect login or password. Please, try again.")
                except Exception as e:
                    print(e)
        else:
            self.login_txtbox.setText('')
            self.pass_txtbox.setText('')
            self.status_lbl.setText("Incorrect login or password. Please, try again.")

    def register(self):
        usern = self.login_txtbox.text()
        userp = self.pass_txtbox.text()

        if usern != '' and userp != '':
            userp = hashpass(userp)

            engine = create_engine(self.__url)
            Session = sessionmaker(engine)

            with (Session() as session):
                try:
                    userlog = session.scalar(select(User).where(and_(User.username == usern)))
                    if userlog is None or usern != userlog.username:
                        session.add(User(fname=f"Имя{random.randint(0, 100)}", lname=f"Фамилия{random.randint(0, 100)}",
                                         username=usern, passhash=userp))
                        session.commit()
                        self.login_txtbox.setText('')
                        self.pass_txtbox.setText('')
                        self.status_lbl.setText("You have successfully registered. Now you can log in")
                    else:
                        self.login_txtbox.setText('')
                        self.pass_txtbox.setText('')
                        self.status_lbl.setText("Incorrect login or password. Please, try again.")
                except Exception as e:
                    print(e)
        else:
            self.login_txtbox.setText('')
            self.pass_txtbox.setText('')
            self.status_lbl.setText("Incorrect login or password. Please, try again.")

    def openMain(self):
        self.mainWindow = UiMain(self.__url, self.__user)
        self.mainWindow.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = UI_login(app_db_url)

    widget.show()
    sys.exit(app.exec())
