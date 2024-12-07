class UserMenuController:
    def __init__(self, menuview, userview, tablecontroller, usercontroller, checkuserinputcontroller):
        self.menu_view = menuview
        self.user_view = userview
        self.table_c = tablecontroller
        self.user_c = usercontroller
        self.check_user_input_c = checkuserinputcontroller

    def assign_correct_menu_controller(self, username_password):
        username = username_password[0]
        password = username_password[1]
        info_user = self.table_c.get_information_for_all_collaborators_controller(username, password)
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
                    self.register_new_collaborator_controller(username, password)
                elif user_input == 2:
                    # Afficher la liste des collaborateurs
                    self.show_collaborator_list_controller(username, password)
                    # demander à l'utilisateur s'il souhaite apporter des modifications à un collaborateur
                    response = self.ask_user_if_they_want_to_edit_collaborator()
                    if response == "Y":
                        # Demander à l'utilisateur de selectionner le collaborateur à modifier
                        self.ask_user_to_select_collaborator_controller(username, password)
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

    def register_new_collaborator_controller(self, username, password):
        self.menu_view.clear_terminal_view()
        self.menu_view.display_message_create_new_collaborator()
        self.user_c.start_create_user_controller(username, password)

    def show_collaborator_list_controller(self, username, password):
        self.menu_view.clear_terminal_view()
        result = self.table_c.get_information_for_all_collaborators_controller(username, password)
        self.user_view.display_list_collaborator(result)

    def ask_user_if_they_want_to_edit_collaborator(self):
        while True:
            user_input = self.user_view.display_message_edit_collaborator_list()
            response = self.check_user_input_c.check_user_input_yes_no_controller(user_input)
            if response == "Y":
                return response
            elif response == "N":
                break
            else:
                self.user_view.display_error_message_edit_collaborator_list()

    def ask_user_to_select_collaborator_controller(self, username, password):
        while True:
            # On demande à l'utilisateur de saisir l'id du collaborateur à modifier
            user_input = self.user_view.get_collaborator_id_view()
            # Contrôle que la saisie soit bien un chiffre
            result = self.check_user_input_c.check_user_input_isdigit(user_input)
            if result:
                # Récupération de la liste des collaborateurs
                collaborator_list = self.table_c.get_information_for_all_collaborators_controller(username, password)
                # Vérifie que l'id du collaborateur est présent dans la liste
                collaborator_info = self.check_user_input_c.check_id_in_list_controller(collaborator_list,
                                                                                        int(user_input))
                if collaborator_info:
                    return collaborator_info
                else:
                    self.user_view.display_error_message_choice_view()
            else:
                self.user_view.display_error_message_choice_view()
