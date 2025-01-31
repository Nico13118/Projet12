class MenuSupportController:
    def __init__(self, menuview, userview, errormessagesview):
        self.menu_view = menuview
        self.user_view = userview
        self.error_messages_v = errormessagesview

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
                error = ''

            user_input_choice_menu = self.user_view.get_user_input_view()

            if user_input_choice_menu == '1':  # Modifier un événement
                pass

            elif user_input_choice_menu == '2':  # Afficher tous les clients (Lecture seule)
                pass

            elif user_input_choice_menu == '3':  # Afficher tous les contrats (Lecture seule)
                pass

            elif user_input_choice_menu == '4':  # Afficher tous les événements (Lecture seule)
                pass

            elif user_input_choice_menu == '5':  # Quitter l'application
                break

            else:
                error = 'error_1'
