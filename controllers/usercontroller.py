from sqlalchemy import create_engine
from urllib.parse import quote
import re

ROLE = ["COM", "GES", "SUP"]


class UserController:
    def __init__(self, userview, tablecontroller, databasecontroller, checkuserinputcontroller):
        self.user_v = userview
        self.table_c = tablecontroller
        self.database_c = databasecontroller
        self.check_user_input_c = checkuserinputcontroller

    def start_create_user_controller(self, username_admin, password_admin):
        info_name = self.get_name_controller()
        info_first_name = self.get_first_name_controller()
        name_first_name = f"{info_name} {info_first_name}"
        info_email = self.get_email_controller()
        info_username = self.get_username_controller(name_first_name)
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
        :return: role_id
        """
        role_id = ""
        if info_role == "COM":
            role_id = 1
        elif info_role == "GES":
            role_id = 2
        elif info_role == "SUP":
            role_id = 3
        return role_id

    def get_name_controller(self):
        """
        Fonction qui permet de contrôler la saisie utilisateur concernant le champ name.

        :return: name
        """
        while True:
            name = self.user_v.get_name_view()  # Récupère la saisie de l'utilisateur
            if name:  # Vérifie que la saisie n'est pas vide
                # Vérifie que la saisie contient que des lettres
                if self.check_user_input_c.search_is_alpha_controller(name):
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
                # Vérifie que la saisie contient que des lettres
                if self.check_user_input_c.search_is_alpha_controller(first_name):
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

    def get_username_controller(self, name_first_name):
        """
        Fonction qui permet de créer un username.
        Name et first_name sont modifiés en minuscule en ajoutant un undescore si présence d'un espace dans le nom
        et prénom.

        :return: user_name
        """
        name_first_name_lower = name_first_name.lower()
        username = re.sub(r"\s", "_", name_first_name_lower)
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
