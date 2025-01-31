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
                    self.error_messages_v.display_error_message_choice_view()
                elif error == 'error_4':
                    self.error_messages_v.no_events_to_display_view()
                error = ''

            user_input_choice_menu = self.user_view.get_user_input_view()

            if user_input_choice_menu == '1':  # Modifier un événement
                pass

            elif user_input_choice_menu == '2':  # Afficher tous les clients (Lecture seule)
                pass

            elif user_input_choice_menu == '3':  # Afficher tous les contrats (Lecture seule)
                pass

            elif user_input_choice_menu == '4':  # Afficher tous les événements (Lecture seule)
                self.menu_view.clear_terminal_view()
                result_event = self.user_c.get_all_event_controller(session)
                if result_event:
                    list_collab_supp = self.table_c.get_information_for_all_collaborators_controller(session)
                    self.user_view.display_list_all_events_view(result_event, list_collab_supp,
                                                                info_title="Liste d'événements")
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                else:
                    error = 'error_4'

            elif user_input_choice_menu == '5':  # Quitter l'application
                break

            else:
                error = 'error_1'
