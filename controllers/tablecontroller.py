from models.tablemodel import Base, Collaborator, Customer, Role
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from urllib.parse import quote


class TableController:
    def __init__(self, jsoncontroller):
        self.json_c = jsoncontroller

    def create_table_all_controller(self, username_admin, password_admin, database_name):
        pass_admin = quote(password_admin)
        engine = create_engine(f'mysql+pymysql://{username_admin}:{pass_admin}@localhost/{database_name}')
        Base.metadata.create_all(bind=engine, tables=None, checkfirst=False)
        self.add_roles_in_the_table(username_admin, pass_admin, database_name)

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
            session.commit()

    def add_roles_in_the_table(self, username_admin, pass_admin, database_name):
        engine = create_engine(f'mysql+pymysql://{username_admin}:{pass_admin}@localhost/{database_name}')
        with Session(engine) as session:
            com = Role(
                name="COM"
            )
            ges = Role(
                name="GES"
            )
            sup = Role(
                name="SUP"
            )
            session.add_all([com, ges, sup])
            session.commit()

    def get_information_for_single_collaborator_controller(self, username_collab, password_collab):
        """
        Fonction qui permet de retourner les informations d'un seul collaborateur.
        Recherche avec username.

        :param username_collab
        :param password_collab
        :return: result
        """
        password = quote(password_collab)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{username_collab}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result = connection.execute(text(f"SELECT * FROM collaborator WHERE username = '{username_collab}'"))
            return result

    def get_information_for_all_collaborators_controller(self, username_collab, password_collab):
        """
        Fonction qui permet de retourner la liste complète des collaborateurs.

        :param username_collab:
        :param password_collab:
        :return:
        """
        password = quote(password_collab)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{username_collab}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result = connection.execute(text(f"SELECT * FROM collaborator"))
            return result

    def get_single_collaborator_info_with_id_controller(self, user_id, username_admin, password_admin):
        password = quote(password_admin)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{username_admin}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_user = connection.execute(text(f"SELECT * FROM collaborator JOIN role ON collaborator.role_id = "
                                                  f"role.id WHERE collaborator.id = '{user_id}'"))
            return result_user

    def edit_collaborator_fields(self):
        pass