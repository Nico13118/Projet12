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

    def ask_user_which_field_to_edit(self):
        """
        Fonction qui permet de demander à l'utilisateur quel champ souhaite-t-il modifier.
        Deux contrôles sont effectués :
        1) Vérification d'une saisie vide
        2) Vérification que la saisie correspond aux choix du menu.

        :return: result_choice
        """
        while True:
            result_choice = self.user_view.get_user_input_view()
            if result_choice:
                if 1 <= result_choice <= 6:
                    break
                else:
                    self.error_messages_v.display_error_message_choice_view()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return result_choice

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
