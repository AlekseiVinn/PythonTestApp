import sys
from db_engine.db_urls import app_db_url

from PySide6.QtWidgets import QApplication

from gui.ui_login_page import UI_login

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = UI_login(app_db_url)
    widget.show()
    sys.exit(app.exec())
