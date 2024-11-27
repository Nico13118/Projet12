from sqlalchemy import create_engine, text
from urllib.parse import quote


class DatabaseController:
    def create_databases_controller(self, username, password1, database_name):
        password2 = quote(password1)
        engine = create_engine(f'mysql+pymysql://{username}:{password2}@localhost')
        with engine.connect() as connection:
            connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))
