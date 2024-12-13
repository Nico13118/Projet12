import re


class UserController:
    def __init__(self, userview, errormessagesview, tablecontroller, databasecontroller, checkuserinputcontroller):
        self.user_v = userview
        self.error_messages_v = errormessagesview
        self.table_c = tablecontroller
        self.database_c = databasecontroller
        self.check_user_input_c = checkuserinputcontroller
        self.session = None

    def start_create_user_controller(self, session):
        info_name = self.get_name_controller()
        info_first_name = self.get_first_name_controller()
        info_email = self.get_email_controller()
        info_username = self.get_username_controller(f"{info_name} {info_first_name}")
        info_password = self.get_password_controller()
        info_role = self.get_role_controller()

        role_id = self.get_role_id_controller(info_role)  # Récupération de role_id

        self.table_c.save_collaborator_in_table_controller(session, info_name, info_first_name,
                                                           info_email, info_username, info_password, role_id)
        if role_id == 1:
            self.database_c.save_collaborator_com_in_mysql_controller(session, info_username, info_password)
        if role_id == 2:
            self.database_c.save_collaborator_ges_in_mysql_controller(session, info_username, info_password)
        if role_id == 3:
            self.database_c.save_collaborator_sup_in_mysql_controller(session, info_username, info_password)

    def start_create_customer_controller(self, session):
        info_name = self.get_name_controller()
        info_first_name = self.get_first_name_controller()
        info_email = self.get_email_controller()
        company_name = self.get_company_name_controller()
        self.table_c.save_customer_in_table_controllersave_customer_in_table_controller(
            session, info_name, info_first_name, info_email, company_name)

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
                    self.error_messages_v.error_message_field_contains_number()
            else:
                self.error_messages_v.error_message_empty_field_view()
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
                self.error_messages_v.error_message_empty_field_view()
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
                self.error_messages_v.error_message_empty_field_view()
        return email

    def get_company_name_controller(self):
        """
        Fonction qui permet de récupérer le nom de l'entreprise et vérifie que la saisie n'est pas vide.

        :return company_name
        """
        while True:
            company_name = self.user_v.get_company_name_view()
            if company_name:
                break
            else:
                self.error_messages_v.error_message_empty_field_view()
        return company_name

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
                self.error_messages_v.error_message_empty_field_view()
        return password

    def get_role_controller(self):
        """
        Fonction qui permet de récupérer la saisie utilisateur concernant le champ role.
        La saisie est ensuite envoyée pour y être contrôlée.

        :return: info_role
        """
        while True:
            role = self.user_v.get_role_view()  # Récupère la saisie de l'utilisateur
            if role:
                info_role = self.check_user_input_c.check_user_input_role_controller(role)
                if info_role:
                    break
                else:
                    self.error_messages_v.error_message_choices_com_ges_sup_view()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return info_role
