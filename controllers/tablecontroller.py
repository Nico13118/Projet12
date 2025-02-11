from models.tablemodel import Base, Collaborator, Customer, Role, ContractStatus, Contract, Event
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
        self.add_roles_in_the_table(session, database_name)
        self.add_contract_status_in_the_table(session, database_name)

    def save_customer_in_table_controller(self, session, info_name, info_first_name, info_email, info_phone,
                                          info_company_name):
        self.session = session
        database_name = self.json_c.get_database_name_in_json_file()
        password = quote(self.session.password)
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with Session(engine) as session:
            customer = Customer(
                custom_name=info_name,
                custom_first_name=info_first_name,
                custom_email=info_email,
                custom_phone=info_phone,
                custom_company_name=info_company_name,
                collaborator_id=self.session.collab_id
            )
            session.add(customer)
            session.commit()

    def save_customer_contract_in_table_controller(self, session, contract_description, contract_total_price,
                                                   contract_amount_remaining, custom_id, collaborator_id):
        self.session = session
        database_name = self.json_c.get_database_name_in_json_file()
        password = quote(self.session.password)
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with Session(engine) as session:
            contract = Contract(
                contract_description=contract_description,
                contract_total_price=contract_total_price,
                contract_amount_remaining=contract_amount_remaining,
                customer_id=custom_id,
                collaborator_id=collaborator_id
            )
            session.add(contract)
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
                collab_name=info_name,
                collab_first_name=info_first_name,
                collab_email=info_email,
                collab_username=info_username,
                collab_password=info_password,
                role_id=role
            )
            session.add(collaborator)
            session.commit()

    def save_new_event_contract_controller(self, session, event_date_start, event_date_end, location, attendees,
                                           notes, customer_id, contract_id):
        self.session = session
        database_name = self.json_c.get_database_name_in_json_file()
        password = quote(self.session.password)
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with Session(engine) as session:
            event = Event(
                event_date_start=event_date_start,
                event_date_end=event_date_end,
                location=location,
                attendees=attendees,
                notes=notes,
                customer_id=customer_id,
                contract_id=contract_id
            )
            session.add(event)
            session.commit()

    def add_contract_status_in_the_table(self, session, database_name):
        self.session = session
        password = quote(self.session.password)
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with Session(engine) as session:
            status_ok = ContractStatus(
                contract_status_name="Contrat signé"
            )
            status_nok = ContractStatus(
                contract_status_name="Contrat non signé"
            )
            session.add_all([status_ok, status_nok])
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
            result = connection.execute(text(
                f"SELECT * FROM collaborator WHERE collab_username = '{self.session.username}'"))
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

    def get_single_customer_info_with_id_controller(self, customer_id, session):
        """
        Fonction qui permet de récupérer les informations d'un client avec son ID.

        :param customer_id :
        :param session
        :return: result_customer
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_customer = connection.execute(text(f"SELECT * from customer JOIN collaborator "
                                                      f"ON customer.collaborator_id = collaborator.collab_id"
                                                      f" WHERE custom_id = {customer_id}"))
            return result_customer

    def edit_a_field_in_table(self, session, table_name, field, new_value, object_id, info_id):
        """
        Fonction qui permet de mettre à jour un champ de n'importe qu'elle table.
        Exemple :
        UPDATE {table_name} SET {field}       = '{new_value}' WHERE {object_id} = {info_id}"
        UPDATE {customer}   SET {custom_name} = '{Angel}'     WHERE {custom_id} = {1}"

        :param session : Correspond à l'utilisateur connecté
        :param info_id : L'id du client ou du collaborateur qui reçoit les modifications
        :param new_value : Nouvelle valeur à mettre à jour dans la table
        :param table_name : Nom de la table à modifier
        :param object_id : Correspond à l'id d'un objet (collab_id, custom_id ...)
        :param field: Correspond au champ qui va être modifié.
        :return: True
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            connection.execute(text(f"UPDATE {table_name} SET {field} = '{new_value}' WHERE {object_id} = {info_id}"))
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
                f"SELECT * FROM customer JOIN collaborator ON customer.collaborator_id = collaborator.collab_id"))
            return result_customer

    def delete_collaborator_in_table_controller(self, session, user_id):
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            connection.execute(text(f"DELETE FROM collaborator WHERE collab_id = {user_id}"))
            connection.commit()

    def get_list_customers_without_commercial_controller(self, session):
        """
        Fonction qui permet de retourner une liste de clients sans commercial assigné.

        :param session:
        :return: result_customer
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_customer = connection.execute(text(f"SELECT * FROM customer WHERE collaborator_id IS NULL"))
            return result_customer

    def get_list_commercial_controller(self, session):
        """
        Fonction qui permet de retourner la liste de tous les commerciaux.

        :param session:
        :return: result_commercial
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_commercial = connection.execute(text(f"SELECT * FROM collaborator WHERE role_id = 1"))
            return result_commercial

    def get_all_contract_controller(self, session):
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_contract = connection.execute(text(
                f"SELECT * FROM contract "
                f"JOIN contractstatus ON contract.contract_status_id = contractstatus.contract_status_id "
                f"JOIN customer ON customer.custom_id = contract.customer_id"))
            return result_contract

    def get_single_contract_controller(self, session, contract_id):
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_contract = connection.execute(text(
                f"SELECT * From contract "
                f"JOIN contractstatus ON contract.contract_status_id = contractstatus.contract_status_id "
                f"JOIN customer ON customer.custom_id = contract.customer_id "
                f"JOIN collaborator ON collaborator.collab_id = contract.collaborator_id "
                f"WHERE contract_id = {contract_id}"))
            return result_contract

    def get_a_customer_contracts_controller(self, session, customer_id):
        """
        Fonction qui permet de retourner un ou plusieurs contrats d'un client.

        :param session:
        :param customer_id:
        :return: result_contract
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_contract = connection.execute(text(
                f"SELECT * From contract "
                f"WHERE contract.customer_id = {customer_id}"))
            return result_contract

    def get_single_event_controller(self, session, contract_id):
        """
        Fonction qui permet de retourner un événement avec l'aide de l'id d'un contrat.
         
        :param session
        :param contract_id
        :return result_event
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_event = connection.execute(text(f"SELECT * From event WHERE contract_id = {contract_id}"))
            return result_event

    def get_all_event_controller(self, session):
        """
        Fonction qui permet de récupérer et de retourner une liste d'événements associés à chaques clients.
        :param session:
        :return: result_event
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_event = connection.execute(text(
                "SELECT * FROM event"
                " JOIN customer ON customer.custom_id = event.customer_id"))
            return result_event

    def get_event_list_by_user_controller(self, session):
        """
        Fonction qui permet de récupérer et de retourner une liste d'événement de l'utilisateur connecté.
        :param session:
        :return: result_event
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_event = connection.execute(text(
                "SELECT * FROM event"
                " JOIN customer ON customer.custom_id = event.customer_id"
                " JOIN collaborator ON collaborator.collab_id = event.collaborator_supp_id"
                f" WHERE collaborator_supp_id = {self.session.collab_id}"))
            return result_event

    def get_single_event_with_event_id_controller(self, session, info_event_id):
        """
        Fonction qui permet de récupérer un événement avec l'aide de son identifiant.
        :param session:
        :param info_event_id:
        :return: result_event1
        """
        self.session = session
        password = quote(self.session.password)
        database_name = self.json_c.get_database_name_in_json_file()
        engine = create_engine(f'mysql+pymysql://{self.session.username}:{password}@localhost/{database_name}')
        with engine.connect() as connection:
            result_event1 = connection.execute(text(
                "SELECT * FROM event "
                "JOIN customer ON customer.custom_id = event.customer_id "
                "JOIN collaborator ON collaborator.collab_id = event.collaborator_supp_id "
                f"WHERE event_id = {info_event_id}"))
            return result_event1
