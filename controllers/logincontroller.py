class LoginController:
    def __init__(self, loginview, firststartview, usercontroller, databasecontroller):
        self.user_c = usercontroller
        self.login_v = loginview
        self.first_start_v = firststartview
        self.database_c = databasecontroller
        
    def start_authentication_controller(self):
        """
        Fonction qui gère la récupération d'un username et password d'un utilisateur et fait appel à une
        fonction pour vérifier que l'utilisateur existe dans la base MySQL.

        :return: username , password
        """
        self.login_v.display_message_info_authentication()
        while True:
            username = self.login_v.get_username_view()
            password = self.login_v.get_password_view()
            control_authentication = self.database_c.test_username_password_controller(username, password)
            if not control_authentication:
                self.first_start_v.error_username_password_view()
            else:
                break
        return username, password
