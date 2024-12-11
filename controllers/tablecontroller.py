from models.tablemodel import Base, Collaborator, Customer, Role
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from urllib.parse import quote


class TableController:
    def __init__(self, jsoncontroller):
        self.json_c = jsoncontroller

    def create_table_all_controller(self, username_admin, password_admin, database_name):
        """
        Fonction qui permet de créer toutes les tables.

        :param username_admin:
        :param password_admin:
        :param database_name:
        """
        pass_admin = quote(password_admin)
        engine = create_engine(f'mysql+pymysql://{username_admin}:{pass_admin}@localhost/{database_name}')
        Base.metadata.create_all(bind=engine, tables=None, checkfirst=False)
        self.add_roles_in_the_table(username_admin, pass_admin, database_name)

    def save_collaborator_in_table_controller(self, username_collab, password_collab, info_name, info_first_name,
                                              info_email, info_username, info_password, role):
        """
        Fonction qui permet d'enregistrer un collaborateur dans la table.

        :param username_collab:
        :param password_collab:
        :param info_name:
        :param info_first_name:
        :param info_email:
        :param info_username:
        :param info_password:
        :param role:
        """
        database_name = self.json_c.get_database_name_in_json_file()  # Récupère le nom de la base de données
        password = quote(password_collab)
        engine = create_engine(f'mysql+pymysql://{username_collab}:{password}@localhost/{database_name}')
        with Session(engine) as session:
            collaborator = Collaborator(
                name=info_name,
                first_name=info_first_name,
                email=info_email,
                username=info_username,
                password=info_password,
                role_id=role
            )
            session.add(collaborator)
            session.commit()

    def add_roles_in_the_table(self, username_admin, pass_admin, database_name):
        """
        Fonction qui permet d'enregistrer les rôles dans la table.

        :param username_admin :
        :param pass_admin :
        :param database_name :
        """
        engine = create_engine(f'mysql+pymysql://{username_admin}:{pass_admin}@localhost/{database_name}')
        with Session(engine) as session:
            com = Role(
                role_name="COM"
            )
            ges = Role(
                role_name="GES"
            )
            sup = Role(
                role_name="SUP"
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
        :return: result
        """
        password = quote(password_collab)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{username_collab}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result = connection.execute(text(f"SELECT * FROM collaborator"))
            return result

    def get_single_collaborator_info_with_id_controller(self, user_id, username_admin, password_admin):
        """
        Fonction qui permet de récupérer les informations d'un utilisateur avec son ID.

        :param user_id :
        :param username_admin :
        :param password_admin :
        :return: result_user
        """
        password = quote(password_admin)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{username_admin}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_user = connection.execute(text(f"SELECT * FROM collaborator JOIN role ON collaborator.role_id = "
                                                  f"role.id WHERE collaborator.id = '{user_id}'"))
            return result_user

    def edit_collaborator_fields_controller(self, user_id, new_value, username_admin, password_admin, field):
        """
        Fonction qui permet de mettre à jour un champ concernant un collaborateur.

        :param user_id :
        :param new_value :
        :param username_admin :
        :param password_admin :
        :param field:
        :return: True
        """
        password = quote(password_admin)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{username_admin}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            connection.execute(text(f"UPDATE collaborator SET {field} = '{new_value}' WHERE id = {user_id}"))
            connection.commit()
            return True
