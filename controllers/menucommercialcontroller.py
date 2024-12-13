class MenuCommercialController:
    def __init__(self, menuview, userview, errormessagesview, commercialcontroller):
        self.session = None
        self.menu_view = menuview
        self.user_view = userview
        self.error_messages_v = errormessagesview
        self.commercial_c = commercialcontroller

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
                elif user_input == 2:
                    pass
                elif user_input == 3:
                    pass
                elif user_input == 4:
                    pass
                elif user_input == 5:
                    pass
                elif user_input == 6:
                    pass
                elif user_input == 7:
                    pass
                elif user_input == 8:
                    pass
                elif user_input == 9:
                    pass
                elif user_input == 10:
                    pass
