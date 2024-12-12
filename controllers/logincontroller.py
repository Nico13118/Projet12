class LoginController:
    def __init__(self, userview, errormessagesview, usercontroller, databasecontroller):
        self.user_view = userview
        self.error_messages_v = errormessagesview
        self.user_c = usercontroller
        self.database_c = databasecontroller
        
    def start_authentication_controller(self):
        """
        Fonction qui gère la récupération d'un username et password d'un utilisateur et fait appel à une
        fonction pour vérifier que l'utilisateur existe dans la base MySQL.

        :return: username , password
        """
        self.user_view.display_message_info_authentication()
        while True:
            username = self.user_view.get_username_view()
            password = self.user_view.get_login_password_view()
            control_authentication = self.database_c.test_username_password_controller(username, password)
            if not control_authentication:
                self.error_messages_v.error_username_password_view()
            else:
                break
        return username, password
