from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from db_engine.db_urls import postgres_db_url, app_db_url
from db_engine.model import Base
from seed_db_utils import create_db_user, seed_all_data


print("\nЗапуск скрипта для создания и наполнения базы данных Farmers Markets на сервере Postgresql.")
username = input("Введите имя пользователя-администратора сервера Postgresql (обычно, postgres): ")
password = input(f"Введите пароль пользователя {username}: ")


conn_string = postgres_db_url(username, password)
engine = create_engine(conn_string)

#создание базы данных из-под рута
try:
    database_exists(engine.url)
except:
    print("База \"Farmers Markets\" не обнаружена.")
    # if input("Создать базу \"Farmers Markets\"? (Y/N): ") == "Y":
    if 1:
        try:
            create_database(engine.url)
            create_db_user(engine)
        except Exception as e:
            raise e

if database_exists(app_db_url):
    print("Успешно созданы база данных и пользователь marketuser для подключения к БД.")
    print("Считывание БД из Export.csv...")
    del engine, conn_string

    # Заполняем БД через новое подключение
    engine2 = create_engine(app_db_url)
    Base.metadata.create_all(engine2)
    seed_all_data(engine2)
    print("Скрипт закончил выполнение, можно запускать приложение для работы")
