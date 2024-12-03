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
        role = ""
        if info_role == "COM":
            role = 1
        elif info_role == "GES":
            role = 2
        elif info_role == "SUP":
            role = 3
        return role

    def search_is_alpha_controller(self, user_input1):
        user_input2 = re.sub(r"\s", "", user_input1)
        x = user_input2.isalpha()
        return x

    def get_name_controller(self):
        while True:
            user_input = self.user_v.get_name_view()  # Récupère la saisie de l'utilisateur
            if user_input:  # Vérifie que la saisie n'est pas vide
                if self.search_is_alpha_controller(user_input):  # Vérifie que la saisie contient que des lettres
                    break
                else:
                    self.user_v.error_message_field_contains_number()
            else:
                self.user_v.error_message_empty_field_view()
        return user_input

    def get_first_name_controller(self):
        while True:
            user_input = self.user_v.get_first_name_view()  # Récupère la saisie de l'utilisateur
            if user_input:  # Vérifie que la saisie n'est pas vide
                if self.search_is_alpha_controller(user_input):  # Vérifie que la saisie contient que des lettres
                    break
            else:
                self.user_v.display_message_error_field_view()
        return user_input

    def get_email_controller(self):
        while True:
            user_input = self.user_v.get_email_view()  # Récupère la saisie de l'utilisateur
            if user_input:  # Vérifie que la saisie n'est pas vide
                break
            else:
                self.user_v.display_message_error_field_view()
        return user_input

    def get_username_controller(self, name, first_name):
        lower_name = name.lower()
        lower_first_name = first_name.lower()
        username = f"{lower_name}_{lower_first_name}"
        return username

    def get_password_controller(self):
        while True:
            user_input = self.user_v.get_password_view()  # Récupère la saisie de l'utilisateur
            if user_input:
                break
            else:
                self.user_v.display_message_error_field_view()
        return user_input

    def get_role_controller(self):
        while True:
            user_input = self.user_v.get_role_view()  # Récupère la saisie de l'utilisateur
            if user_input:
                user_input = user_input.upper()
                if user_input in ROLE:
                    break
                else:
                    self.user_v.display_message_error_choices_view()
            else:
                self.user_v.display_message_error_field_view()
        return user_input
