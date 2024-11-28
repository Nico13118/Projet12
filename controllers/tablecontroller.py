from models.tablemodel import Base, Collaborator, Customer
from sqlalchemy import create_engine
from urllib.parse import quote


class TableController:
    def create_table_all_controller(self, username, password1, database_name):
        password2 = quote(password1)
        engine = create_engine(f'mysql+pymysql://{username}:{password2}@localhost/{database_name}')
        Base.metadata.create_all(bind=engine, tables=None, checkfirst=False)
