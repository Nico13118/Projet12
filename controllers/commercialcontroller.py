class CommercialController:
    def __init__(self, menuview, userview, usercontroller, tablecontroller):
        self.session = None
        self.menu_view = menuview
        self.user_view = userview
        self.user_c = usercontroller
        self.table_c = tablecontroller

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
        info_company_name = self.user_c.get_company_name_controller()

        self.table_c.save_customer_in_table_controller(session, info_name, info_first_name, info_email,
                                                       info_company_name)
