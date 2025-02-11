class MenuSupportController:
    def __init__(self, menuview, userview, errormessagesview, usercontroller, tablecontroller):
        self.menu_view = menuview
        self.user_view = userview
        self.error_messages_v = errormessagesview
        self.user_c = usercontroller
        self.table_c = tablecontroller

    def get_menu_support_controller(self, session):
        """
        Fonction qui gère le menu principal de support
        :param session:
        :return:
        """
        error = ''
        while True:
            self.menu_view.clear_terminal_view()
            self.menu_view.display_menu_support_view()
            if error:
                if error == 'error_1':
                    self.error_messages_v.no_events_to_display_view()
                elif error == 'error_2':
                    self.error_messages_v.no_customer_to_display_view()
                elif error == 'error_3':
                    self.error_messages_v.no_contract_to_display_view()
                elif error == 'error_4':
                    self.error_messages_v.no_events_to_display_view()
                elif error == 'error_6':
                    self.error_messages_v.display_error_message_choice_view()
                error = ''

            user_input_choice_menu = self.user_view.get_user_input_view()

            if user_input_choice_menu == '1':  # Modifier un événement
                self.menu_view.clear_terminal_view()
                # Récupération de la liste des événements qui concerne le callaborateur connecté.
                result_event1 = self.user_c.get_user_event_list_support_controller(session)
                if result_event1:
                    self.user_view.display_collaborator_event_list(result_event1, info_title="Liste d'événements")
                    #  On affiche la question s'il souhaite modifier un événement
                    result_response_y_n = self.user_c.ask_user_if_they_want_to_edit_event()
                    if result_response_y_n:
                        #  On vérifie que l'id de l'événement saisi par l'utilisateur correspond à celle de la liste
                        user_input_event_id = self.user_c.ask_user_to_select_event_id_controller(result_event1)
                        self.user_c.edit_info_event_contract_controller(session, user_input_event_id)

                else:
                    error = "error_1"

            elif user_input_choice_menu == '2':  # Afficher tous les clients (Lecture seule)
                self.menu_view.clear_terminal_view()
                list_customer = self.user_c.get_list_all_customer_controller(session)
                if list_customer:
                    self.user_view.display_list_customer_view(list_customer)
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                else:
                    error = "error_2"

            elif user_input_choice_menu == '3':  # Afficher tous les contrats (Lecture seule)
                self.menu_view.clear_terminal_view()
                result_contract = self.user_c.get_all_contract_controller(session)
                if result_contract:
                    self.user_view.display_list_contract_view(result_contract, info_title="Liste des contrats")
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                else:
                    error = 'error_3'

            elif user_input_choice_menu == '4':  # Afficher tous les événements (Lecture seule)
                self.menu_view.clear_terminal_view()
                all_event_result = self.user_c.get_all_event_controller(session)
                if all_event_result:
                    list_collab_supp = self.table_c.get_information_for_all_collaborators_controller(session)
                    self.user_view.display_list_all_events_view(all_event_result, list_collab_supp,
                                                                info_title="Liste d'événements")
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                else:
                    error = 'error_4'

            elif user_input_choice_menu == '5':  # Quitter l'application
                break

            else:
                error = 'error_6'
