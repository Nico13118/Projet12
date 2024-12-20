class MenuCommercialController:
    def __init__(self, menuview, userview, errormessagesview, commercialcontroller, tablecontroller, usercontroller):
        self.session = None
        self.menu_view = menuview
        self.user_view = userview
        self.error_messages_v = errormessagesview
        self.commercial_c = commercialcontroller
        self.table_c = tablecontroller
        self.user_c = usercontroller

    def get_menu_commercial_controller(self, session):
        """
        Fonction qui gère le menu principal du commercial.
        :param session:

        """
        error = False
        while True:
            self.menu_view.clear_terminal_view()
            self.menu_view.display_menu_commercial_view()
            if error:
                self.error_messages_v.display_error_message_choice_view()
                error = False
            user_input = self.user_view.get_user_input_view()
            if not user_input:
                error = True
            else:
                if user_input == 1:  # Enregistrer un nouveau client.
                    self.commercial_c.register_new_customer_controller(session)
                elif user_input == 2:  # Liste des clients et modification
                    while True:
                        self.user_c.show_customer_list_controller(session)
                        response = self.commercial_c.ask_user_if_wants_they_want_to_edit_customer()
                        if response:
                            customer_id = self.commercial_c.ask_user_to_select_customer_controller(session)
                            self.edit_customer_info_controller(customer_id, session)
                        else:
                            break
                elif user_input == 3:  # Modifier un contrat non signé
                    pass
                elif user_input == 4:  # Modifier un contrat non soldé
                    pass
                elif user_input == 5:  # Créer un événement
                    pass
                elif user_input == 6:  # Afficher tous les collaborateurs
                    list_collaborator = self.table_c.get_information_for_all_collaborators_controller(session)
                    self.user_view.display_list_collaborator(list_collaborator)
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()

                elif user_input == 7:  # Afficher tous les clients
                    list_customer = self.table_c.get_list_of_all_customers_controller(session)
                    self.user_view.display_list_customer_view(list_customer)
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                    
                elif user_input == 8:  # Afficher tous les contrats
                    self.menu_view.clear_terminal_view()
                    result_contract = self.table_c.get_all_contract_controller(session)
                    self.user_view.display_list_contract_view(result_contract)
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                elif user_input == 9:  # Afficher tous les événements
                    pass
                elif user_input == 10:
                    break
                    
                else:
                    error = True

    def edit_customer_info_controller(self, customer_id, session):
        """
        Fonction qui va gérer un sous menu afin de procéder à la modification d'informations d'un cllient.
        Selon le choix de l'utilisateur, d'autres fonctions sont appelés pour effectuer les changements.
        Les choix concernent la modification : nom, prénom, email, télélphone et intitulé de l'entreprise

        :param customer_id : Concerne l'id du client qui va recevoir les modifications.
        :param session : Correspond à l'utilisateur qui procède aux modifications.

                """
        while True:
            self.menu_view.clear_terminal_view()
            result_customer_info = self.table_c.get_single_customer_info_with_id_controller(customer_id, session)
            self.menu_view.display_edit_menu_of_a_customer_view(result_customer_info)
            result_choice = self.commercial_c.ask_user_which_field_to_edit()

            if result_choice == 1:  # Modifier le nom
                new_name = self.user_c.get_name_controller()
                self.table_c.edit_a_field_in_table(session, table_name='customer', field='custom_name',
                                                   new_value=new_name, object_id='custom_id', info_id=customer_id)

            if result_choice == 2:  # Modifier le prénom
                new_first_name = self.user_c.get_first_name_controller()
                self.table_c.edit_a_field_in_table(session, table_name='customer', field='custom_first_name',
                                                   new_value=new_first_name, object_id='custom_id', info_id=customer_id)

            if result_choice == 3:  # Modifier l'email
                new_email = self.user_c.get_email_controller()
                self.table_c.edit_a_field_in_table(session, table_name='customer', field='custom_email',
                                                   new_value=new_email, object_id='custom_id', info_id=customer_id)

            if result_choice == 4:  # Modifier N° de télélphone
                new_phone = self.user_c.get_number_phone_controller()
                self.table_c.edit_a_field_in_table(session, table_name='customer', field='custom_phone',
                                                   new_value=new_phone, object_id='custom_id', info_id=customer_id)

            if result_choice == 5:  # Modifier intitulé de l'entreprise
                new_company_name = self.user_c.get_company_name_controller()
                self.table_c.edit_a_field_in_table(session, table_name='customer', field='custom_company_name',
                                                   new_value=new_company_name, object_id='custom_id',
                                                   info_id=customer_id)
            if result_choice == 6:  #
                break
