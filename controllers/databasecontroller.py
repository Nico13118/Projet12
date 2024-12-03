from sqlalchemy import create_engine, text
from urllib.parse import quote


class DatabaseController:
    def __init__(self, jsoncontroller):
        self.json_c = jsoncontroller

    def create_databases_controller(self, username, password1, database_name):
        password2 = quote(password1)
        engine = create_engine(f'mysql+pymysql://{username}:{password2}@localhost')
        with engine.connect() as connection:
            connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))

    def save_collaborator_com_in_mysql_controller(self, username_admin, password_admin,
                                                  info_username, info_password):
        """
        Le commercial doit pouvoir :
        Customer : Créer ou mettre à jour des clients. >> Table customer SELECT, INSERT, UPDATE
        Contract : Modifier / Mettre à jour les contrats >> Table contract SELECT, INSERT, UPDATE
        Event :  Créer un évènement INSERT,

        """
        pass_admin = quote(password_admin)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{username_admin}:{pass_admin}@localhost/{database_name}')
        with engine.connect() as connection:
            connection.execute(text(f"CREATE USER {info_username}@localhost IDENTIFIED BY {info_password}"))
            connection.execute(text(f"GRANT SELECT, INSERT, UPDATE ON {database_name}.customer "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, INSERT, UPDATE ON {database_name}.contract "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT INSERT ON {database_name}.event TO {info_username}@localhost"))
            connection.execute(text("FLUSH PRIVILEGES"))

    def save_collaborator_ges_in_mysql_controller(self, username_admin, password_admin,
                                                  info_username, info_password):
        """
        La gestion doit pouvoir :
        Collaborator : Créer, mettre à jour et supprimer des collaborateurs >> SELECT, INSERT, UPDATE, DELETE.
        Contract : Créer et modifier tous les contrats >> INSERT, UPDATE.
        Event : Afficher et modifier des évènements SELECT, UPDATE.
        """
        pass_admin = quote(password_admin)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{username_admin}:{pass_admin}@localhost/{database_name}')
        with engine.connect() as connection:
            connection.execute(text(f"CREATE USER {info_username}@localhost IDENTIFIED BY {info_password}"))
            connection.execute(text(f"GRANT SELECT, INSERT, UPDATE, DELETE ON {database_name}.collaborator "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT INSERT, UPDATE ON {database_name}.contract "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, UPDATE ON {database_name}.event "
                                    f"TO {info_username}@localhost"))
            connection.execute(text("FLUSH PRIVILEGES"))

    def save_collaborator_sup_in_mysql_controller(self, username_admin, password_admin,
                                                  info_username, info_password):
        """
        Le support doit pouvoir :
        Event : Afficher et mettre à jour les évènements >> SELECT, UPDATE.
        """
        pass_admin = quote(password_admin)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{username_admin}:{pass_admin}@localhost/{database_name}')
        with engine.connect() as connection:
            connection.execute(text(f"CREATE USER {info_username}@localhost IDENTIFIED BY {info_password}"))
            connection.execute(text(f"GRANT SELECT, UPDATE ON {database_name}.event "
                                    f"TO {info_username}@localhost"))
            connection.execute(text("FLUSH PRIVILEGES"))
            