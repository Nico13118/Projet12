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
        error = ''
        while True:
            self.menu_view.clear_terminal_view()
            self.menu_view.display_menu_commercial_view()

            if error:
                if error == 'error_1':
                    self.error_messages_v.display_error_message_choice_view()
                elif error == 'error_2':
                    self.error_messages_v.no_customer_to_display_view()
                elif error == 'error_3':
                    self.error_messages_v.no_contract_to_display_view()
                elif error == 'error_4':
                    self.error_messages_v.no_events_to_create_view()
                elif error == 'error_5':
                    self.error_messages_v.no_customer_to_display_view()
                elif error == 'error_6':
                    self.error_messages_v.no_contract_to_display_view()
                elif error == 'error_7':
                    self.error_messages_v.no_events_to_display_view()
                error = ''

            user_input = self.user_view.get_user_input_view()
            if user_input == '1':  # Enregistrer un client.
                self.commercial_c.register_new_customer_controller(session)

            elif user_input == '2':  # Modifier un client
                while True:
                    self.menu_view.clear_terminal_view()
                    # Récupère la liste des clients associés au collaborateur
                    result_customer = self.commercial_c.get_customers_by_collaborator_controller(session)
                    if result_customer:
                        self.user_view.display_list_customer_view(result_customer)
                        response = self.commercial_c.ask_user_if_wants_they_want_to_edit_customer()
                        if response:
                            customer_id = self.commercial_c.ask_user_to_select_customer_controller(result_customer)
                            self.edit_customer_info_controller(customer_id, session)
                        else:
                            break
                    else:
                        error = 'error_2'
                        break

            elif user_input == '3':  # Afficher tous les contrats (Modification)
                self.menu_view.clear_terminal_view()
                result_contract_list = self.commercial_c.get_collaborator_contract_list(session)
                if result_contract_list:
                    self.ask_the_user_to_choose_how_to_display_contracts_controller(session)
                else:
                    error = 'error_3'

            elif user_input == '4':  # Créer un événement
                self.menu_view.clear_terminal_view()
                # Vérification qu'il y a un ou plusieurs contrats signés et soldés.
                result_contract_list1 = self.commercial_c.get_contract_signed_and_paid(session)
                if result_contract_list1:
                    # Permet de vérifier et retourner les contrats non associés à un événement.
                    result_contract_list2 = self.commercial_c.search_if_contract_has_event(session,
                                                                                           result_contract_list1)
                    if result_contract_list2:
                        info_title = "Liste de contrats disponibles pour créations d'événements"
                        self.user_view.display_list_contract_view(result_contract_list2, info_title=info_title)
                        response = self.commercial_c.ask_user_if_wants_create_event_contract_controller()
                        if response:
                            self.commercial_c.create_new_event_controller(session, result_contract_list2)
                    else:
                        error = 'error_4'
                else:
                    error = 'error_4'

            elif user_input == '5':  # Afficher tous les clients (Lecture seule)
                self.menu_view.clear_terminal_view()
                list_customer = self.user_c.get_list_all_customer_controller(session)
                if list_customer:
                    self.user_view.display_list_customer_view(list_customer)
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                else:
                    error = "error_5"

            elif user_input == '6':  # Afficher tous les contrats (Lecture seule)
                self.menu_view.clear_terminal_view()
                result_contract = self.user_c.get_all_contract_controller(session)
                if result_contract:
                    self.user_view.display_list_contract_view(result_contract, info_title="Liste des contrats")
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                else:
                    error = 'error_6'

            elif user_input == '7':  # Afficher tous les événements (Lecture seule)
                self.menu_view.clear_terminal_view()
                result_event = self.user_c.get_all_event_controller(session)
                if result_event:
                    list_collab_supp = self.table_c.get_information_for_all_collaborators_controller(session)
                    self.user_view.display_list_all_events_view(result_event, list_collab_supp,
                                                                info_title="Liste d'événements")
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                else:
                    error = 'error_7'

            elif user_input == '8':  # Quitter l'application
                break

            else:
                error = 'error_1'

    def edit_customer_info_controller(self, customer_id, session):
        """
        Fonction qui va gérer un sous menu afin de procéder à la modification d'informations d'un client.
        Selon le choix de l'utilisateur, d'autres fonctions sont appelés pour effectuer les changements.
        Les choix concernent la modification : nom, prénom, email, télélphone et intitulé de l'entreprise

        :param customer_id : Concerne l'id du client qui va recevoir les modifications.
        :param session : Correspond à l'utilisateur qui procède aux modifications.

                """
        error = False
        while True:
            self.menu_view.clear_terminal_view()
            result_customer_info = self.table_c.get_single_customer_info_with_id_controller(customer_id, session)
            self.menu_view.display_edit_menu_of_a_customer_view(result_customer_info)
            if error:
                self.error_messages_v.display_error_message_choice_view()
                error = False
            result_choice = self.user_view.get_user_input_view()

            if result_choice == '1':  # Modifier le nom
                new_name = self.user_c.get_name_controller()
                self.table_c.edit_a_field_in_table(session, table_name='customer', field='custom_name',
                                                   new_value=new_name, object_id='custom_id', info_id=customer_id)

            elif result_choice == '2':  # Modifier le prénom
                new_first_name = self.user_c.get_first_name_controller()
                self.table_c.edit_a_field_in_table(session, table_name='customer', field='custom_first_name',
                                                   new_value=new_first_name, object_id='custom_id', info_id=customer_id)

            elif result_choice == '3':  # Modifier l'email
                new_email = self.user_c.get_email_controller()
                self.table_c.edit_a_field_in_table(session, table_name='customer', field='custom_email',
                                                   new_value=new_email, object_id='custom_id', info_id=customer_id)

            elif result_choice == '4':  # Modifier N° de télélphone
                new_phone = self.user_c.get_number_phone_controller()
                self.table_c.edit_a_field_in_table(session, table_name='customer', field='custom_phone',
                                                   new_value=new_phone, object_id='custom_id', info_id=customer_id)

            elif result_choice == '5':  # Modifier intitulé de l'entreprise
                new_company_name = self.user_c.get_company_name_controller()
                self.table_c.edit_a_field_in_table(session, table_name='customer', field='custom_company_name',
                                                   new_value=new_company_name, object_id='custom_id',
                                                   info_id=customer_id)

            elif result_choice == '6':  # Quitter
                break

            else:
                error = True

    def ask_the_user_to_choose_how_to_display_contracts_controller(self, session):
        """
        Fonction qui permet de gérer un sous menu afin que l'utilisateur puisse avoir la possibilité
        d'afficher et modifier tous les contrats, les contrats non signés ou non soldés.

        :param session:
        """
        error = ''
        while True:
            self.menu_view.clear_terminal_view()
            self.menu_view.ask_the_user_to_choose_how_to_display_contracts_view()

            if error:
                if error == 'error_1':
                    self.error_messages_v.display_error_message_choice_view()
                elif error == 'error_2':
                    self.error_messages_v.no_contract_to_display_view()
                error = ''

            user_input = self.user_view.get_user_input_view()

            if user_input == '1':  # Afficher tous les contrats
                result_contract_list = self.commercial_c.get_collaborator_contract_list(session)
                self.menu_view.clear_terminal_view()
                self.user_view.display_list_contract_view(result_contract_list, info_title="Liste des contrats")
                result_response_y_n = self.user_c.ask_user_if_they_want_to_edit_contract()
                if result_response_y_n:
                    contract_id = self.user_c.ask_user_to_select_customer_contract_controller(result_contract_list)
                    self.user_c.edit_info_customer_contract_controller(session, contract_id)

            elif user_input == '2':  # Afficher seulement les contrats non signés
                result = self.commercial_c.get_unsigned_contracts(session)
                if result:
                    self.menu_view.clear_terminal_view()
                    self.user_view.display_list_contract_view(result, info_title="Liste des contrats non signés")
                    result_response_y_n = self.user_c.ask_user_if_they_want_to_edit_contract()
                    if result_response_y_n:
                        contract_id = self.user_c.ask_user_to_select_customer_contract_controller(result)
                        self.user_c.edit_info_customer_contract_controller(session, contract_id)
                else:
                    error = 'error_2'

            elif user_input == '3':  # Afficher seulement les contrats non soldés
                result = self.commercial_c.get_unpaid_contracts(session)
                if result:
                    self.menu_view.clear_terminal_view()
                    self.user_view.display_list_contract_view(result, info_title="Liste des contrats non soldés")
                    result_response_y_n = self.user_c.ask_user_if_they_want_to_edit_contract()
                    if result_response_y_n:
                        contract_id = self.user_c.ask_user_to_select_customer_contract_controller(result)
                        self.user_c.edit_info_customer_contract_controller(session, contract_id)

                else:
                    error = 'error_2'

            elif user_input == '4':  # Retourner au menu principal
                break

            else:
                error = 'error_1'
