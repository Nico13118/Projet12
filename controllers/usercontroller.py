from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from urllib.parse import quote
import re

ROLE = ["COM", "GES", "SUP"]


class UserController:
    def __init__(self, userview, tablecontroller, databasecontroller):
        self.user_v = userview
        self.table_c = tablecontroller
        self.database_c = databasecontroller

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

    def start_create_user_controller(self, username_admin, password_admin):
        info_name = self.get_name_controller()
        info_first_name = self.get_first_name_controller()
        info_email = self.get_email_controller()
        info_username = self.get_username_controller(info_name, info_first_name)
        info_password = self.get_password_controller()
        info_role = self.get_role_controller()

        role_id = self.get_role_id_controller(info_role)  # Récupération de role_id

        self.table_c.save_collaborator_in_table_controller(username_admin, password_admin,
                                                           info_name, info_first_name,
                                                           info_email, info_username,
                                                           info_password, role_id)
        if role_id == 1:
            self.database_c.save_collaborator_com_in_mysql_controller(username_admin, password_admin,
                                                                      info_username, info_password)
        if role_id == 2:
            self.database_c.save_collaborator_ges_in_mysql_controller(username_admin, password_admin,
                                                                      info_username, info_password)
        if role_id == 3:
            self.database_c.save_collaborator_sup_in_mysql_controller(username_admin, password_admin,
                                                                      info_username, info_password)

    def get_role_id_controller(self, info_role):
        """
        Fonction qui retourne le role_id selon le role reçu en paramètre.
        : param info_role:
        : return: role_id
        """
        role_id = ""
        if info_role == "COM":
            role_id = 1
        elif info_role == "GES":
            role_id = 2
        elif info_role == "SUP":
            role_id = 3
        return role_id

    def search_is_alpha_controller(self, user_input1):
        """
        Fonction qui permet de vérifier que la saisie ne contient que des lettres
        : param user_input1:
        :return: True / False
        """
        user_input2 = re.sub(r"\s", "", user_input1)
        x = user_input2.isalpha()
        return x

    def get_name_controller(self):
        """
        Fonction qui permet de contrôler la saisie utilisateur concernant le champ name.

        :return: name
        """
        while True:
            name = self.user_v.get_name_view()  # Récupère la saisie de l'utilisateur
            if name:  # Vérifie que la saisie n'est pas vide
                if self.search_is_alpha_controller(name):  # Vérifie que la saisie contient que des lettres
                    break
                else:
                    self.user_v.error_message_field_contains_number()
            else:
                self.user_v.error_message_empty_field_view()
        return name

    def get_first_name_controller(self):
        """
        Fonction qui permet de contrôler la saisie utilisateur concernant le champ first_name.

        :return: first_name
        """
        while True:
            first_name = self.user_v.get_first_name_view()  # Récupère la saisie de l'utilisateur
            if first_name:  # Vérifie que la saisie n'est pas vide
                if self.search_is_alpha_controller(first_name):  # Vérifie que la saisie contient que des lettres
                    break
            else:
                self.user_v.display_message_error_field_view()
        return first_name

    def get_email_controller(self):
        """
        Fonction qui permet de contrôler la saisie utilisateur concernant le champ email.

        :return: email
        """
        while True:
            email = self.user_v.get_email_view()  # Récupère la saisie de l'utilisateur
            if email:  # Vérifie que la saisie n'est pas vide
                break
            else:
                self.user_v.display_message_error_field_view()
        return email

    def get_username_controller(self, name, first_name):
        """
        Fonction qui permet de créer un username.
        Name et first_name sont modifiés en minuscule puis concaténé avec un undescore qui permet la séparation.

        :return: user_name
        """
        lower_name = name.lower()
        lower_first_name = first_name.lower()
        username = f"{lower_name}_{lower_first_name}"
        return username

    def get_password_controller(self):
        """
        Fonction qui permet de contrôler la saisie utilisateur concernant le champ password.

        :return: password
        """
        while True:
            password = self.user_v.get_password_view()  # Récupère la saisie de l'utilisateur
            if password:
                break
            else:
                self.user_v.display_message_error_field_view()
        return password

    def get_role_controller(self):
        """
        Fonction qui permet de contrôler la saisie utilisateur concernant le champ role.

        :return: role
        """
        while True:
            role = self.user_v.get_role_view()  # Récupère la saisie de l'utilisateur
            if role:
                role = role.upper()
                if role in ROLE:
                    break
                else:
                    self.user_v.display_message_error_choices_view()
            else:
                self.user_v.display_message_error_field_view()
        return role
