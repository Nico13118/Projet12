import re


class UserController:
    def __init__(self, userview, errormessagesview, menuview, tablecontroller, databasecontroller,
                 checkuserinputcontroller):
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

    def control_name_and_first_name(self, message_function, max_length):
        """
        Fonction qui permet de récupérer la saisie utilisateur (nom prénom) et vérifie quelle ne soit pas vide, qu'elle
        contienne que des lettres et qu'elle ne dépasse pas longueur autorisée.
        :param message_function:
        :param max_length:
        :return: user_input
        """
        while True:
            user_input = message_function()
            if user_input:
                if self.check_user_input_c.search_is_alpha_controller(user_input):
                    if self.check_user_input_c.check_input_length(user_input, max_length):
                        break
                    else:
                        self.error_messages_v.display_error_message_input_too_long(max_length)
                else:
                    self.error_messages_v.error_message_field_contains_number()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return user_input

    def get_name_controller(self):
        return self.control_name_and_first_name(self.user_v.get_name_view, max_length=40)

    def get_first_name_controller(self):
        return self.control_name_and_first_name(self.user_v.get_first_name_view, max_length=40)

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

    def ask_user_confirmation(self, message_function):
        """
        Fonction qui permet de demander à l'utilisateur confirmation selon l'action qui s'affiche à l'écran.
        :param message_function:
        :return: bool
        """
        while True:
            user_input_y_n = message_function()
            if user_input_y_n:
                response = self.check_user_input_c.check_user_input_yes_no_controller(user_input_y_n)
                if response == "Y":
                    return True
                elif response == "N":
                    break
                else:
                    self.error_messages_v.display_error_message_of_values_yes_and_no()
            else:
                self.error_messages_v.error_message_empty_field_view()

    def ask_user_if_they_want_to_edit_contract(self):
        return self.ask_user_confirmation(self.user_v.display_message_edit_customer_contract_view)

    def ask_user_if_they_want_to_edit_event(self):
        return self.ask_user_confirmation(self.user_v.display_message_edit_event_view)

    def ask_user_if_they_want_assign_reassign_event_to_a_collaborator_controller(self):
        return self.ask_user_confirmation(self.user_v.display_message_to_assign_reassign_event_to_a_collaborator_view)

    def ask_user_if_they_want_assign_event_to_a_collaborator_controller(self):
        return self.ask_user_confirmation(self.user_v.display_message_to_assign_event_to_a_collaborator_view)

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

    def check_that_the_numeric_value_is_valid_controller(self, message_fonction):
        """
        Fonction qui permet de contrôler que la saisie utilisateur soit bien une valeur numérique.
        :param message_fonction:
        :return: user_input
        """
        while True:
            user_input = message_fonction()
            if user_input:
                result = self.check_user_input_c.check_user_input_isdigit(user_input)
                if result:
                    break
                else:
                    self.error_messages_v.display_message_error_numerical_value_view()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return user_input

    def get_contract_total_price_controller(self):
        return self.check_that_the_numeric_value_is_valid_controller(self.user_v.get_contract_total_price_view)

    def get_contract_amount_remaining_controller(self):
        return self.check_that_the_numeric_value_is_valid_controller(self.user_v.get_contract_amount_remaining_view)

    def get_attendees_event_controller(self):
        return self.check_that_the_numeric_value_is_valid_controller(self.user_v.get_attendees_view)

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

    def edit_info_event_contract_controller(self, session, user_input_event_id):
        """
        Fonction qui permet de gérer un sous menu permettant l'affichage et la modification d'informations concernant
        un événement.

        :param session:
        :param user_input_event_id:
        :return:
        """
        error = False
        while True:
            self.menu_view.clear_terminal_view()
            result_event = self.table_c.get_single_event_with_event_id_controller(session, user_input_event_id)
            self.menu_view.display_edit_menu_of_a_event_view(result_event)  # Affiche le menu

            if error:
                self.error_messages_v.display_error_message_choice_view()
                error = False

            result_choice = self.user_v.get_user_input_view()  # Demande à l'utilisateur de faire un choix

            if result_choice == '1':  # Modifier la date et l'heure de début
                new_value_event_date_start = self.get_start_date_event_controller()
                self.table_c.edit_a_field_in_table(session, table_name='event', field="event_date_start",
                                                   new_value=new_value_event_date_start, object_id="event_id",
                                                   info_id=user_input_event_id)

            elif result_choice == '2':  # Modifier la date et l'heure de fin
                new_value_event_date_end = self.get_end_date_event_controller()
                self.table_c.edit_a_field_in_table(session, table_name='event', field="event_date_end",
                                                   new_value=new_value_event_date_end, object_id="event_id",
                                                   info_id=user_input_event_id)

            elif result_choice == '3':  # Modifier l'adresse de l'événement
                new_value_location = self.get_location_event_controller()
                self.table_c.edit_a_field_in_table(session, table_name='event', field="location",
                                                   new_value=new_value_location, object_id="event_id",
                                                   info_id=user_input_event_id)

            elif result_choice == '4':  # Modifier le nombre d'invités
                new_value_attendees = self.get_attendees_event_controller()
                self.table_c.edit_a_field_in_table(session, table_name='event', field="attendees",
                                                   new_value=new_value_attendees, object_id="event_id",
                                                   info_id=user_input_event_id)

            elif result_choice == '5':  # Modifier la note d'information
                new_value_notes = self.get_notes_event_controller()
                self.table_c.edit_a_field_in_table(session, table_name='event', field="notes",
                                                   new_value=new_value_notes, object_id="event_id",
                                                   info_id=user_input_event_id)

            elif result_choice == '6':  # Quitter
                break

            else:
                error = True

    def get_and_validate_input_length(self, message_fonction, max_length):
        """
        Fonction qui permet de récupérer la saisie utilisateur et contrôle qu'elle ne soit pas vide ou ne dépasse pas
        la limite imposée.
        :param message_fonction:
        :param max_length:
        :return: user_input
        """
        while True:
            user_input = message_fonction()
            if user_input:
                if self.check_user_input_c.check_input_length(user_input, max_length):
                    break
                else:
                    self.error_messages_v.display_error_message_input_too_long(max_length)
            else:
                self.error_messages_v.error_message_empty_field_view()
        return user_input

    def get_start_date_event_controller(self):
        return self.get_and_validate_input_length(self.user_v.get_start_date_view, max_length=30)

    def get_end_date_event_controller(self):
        return self.get_and_validate_input_length(self.user_v.get_end_date_view, max_length=30)

    def get_location_event_controller(self):
        return self.get_and_validate_input_length(self.user_v.get_location_view, max_length=200)

    def get_notes_event_controller(self):
        return self.get_and_validate_input_length(self.user_v.get_notes_event_view, max_length=500)

    def fetch_and_check_table_data(self, search_table, session):
        """
        Fonction qui permet de récupérer des données selon la table choisie et vérifie si elles contiennent au moins une
        valeur avant de les retourner.
        :param search_table:
        :param session:
        :return: result_list si des données sont trouvées, sinon None.
        """
        result = search_table(session)
        result_list = [c for c in result]
        if len(result_list) >= 1:
            return result_list

    def get_all_event_controller(self, session):
        return self.fetch_and_check_table_data(self.table_c.get_all_event_controller, session)

    def get_event_without_support_controller(self, session):
        return self.fetch_and_check_table_data(self.table_c.get_list_event_without_support_controller, session)

    def get_all_contract_controller(self, session):
        return self.fetch_and_check_table_data(self.table_c.get_all_contract_controller, session)

    def get_list_all_customer_controller(self, session):
        return self.fetch_and_check_table_data(self.table_c.get_list_of_all_customers_controller, session)

    def get_user_event_list_support_controller(self, session):
        return self.fetch_and_check_table_data(self.table_c.get_event_list_by_user_controller, session)

    def get_collaborator_list_controller(self, session):
        return self.fetch_and_check_table_data(self.table_c.get_information_for_all_collaborators_controller, session)

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

    def get_and_validate_entity_id(self, message_fonction, entity_list):
        """
        Fonction qui permet de récupérer l'id (event, contrat ...) saisi par l'utilisateur puis contrôle qu'il
        correspond dans la liste.

        :param message_fonction:
        :param entity_list:
        :return: user_input_id
        """
        while True:
            user_input_id = message_fonction()
            if user_input_id:
                result = [c for c in entity_list if c[0] == int(user_input_id)]
                if result:
                    break
                else:
                    self.error_messages_v.display_error_message_choice_view()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return user_input_id

    def ask_user_to_select_event_id_controller(self, result_event):
        return self.get_and_validate_entity_id(self.user_v.get_event_id_view, result_event)

    def ask_user_to_select_customer_contract_controller(self, result_contract):
        return self.get_and_validate_entity_id(self.user_v.get_contract_id_view, result_contract)

