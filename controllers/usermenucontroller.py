class UserMenuController:
    def __init__(self, menuview, tablecontroller, usercontroller):
        self.menu_view = menuview
        self.table_c = tablecontroller
        self.user_c = usercontroller

    def assign_correct_menu_controller(self, username_password):
        username = username_password[0]
        password = username_password[1]
        info_user = self.table_c.get_info_collaborator(username, password)
        for row in info_user:
            if row.role_id == 1:
                self.get_menu_commercial_controller()
            if row.role_id == 2:
                self.get_menu_gestion_controller(username, password)
                print(f"role_id = {row.role_id}. type = {type(row.role_id)}")
            if row.role_id == 3:
                print(f"role_id = {row.role_id}. type = {type(row.role_id)}")

    def get_menu_commercial_controller(self):
        pass

    def get_menu_gestion_controller(self, username, password):
        error = False
        while True:
            self.menu_view.clear_terminal_view()
            self.menu_view.display_menu_gestion_view()
            if error:
                self.menu_view.display_error_message_view()
                error = False
            user_input = self.menu_view.get_user_input_view()

            if not user_input:
                error = True
            else:
                if user_input == 1:
                    self.menu_view.clear_terminal_view()
                    self.menu_view.display_message_create_new_collaborator()
                    self.user_c.start_create_user_controller(username, password)
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
                else:
                    error = True
