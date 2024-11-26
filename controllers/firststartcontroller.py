class FirstStartController:
    def __init__(self, first_start_view, usercontroller):
        self.first_start_v = first_start_view
        self.user_c = usercontroller

    def first_start_controller(self):
        self.first_start_v.first_connection_message_view()
        list_username_password = self.username_password_controller()
        

    def username_password_controller(self):
        connexion_test = False
        while not connexion_test:
            result_username = self.first_start_v.get_username_view()
            result_password = self.first_start_v.get_password_view()
            connexion_test = self.user_c.test_username_password_controller(result_username, result_password)
            if connexion_test:
                return [result_username, result_password]
            else:
                self.first_start_v.error_username_password_view()

