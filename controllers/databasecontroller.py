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
        """
        Fonction qui permet de créer une base de données.
        :param username:
        :param password1:
        :param database_name:
        """
        password2 = quote(password1)
        engine = create_engine(f'mysql+pymysql://{username}:{password2}@localhost')
        with engine.connect() as connection:
            connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))

    def save_collaborator_com_in_mysql_controller(self, username_admin, password_admin,
                                                  info_username, info_password):
        """
        Fonction qui permet d'enregistrer un nouveau collaborateur (Commercial) dans la base MySQL.
        Attributions de droits concernant son rôle.

        :param username_admin :
        :param password_admin :
        :param info_username :
        :param info_password :
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
        Fonction qui permet de créer un nouveau collaborateur (Gestion) dans la base MySQL.
        Attributions de droits selon son rôle.

        :param username_admin :
        :param password_admin :
        :param info_username :
        :param info_password :
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
            connection.execute(text(f"GRANT SELECT ON {database_name}.role "
                                    f"TO {info_username}@localhost"))

            "Pour que l'utilisateur Gestion puisse accorder des droits à d'autres collaborateur 'Gestion compris"
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.customer TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.contract TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.event TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.role TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON *.* TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON mysql.user TO {info_username}@localhost"))

    def save_collaborator_sup_in_mysql_controller(self, username_admin, password_admin,
                                                  info_username, info_password):
        """
        Fonction qui permet d'enregistrer un collaborateur (Support) dans la base MySQL.
        Attributions de droits selon son rôle.

        :param username_admin :
        :param password_admin :
        :param info_username :
        :param info_password :
        """
        pass_admin = quote(password_admin)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{username_admin}:{pass_admin}@localhost/{database_name}')
        with engine.connect() as connection:
            connection.execute(text(f"CREATE USER '{info_username}'@'localhost' IDENTIFIED BY '{info_password}'"))
            connection.execute(text(f"GRANT SELECT, UPDATE ON {database_name}.event "
                                    f"TO {info_username}@localhost"))

    def change_username_in_mysql_controller(self, username_admin, password_admin, old_username, new_username):
        """
        Fonction qui permet de modifier identifiant de connexion (username) d'un collaborateur dans la base MySQL.
        
        :param username_admin:
        :param password_admin:
        :param old_username:
        :param new_username:
        """
        password = quote(password_admin)
        engine = create_engine(f'mysql+pymysql://{username_admin}:{password}@localhost')
        with engine.connect() as connection:
            connection.execute(text(f"UPDATE mysql.user SET user='{new_username}' WHERE user='{old_username}' "))
            connection.commit()
