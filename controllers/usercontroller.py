import re


class UserController:
    def __init__(self, userview, errormessagesview, menuview, tablecontroller, databasecontroller, checkuserinputcontroller):
        self.user_v = userview
        self.error_messages_v = errormessagesview
        self.menu_view = menuview
        self.table_c = tablecontroller
        self.database_c = databasecontroller
        self.check_user_input_c = checkuserinputcontroller
        self.session = None

    def start_create_user_controller(self, session, first_connexion=None):
        info_name = self.get_name_controller()
        info_first_name = self.get_first_name_controller()
        info_email = self.get_email_controller()
        info_username = self.get_username_controller(f"{info_name} {info_first_name}")
        info_password = self.get_password_controller()
        if first_connexion:
            role_id = 2
        else:
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

    def get_number_phone_controller(self):
        """
        Fonction qui permet de contrôler la saisie utilisateur concernant le champ phone.

        :return: email
        """
        while True:
            phone = self.user_v.get_number_phone_view()  # Récupère la saisie de l'utilisateur
            if phone:  # Vérifie que la saisie n'est pas vide
                break
            else:
                self.error_messages_v.error_message_empty_field_view()
        return phone

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

    def show_customer_list_controller(self, session):
        """
        Fonction qui permet de récupérer la liste des clients puis transmet les informations à la vue
        pour être affichées.

        :param session:
        """
        list_customers = []
        self.menu_view.clear_terminal_view()
        result_list_customer = self.table_c.get_list_of_all_customers_controller(session)
        for r in result_list_customer:
            list_customers.append(r)
        if len(list_customers) >= 1:
            self.user_v.display_list_customer_view(list_customers)
        return len(list_customers)
        
    def ask_user_if_they_want_to_edit_contract(self):
        while True:
            user_input_y_n = self.user_v.display_message_edit_customer_contract_view()
            if user_input_y_n:
                response = self.check_user_input_c.check_user_input_yes_no_controller(user_input_y_n)
                if response == "Y":
                    return True
                elif response == "N":
                    break
                elif response != "Y" or response != "N":
                    self.error_messages_v.display_error_message_of_values_yes_and_no()
            else:
                self.error_messages_v.error_message_empty_field_view()

    def ask_user_to_select_customer_contract_controller(self, session):
        while True:
            user_input_contract_id = self.user_v.get_contract_id_view()
            if user_input_contract_id:
                result_contract = self.table_c.get_single_contract_controller(session, user_input_contract_id)
                list_result_contract = [c for c in result_contract]
                if list_result_contract:
                    break
                else:
                    self.error_messages_v.display_error_message_choice_view()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return user_input_contract_id

    def edit_info_customer_contract_controller(self, session, contract_id):
        error = False
        while True:
            self.menu_view.clear_terminal_view()
            result_contract = self.table_c.get_single_contract_controller(session, contract_id)  # Récupère le contrat
            self.menu_view.display_edit_menu_of_a_customer_contract_view(result_contract)  # Affiche le menu

            if error:
                self.error_messages_v.display_error_message_choice_view()
                error = False

            result_choice = self.user_v.get_user_input_view()  # Demande à l'utilisateur de faire un choix

            if result_choice == '1':  # Modifier la description du contrat
                description = self.get_contract_description_controller()
                self.table_c.edit_a_field_in_table(session, table_name='contract', field="contract_description",
                                                   new_value=description, object_id="contract_id", info_id=contract_id)

            elif result_choice == '2':  # Modifier le prix du contrat
                total_price = self.get_contract_total_price_controller()
                self.table_c.edit_a_field_in_table(session, table_name='contract', field="contract_total_price",
                                                   new_value=total_price, object_id="contract_id", info_id=contract_id)

            elif result_choice == '3':  # Modifier le solde restant
                amount_remaining = self.get_contract_amount_remaining_controller()
                self.table_c.edit_a_field_in_table(session, table_name='contract', field="contract_amount_remaining",
                                                   new_value=amount_remaining, object_id="contract_id",
                                                   info_id=contract_id)

            elif result_choice == '4':  # Modifier le statut du contrat
                self.change_status_of_contract_controller(session, contract_id)

            elif result_choice == '5':
                break

            else:
                error = True

    def get_contract_description_controller(self):
        while True:
            user_input = self.user_v.get_contract_description_view()
            if user_input:
                break
            else:
                self.error_messages_v.error_message_empty_field_view()
        return user_input

    def get_contract_total_price_controller(self):
        while True:
            user_input = self.user_v.get_contract_total_price_view()
            result = self.check_user_input_c.check_user_input_isdigit(user_input)
            if result:
                break
            else:
                self.error_messages_v.display_message_error_numerical_value_view()
        return user_input

    def get_contract_amount_remaining_controller(self):
        while True:
            user_input = self.user_v.get_contract_amount_remaining_view()
            result = self.check_user_input_c.check_user_input_isdigit(user_input)
            if result:
                break
            else:
                self.error_messages_v.display_message_error_numerical_value_view()
        return user_input

    def change_status_of_contract_controller(self, session, contract_id):
        result_contract = self.table_c.get_single_contract_controller(session, contract_id)
        infos_contract = result_contract.fetchone()
        while True:
            if infos_contract.contract_status_id == 1:
                result_y_n = self.user_v.display_message_of_an_unsigned_contract_view()
                if result_y_n:
                    check_result_y_n = self.check_user_input_c.check_user_input_yes_no_controller(result_y_n)
                    if check_result_y_n == "Y":
                        self.table_c.edit_a_field_in_table(session, table_name='contract', field='contract_status_id',
                                                           new_value=2, object_id='contract_id',
                                                           info_id=infos_contract.contract_id)
                        break
                    else:
                        break
                else:
                    self.error_messages_v.error_message_empty_field_view()

            elif infos_contract.contract_status_id == 2:
                result_y_n = self.user_v.display_message_of_a_signed_contract_view()
                if result_y_n:
                    check_result_y_n = self.check_user_input_c.check_user_input_yes_no_controller(result_y_n)
                    if check_result_y_n == "Y":
                        self.table_c.edit_a_field_in_table(session, table_name='contract', field="contract_status_id",
                                                           new_value=1, object_id="contract_id",
                                                           info_id=infos_contract.contract_id)
                        break
                    else:
                        break
                else:
                    self.error_messages_v.error_message_empty_field_view()

    def get_start_date_event_controller(self):
        """
        Fonction qui permet de récupérer la date et de contrôler que la saisie ne soit pas vide ou ne dépasse pas
        la limite imposée.

        :return response_start_date
        """
        while True:
            response_start_date = self.user_v.get_start_date_view()
            if response_start_date:
                if len(response_start_date) <= 30:
                    break
                else:
                    self.error_messages_v.error_date()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return response_start_date

    def get_end_date_event_controller(self):
        """
        Fonction qui permet de récupérer la date et de contrôler que la saisie ne soit pas vide ou ne dépasse pas
        la limite imposée.

        :return response_end_date
        """
        while True:
            response_end_date = self.user_v.get_end_date_view()
            if response_end_date:
                if len(response_end_date) <= 30:
                    break
                else:
                    self.error_messages_v.error_date()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return response_end_date

    def get_location_event_controller(self):
        """
        Fonction qui permet de récupérer et de contrôler la saisie de l'adresse.
         
        :return: response_location
        """
        while True:
            response_location = self.user_v.get_location_view()
            if response_location:
                if len(response_location) <= 200:
                    break
                else:
                    self.error_messages_v.exceeded_number_of_characters()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return response_location

    def get_attendees_event_controller(self):
        """
        Fonction qui permet de récupérer et de contrôler la valeur saisie par l'utilisateur permettant de connaitre
        le nombre personnes invitées à l'événement.

        :return response_attendees
        """
        while True:
            response_attendees = self.user_v.get_attendees_view()
            if response_attendees:
                result = self.check_user_input_c.check_user_input_isdigit(response_attendees)
                if result:
                    if len(response_attendees) <= 7:
                        break
                    else:
                        self.error_messages_v.exceeded_number_of_characters()
                else:
                    self.error_messages_v.display_message_error_numerical_value_view()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return response_attendees

    def get_notes_event_controller(self):
        """
        Fonction qui permet de récupérer et contrôler la note d'événement saisie par l'utilisateur
        :return response_notes
        """
        while True:
            response_notes = self.user_v.get_notes_event_view()
            if response_notes:
                if len(response_notes) <= 500:
                    break
                else:
                    self.error_messages_v.exceeded_number_of_characters()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return response_notes

    def get_all_event_controller(self, session):
        """
        Fonction qui permet de récupérer, contrôler et retourner tous les événements
        :param session:
        :return: list_events
        """
        result_event = self.table_c.get_all_event_controller(session)
        list_events = [c for c in result_event]
        if len(list_events) >= 1:
            return list_events

    def get_support_collaborator_controller(self, session):
        """
        Fonction qui permet de récupérer la liste de tous collaborateurs puis de retourner une liste de
        collaborateur du support.
        :param session:
        :return: list_collab_supp
        """
        info_collab = self.table_c.get_information_for_all_collaborators_controller(session)
        list_collab_supp = [c for c in info_collab if c.role_id == 3]
        return list_collab_supp

    def get_all_contract_controller(self, session):
        """
        Fonction qui permet de récupérer, contrôler et retourner une liste de contrat.

        :param session:
        :return: list_contract
        """
        result_contract = self.table_c.get_all_contract_controller(session)
        list_contract = [c for c in result_contract]
        if list_contract:
            return list_contract
