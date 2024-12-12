class Session:
    def __init__(self, username, password, user_id):
        self.username = username
        self.password = password
        self.user_id = user_id


class LoginController:
    def __init__(self, userview, errormessagesview, usercontroller, databasecontroller, tablecontroller):
        self.user_view = userview
        self.error_messages_v = errormessagesview
        self.user_c = usercontroller
        self.database_c = databasecontroller
        self.table_c = tablecontroller
        
    def start_authentication_controller(self):
        """
        Fonction qui gère la récupération d'un username et password d'un utilisateur et fait appel à une
        fonction pour vérifier que l'utilisateur existe dans la base MySQL.

        :return: username , password
        """
        global info_user_id
        self.user_view.display_message_info_authentication()
        while True:
            username = self.user_view.get_username_view()
            password = self.user_view.get_login_password_view()
            control_authentication = self.database_c.test_username_password_controller(username, password)
            if not control_authentication:
                self.error_messages_v.error_username_password_view()
            else:
                break
        result = self.table_c.get_information_for_single_collaborator_controller(username, password)
        for row in result:
            info_user_id = row.collab_id
        return Session(username=username, password=password, user_id=info_user_id)
