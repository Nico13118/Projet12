from sqlalchemy import create_engine, text
from urllib.parse import quote
from sqlalchemy.exc import OperationalError


class DatabaseController:
    def __init__(self, jsoncontroller):
        self.json_c = jsoncontroller

    def test_username_password_controller(self, username_admin, password_admin):
        """
        Fonction qui permet de tester les identifiants de connexion d'un compte MySQL.
        : param username_admin :
        : param password_admin :
        : return : True / False
        """
        pass_admin = quote(password_admin)
        try:
            engine = create_engine(f'mysql+pymysql://{username_admin}:{pass_admin}@localhost')
            with engine.connect() as connection:
                return True
        except OperationalError:
            return False

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
            connection.execute(text(f"CREATE USER '{info_username}'@'localhost' IDENTIFIED BY '{info_password}'"))
            connection.execute(text(f"GRANT SELECT, INSERT, UPDATE ON {database_name}.customer "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, INSERT, UPDATE ON {database_name}.contract "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT INSERT ON {database_name}.event TO {info_username}@localhost"))

    def save_collaborator_ges_in_mysql_controller(self, username_admin, password_admin,
                                                  info_username, info_password):
        """

        :param username_admin:
        :param password_admin:
        :param info_username:
        :param info_password:
        :return:
        """
        pass_admin = quote(password_admin)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{username_admin}:{pass_admin}@localhost/{database_name}')
        with engine.connect() as connection:

            " Permet d'enregistrer un User MySQL"
            connection.execute(text(f"CREATE USER '{info_username}'@'localhost' IDENTIFIED BY '{info_password}'"))

            " Configuration des droits de l'utilisateur Gestion pour manipuler les User MSQL."
            connection.execute(text(f"GRANT CREATE USER, DROP ON *.* TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, UPDATE ON mysql.user TO {info_username}@localhost"))

            " Configuration des droits de l'utilisateur Gestion pour manipuler les tables."
            connection.execute(text(f"GRANT SELECT, INSERT, UPDATE, DELETE ON {database_name}.collaborator "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, INSERT, UPDATE ON {database_name}.customer "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, INSERT, UPDATE ON {database_name}.contract "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, INSERT, UPDATE ON {database_name}.event "
                                    f"TO {info_username}@localhost"))

            "Pour que l'utilisateur Gestion puisse accorder des droits à d'autres collaborateur 'Gestion compris"
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.customer TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.contract TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.event TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON *.* TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON mysql.user TO {info_username}@localhost"))

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
            connection.execute(text(f"CREATE USER '{info_username}'@'localhost' IDENTIFIED BY '{info_password}'"))
            connection.execute(text(f"GRANT SELECT, UPDATE ON {database_name}.event "
                                    f"TO {info_username}@localhost"))
