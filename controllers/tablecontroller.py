from models.tablemodel import Base, Collaborator, Customer, Role
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
from urllib.parse import quote


class TableController:
    def __init__(self, jsoncontroller):
        self.json_c = jsoncontroller
        self.session = None

    def create_table_all_controller(self, session, database_name):
        """
        Fonction qui permet de créer toutes les tables.

        :param session
        :param database_name
        """
        self.session = session
        pass_admin = quote(self.session.password)
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{pass_admin}@localhost/{database_name}')
        Base.metadata.create_all(bind=engine, tables=None, checkfirst=False)
        self.add_roles_in_the_table(self.session, database_name)

    def save_customer_in_table_controller(self, session, info_name, info_first_name, info_email, info_company_name):
        self.session = session
        database_name = self.json_c.get_database_name_in_json_file()
        password = quote(self.session.password)
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with Session(engine) as session:
            customer = Customer(
                name=info_name,
                first_name=info_first_name,
                email=info_email,
                company_name=info_company_name,
                collaborator_id=self.session.collab_id
            )
            session.add(customer)
            session.commit()

    def save_collaborator_in_table_controller(self, session, info_name, info_first_name,
                                              info_email, info_username, info_password, role):
        """
        Fonction qui permet d'enregistrer un collaborateur dans la table.

        :param session
        :param info_name:
        :param info_first_name:
        :param info_email:
        :param info_username:
        :param info_password:
        :param role:
        """
        self.session = session
        database_name = self.json_c.get_database_name_in_json_file()  # Récupère le nom de la base de données
        password = quote(self.session.password)
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
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

    def add_roles_in_the_table(self, session, database_name):
        """
        Fonction qui permet d'enregistrer les rôles dans la table.

        :param session
        :param database_name :
        """
        self.session = session
        password = quote(self.session.password)
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
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

    def get_information_for_single_collaborator_controller(self, session):
        """
        Fonction qui permet de retourner les informations d'un seul collaborateur.
        Recherche avec username.

        :param session
        :return: result
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result = connection.execute(text(f"SELECT * FROM collaborator WHERE username = '{self.session.username}'"))
            return result

    def get_information_for_all_collaborators_controller(self, session):
        """
        Fonction qui permet de retourner la liste complète des collaborateurs.

        :param session
        :return: result
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result = connection.execute(text(
                f"SELECT * FROM collaborator JOIN role ON collaborator.role_id = role.id"))
            return result

    def get_single_collaborator_info_with_id_controller(self, user_id, session):
        """
        Fonction qui permet de récupérer les informations d'un utilisateur avec son ID.

        :param user_id :
        :param session
        :return: result_user
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_user = connection.execute(text(f"SELECT * FROM collaborator JOIN role ON collaborator.role_id = "
                                                  f"role.id WHERE collaborator.collab_id = '{user_id}'"))
            return result_user

    def edit_collaborator_fields_controller(self, user_id, new_value, session, field):
        """
        Fonction qui permet de mettre à jour un champ concernant un collaborateur.

        :param user_id :
        :param new_value :
        :param session
        :param field:
        :return: True
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            connection.execute(text(f"UPDATE collaborator SET {field} = '{new_value}' WHERE collab_id = {user_id}"))
            connection.commit()
            return True

    def get_list_of_all_customers_controller(self, session):
        """
        Fonction qui permet de retourner la liste des clients.
        
        :param session
        :return: result_customer
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_customer = connection.execute(text(
                f"SELECT * FROM customer JOIN collaborator ON customer.id = collaborator.collab_id"))
            return result_customer
