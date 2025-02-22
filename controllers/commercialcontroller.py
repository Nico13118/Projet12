class CommercialController:
    def __init__(self, menuview, userview, errormessagesview, usercontroller, tablecontroller,
                 checkuserinputcontroller):
        self.session = None
        self.menu_view = menuview
        self.user_view = userview
        self.user_c = usercontroller
        self.table_c = tablecontroller
        self.check_user_input_c = checkuserinputcontroller
        self.error_messages_v = errormessagesview

    def register_new_customer_controller(self, session):
        """
        Fonction qui permet d'enregistrer un nouveau client.

        :param session
        """
        self.menu_view.clear_terminal_view()
        self.user_view.display_message_create_new_customer()

        info_name = self.user_c.get_name_controller()
        info_first_name = self.user_c.get_first_name_controller()
        info_email = self.user_c.get_email_controller()
        info_phone = self.user_c.get_number_phone_controller()
        info_company_name = self.user_c.get_company_name_controller()

        self.table_c.save_customer_in_table_controller(session, info_name, info_first_name, info_email, info_phone,
                                                       info_company_name)

    def ask_user_if_wants_they_want_to_edit_customer(self):
        """
        Fonction qui permet de demander à l'utilisateur s'il souhaite apporter une modification à un utilisateur.
        La reponse de l'utilisateur est contrôlé.

        :return: Y
        """
        while True:
            user_input = self.user_view.display_message_edit_customer_list_view()
            response = self.check_user_input_c.check_user_input_yes_no_controller(user_input)
            if response == "Y":
                return True
            elif response == "N":
                break
            else:
                self.error_messages_v.display_error_message_of_values_yes_and_no()

    def ask_user_to_select_customer_controller(self, session):
        """
        Fonction qui permet de demander à l'utilisateur de saisir le N° client à modifier.
        Une recherche est effectuée dans la base avec l'id du client concerné.

        :param session
        """
        while True:
            customer_id = self.user_view.get_customer_code_id_view()
            result = self.check_user_input_c.check_user_input_isdigit(customer_id)
            if result:
                customer_list = self.table_c.get_single_customer_info_with_id_controller(customer_id, session)
                result_info = [c for c in customer_list if c.custom_id == int(customer_id)]
                if result_info:
                    return customer_id
                else:
                    self.error_messages_v.display_error_message_choice_view()
            else:
                self.error_messages_v.display_error_message_choice_view()

    def get_unsigned_contracts(self, result_contract):
        """
        Fonction qui permet de retourner uniquement les contrats non signés

        :param result_contract
        :return: list_contract
        """
        list_contract = []
        for row in result_contract:
            if row.contract_status_id == 2:
                list_contract.append(row)
        return list_contract

    def get_unpaid_contracts(self, result_contract):
        """
        Fonction qui permet de retourner uniquement les contrats non soldés.
        :param result_contract:
        :return: list_contract
        """
        list_contract = []
        for row in result_contract:
            if row.contract_amount_remaining != 0:
                list_contract.append(row)
        return list_contract

    def get_collaborator_customer_list(self, session):
        """
        Fonction qui permet de retourner la liste de client attribué à l'utilisateur connecté.
        :param session:
        :return:
        """
        customer_list = []
        result = self.table_c.get_list_of_all_customers_controller(session)
        for row in result:
            if session.collab_id == row.collaborator_id:
                customer_list.append(row)
        return customer_list

    def get_collaborator_contract_list(self, session):
        """
        Fonction qui permet de retourner une liste de contrats attribués à l'utilisateur connecté.
        :param session:
        :return:
        """
        result_contract = self.user_c.get_all_contract_controller(session)
        if result_contract:
            contract_collab_list = [c for c in result_contract if session.collab_id == c.collaborator_id]
            if contract_collab_list:
                return contract_collab_list

    def ask_user_if_wants_create_event_contract_controller(self):
        while True:
            user_input = self.user_view.display_message_create_contract_event_view()
            response = self.check_user_input_c.check_user_input_yes_no_controller(user_input)
            if response == "Y":
                return True
            elif response == "N":
                break
            else:
                self.error_messages_v.display_error_message_of_values_yes_and_no()

    def create_new_event_controller(self, session, result_contract_list3):
        while True:
            contract_id = self.user_view.get_contract_id_view()
            if contract_id:
                result = [c for c in result_contract_list3 if c.contract_id == int(contract_id)]
                if result:
                    event_date_start = self.user_c.get_start_date_event_controller()
                    event_date_end = self.user_c.get_end_date_event_controller()
                    location = self.user_c.get_location_event_controller()
                    attendees = self.user_c.get_attendees_event_controller()
                    notes = self.user_c.get_notes_event_controller()
                    customer_id = result[0].customer_id
                    self.table_c.save_new_event_contract_controller(session, event_date_start, event_date_end, location,
                                                                    attendees, notes, customer_id, contract_id)
                    break
                else:
                    self.error_messages_v.display_error_message_choice_view()
            else:
                self.error_messages_v.error_message_empty_field_view()
        self.user_view.display_end_message_event_view()

    def search_for_signed_and_paid_contracts(self, result_contract_list1):
        """
        Fonction qui retourne une liste de contrats signé et payé.

        :param result_contract_list1
        :return contract_list
        """
        contract_list = []
        for r_contract_list1 in result_contract_list1:
            if r_contract_list1.contract_status_id == 1:
                if r_contract_list1.contract_amount_remaining == 0:
                    contract_list.append(r_contract_list1)
        return contract_list

    def search_if_contract_has_event(self, session, result_contract_list2):
        """
        Fonction qui permet de retourner une liste de contrat n'ayant pas d'événement associé.
        :param session:
        :param result_contract_list2:
        :return: result_contract_list3
        """
        result_contract_list3 = []
        for r_contract_list2 in result_contract_list2:
            result_event = self.table_c.get_single_event_controller(session, r_contract_list2.contract_id)
            info_result_event = result_event.fetchone()
            if info_result_event is None:
                result_contract_list3.append(r_contract_list2)
        return result_contract_list3
