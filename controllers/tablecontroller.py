from models.tablemodel import Base, Collaborator, Customer
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from urllib.parse import quote


class TableController:
    def __init__(self, jsoncontroller):
        self.json_c = jsoncontroller

    def create_table_all_controller(self, username, password1, database_name):
        password2 = quote(password1)
        engine = create_engine(f'mysql+pymysql://{username}:{password2}@localhost/{database_name}')
        Base.metadata.create_all(bind=engine, tables=None, checkfirst=False)

    def save_collaborator_in_table_controller(self, username_collab, password_collab, info_name, info_first_name,
                                              info_email, info_username, info_password, role):
        database_name = self.json_c.get_database_name_in_json_file()  # Récupère le nom de la base de données
        password = quote(password_collab)
        engine = create_engine(f'mysql+pymysql://{username_collab}:{password}@localhost/{database_name}')
        with Session(engine) as session:
            commercial = Collaborator(
                name=info_name,
                first_name=info_first_name,
                email=info_email,
                username=info_username,
                password=info_password,
                role_id=role
            )
            session.add(commercial)




