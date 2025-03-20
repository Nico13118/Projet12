from sqlalchemy import create_engine, text
from urllib.parse import quote
from sqlalchemy.exc import OperationalError


class DatabaseController:
    def __init__(self, jsoncontroller):
        self.session = None
        self.json_c = jsoncontroller

    def test_username_password_controller(self, session):
        """
        Fonction qui permet de tester les identifiants de connexion d'un compte MySQL.
        :param session
        :return : True / False
        """
        self.session = session
        pass_admin = quote(self.session.password)
        try:
            engine = create_engine(f'mysql+pymysql://{self.session.username}:{pass_admin}@localhost')
            with engine.connect() as connection:
                return True
        except OperationalError:
            return False

    def create_databases_controller(self, session, database_name):
        """
        Fonction qui permet de créer une base de données.

        :param session
        :param database_name
        """
        self.session = session
        password = quote(self.session.password)
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost')
        with engine.connect() as connection:
            connection.execute(text(f"CREATE DATABASE IF NOT EXISTS {database_name}"))

    def save_collaborator_com_in_mysql_controller(self, session, info_username, info_password):
        """
        Fonction qui permet d'enregistrer un nouveau collaborateur (Commercial) dans la base MySQL.
        Attributions de droits concernant son rôle.

        :param session
        :param info_username :
        :param info_password :
        """
        self.session = session
        pass_admin = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{pass_admin}@localhost/{database_name}')
        with engine.connect() as connection:
            connection.execute(text(f"CREATE USER '{info_username}'@'localhost' IDENTIFIED BY '{info_password}'"))
            connection.execute(text(f"GRANT SELECT ON {database_name}.collaborator"
                                    f" TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, INSERT, UPDATE ON {database_name}.customer "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, INSERT, UPDATE ON {database_name}.contract "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, INSERT ON {database_name}.event TO {info_username}@localhost"))

            connection.execute(text(f"GRANT SELECT ON {database_name}.contractstatus "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT ON {database_name}.role TO {info_username}@localhost"))
            connection.commit()

    def save_collaborator_ges_in_mysql_controller(self, session, info_username, info_password):
        """
        Fonction qui permet de créer un nouveau collaborateur (Gestion) dans la base MySQL.
        Attributions de droits selon son rôle.

        :param session
        :param info_username :
        :param info_password :
        """
        self.session = session
        pass_admin = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{pass_admin}@localhost/{database_name}')
        with engine.connect() as connection:

            " Permet d'enregistrer un User MySQL"
            connection.execute(text(f"CREATE USER '{info_username}'@'localhost' IDENTIFIED BY '{info_password}'"))

            " Configuration des droits de l'utilisateur Gestion pour manipuler les User MSQL."
            connection.execute(text(f"GRANT RELOAD, CREATE USER, DROP ON *.* TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, UPDATE, DROP ON mysql.user TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, UPDATE, DROP ON mysql.tables_priv "
                                    f"TO {info_username}@localhost"))

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
            connection.execute(text(f"GRANT SELECT ON {database_name}.contractstatus "
                                    f"TO {info_username}@localhost"))

            "Pour que l'utilisateur Gestion puisse accorder des droits à d'autres collaborateur 'Gestion compris"
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.collaborator TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.customer TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.contract TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.event TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.role TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON {database_name}.contractstatus "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON *.* TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON mysql.user TO {info_username}@localhost"))
            connection.execute(text(f"GRANT GRANT OPTION ON mysql.tables_priv TO {info_username}@localhost"))

    def save_collaborator_sup_in_mysql_controller(self, session, info_username, info_password):
        """
        Fonction qui permet d'enregistrer un collaborateur (Support) dans la base MySQL.
        Attributions de droits selon son rôle.

        :param session
        :param info_username :
        :param info_password :
        """
        self.session = session
        pass_admin = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{pass_admin}@localhost/{database_name}')
        with engine.connect() as connection:
            connection.execute(text(f"CREATE USER '{info_username}'@'localhost' IDENTIFIED BY '{info_password}'"))
            connection.execute(text(f"GRANT SELECT ON {database_name}.collaborator "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT ON {database_name}.customer "
                                    f"TO {info_username}@localhost"))
            connection.execute(text(f"GRANT SELECT, UPDATE ON {database_name}.event "
                                    f"TO {info_username}@localhost"))

    def change_username_in_mysql_controller(self, session, old_username, new_username):
        """
        Fonction qui permet de modifier un identifiant de connexion (username) d'un collaborateur dans la base MySQL.

        :param session
        :param old_username :
        :param new_username :
        """
        self.session = session
        password = quote(self.session.password)
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost')
        with engine.connect() as connection:
            connection.execute(text(f"UPDATE mysql.user SET User='{new_username}' WHERE User='{old_username}'"))
            connection.execute(text(f"UPDATE mysql.tables_priv SET User='{new_username}' WHERE User='{old_username}'"))
            connection.execute(text("FLUSH PRIVILEGES"))
            connection.commit()

    def delete_a_mysql_user_controller(self, session, username):
        """
        Fonction qui permet de supprimer un utilisateur de la base mysql.

        :param session
        :param username
        """
        self.session = session
        password = quote(self.session.password)
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost')
        with engine.connect() as connection:
            connection.execute(text(f"DROP USER '{username}'@'localhost'"))
            connection.execute(text("FLUSH PRIVILEGES"))
            connection.commit()

    def create_mysql_auth_user(self, session):
        """
        Fonction qui permet de créer un utilisateur mysql avec une limite de droit pour consulter la table colaborator.
        :param session:
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        info_key = self.json_c.get_info_key_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost')
        with engine.connect() as connection:
            connection.execute(text(f"CREATE USER 'auth_user'@'localhost' IDENTIFIED BY '{info_key}'"))
            connection.execute(text(f"GRANT SELECT ON {database_name}.collaborator "
                                    "TO auth_user@localhost"))
            connection.execute(text("FLUSH PRIVILEGES"))
