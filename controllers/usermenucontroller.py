class UserMenuController:
    def __init__(self, menuview, errormessagesview, userview, tablecontroller, usercontroller, checkuserinputcontroller,
                 databasecontroller):
        self.menu_view = menuview
        self.user_view = userview
        self.error_messages_v = errormessagesview
        self.table_c = tablecontroller
        self.user_c = usercontroller
        self.check_user_input_c = checkuserinputcontroller
        self.database_c = databasecontroller

    def assign_correct_menu_controller(self, username_password):
        username = username_password[0]
        password = username_password[1]
        info_user = self.table_c.get_information_for_all_collaborators_controller(username, password)
        for row in info_user:
            if row.role_id == 1:
                self.get_menu_commercial_controller()
            if row.role_id == 2:
                self.get_menu_gestion_controller(username, password)
            if row.role_id == 3:
                pass

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
            user_input = self.user_view.get_user_input_view()
            if not user_input:
                error = True
            else:
                if user_input == 1:  # Enregistrer un nouveau collaborateur
                    self.register_new_collaborator_controller(username, password)
                elif user_input == 2:  # Afficher la liste des collaborateurs
                    while True:
                        self.show_collaborator_list_controller(username, password)
                        # Demande si l'utilisateur souhaite modifier un collaborateur
                        response = self.ask_user_if_they_want_to_edit_collaborator()
                        if response:
                            # Demander à l'utilisateur de selectionner le collaborateur à modifier
                            user_id = self.ask_user_to_select_collaborator_controller(username, password)
                            self.edit_collaborator_info_controller(user_id, username, password)
                        else:
                            break

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

    def edit_collaborator_info_controller(self, user_id, username_admin, password_admin):
        """
        Fonction qui va gérer un menu afin de procéder à la modification d'informations d'un collaborateur.
        Selon le choix de l'utilisateur, d'autres fonctions sont appelés pour effectuer les changements.
        Les choix concernent la modification : nom, prénom, email, username et rôle

        :param user_id : Concerne l'id de l'utilisateur qui va recevoir les modifications.
        :param username_admin : Correspond à l'utilisateur qui procède aux modifications.
        :param password_admin : Correspond à l'utilisateur qui procède aux modifications.
        """
        while True:
            self.menu_view.clear_terminal_view()
            result_collaborator_info = self.table_c.get_single_collaborator_info_with_id_controller(user_id,
                                                                                                    username_admin,
                                                                                                    password_admin)
            # Affichage d'un menu avec plusieurs choix et les infos du collaborateur
            self.menu_view.display_edit_menu_of_a_collaborator_view(result_collaborator_info)
            # Demande à l'utilisateur quel champ modifier
            result_choice = self.ask_user_which_field_to_edit()

            if result_choice == 1:  # Modifier le nom
                result_input = self.user_c.get_name_controller()
                #  Enregistre le nouveau nom dans la table
                self.table_c.edit_collaborator_fields_controller(user_id, result_input, username_admin,
                                                                 password_admin, field='name')
                # Récupère l'ancien username
                old_username = self.get_old_username_controller(user_id, username_admin, password_admin)
                # Fonction qui récupère le nom et prénom pour créer le nouveau username.
                new_username = self.create_new_username_controller(user_id, username_admin, password_admin)
                if new_username != old_username:
                    # On change username dans mysql
                    self.database_c.change_username_in_mysql_controller(username_admin, password_admin,
                                                                        old_username, new_username)
                    # On enregistre dans la table le nouveau username
                    result_input = new_username
                    self.table_c.edit_collaborator_fields_controller(user_id, result_input, username_admin,
                                                                     password_admin, field="username")
            elif result_choice == 2:  # Modifier le prénom
                result_input = self.user_c.get_first_name_controller()
                #  Enregistre le nouveau prénom
                self.table_c.edit_collaborator_fields_controller(user_id, result_input, username_admin,
                                                                 password_admin, field='first_name')
                # Récupère l'ancien username
                old_username = self.get_old_username_controller(user_id, username_admin, password_admin)
                # Fonction qui récupère le nom et précom pour créer le nouveau username.
                new_username = self.create_new_username_controller(user_id, username_admin, password_admin)
                if new_username != old_username:
                    # On change username dans mysql
                    self.database_c.change_username_in_mysql_controller(username_admin, password_admin,
                                                                        old_username, new_username)
                    # On enregistre dans la table le nouveau username
                    result_input = new_username
                    self.table_c.edit_collaborator_fields_controller(user_id, result_input, username_admin,
                                                                     password_admin, field="username")
            elif result_choice == 3:  # Modifier l'email
                result_input = self.user_c.get_email_controller()
                self.table_c.edit_collaborator_fields_controller(user_id, result_input, username_admin,
                                                                 password_admin, field="email")

            elif result_choice == 4:  # Modifier le role
                self.change_collaborator_role(user_id, username_admin, password_admin)

            elif result_choice == 5:
                break

    def change_collaborator_role(self, user_id, username_admin, password_admin):
        username_delete = ""
        password_delete = ""
        result_collaborator_info = self.table_c.get_single_collaborator_info_with_id_controller(
            user_id, username_admin, password_admin)
        for infos in result_collaborator_info:
            username_delete = infos.username

        # On demande à l'utilisateur de saisir le nouveau rôle
        new_role = self.user_c.get_role_controller()
        int_role_id = self.user_c.get_role_id_controller(new_role)
        # Enregistrement du nouveau rôle dans la table collaborator
        self.table_c.edit_collaborator_fields_controller(user_id, int_role_id, username_admin,
                                                         password_admin, field='role_id')
        # Suppression de l'utilisateur dans la base MySQL
        self.database_c.delete_a_mysql_user_controller(username_admin, password_admin, username_delete)
        # Création d'un nouvel utilisateur MySQL
        if new_role == "COM":
            self.database_c.save_collaborator_com_in_mysql_controller(
                username_admin, password_admin, username_delete, password_delete)
        elif new_role == "GES":
            self.database_c.save_collaborator_ges_in_mysql_controller(
                username_admin, password_admin, username_delete, password_delete)
        elif new_role == "SUP":
            self.database_c.save_collaborator_sup_in_mysql_controller(
                username_admin, password_admin, username_delete, password_delete)

    def register_new_collaborator_controller(self, username, password):
        self.menu_view.clear_terminal_view()
        self.user_view.display_message_create_new_collaborator()
        self.user_c.start_create_user_controller(username, password)

    def show_collaborator_list_controller(self, username, password):
        """
        Fonction qui permet de récupérer la liste des collaborateurs puis transmet les informations à la vue
        pour être affichées.

        :param username:
        :param password:
        :return:
        """
        self.menu_view.clear_terminal_view()
        result = self.table_c.get_information_for_all_collaborators_controller(username, password)
        self.user_view.display_list_collaborator(result)

    def ask_user_if_they_want_to_edit_collaborator(self):
        """
        Fonction qui permet de demander à l'utilisateur s'il souhaite apporter une modification à un collaborateur.
        La reponse de l'utilisateur est contrôlé.

        :return: Y
        """
        while True:
            user_input = self.user_view.display_message_edit_collaborator_list()
            response = self.check_user_input_c.check_user_input_yes_no_controller(user_input)
            if response == "Y":
                return True
            elif response == "N":
                break
            else:
                self.error_messages_v.display_error_message_of_values_yes_and_no()

    def ask_user_to_select_collaborator_controller(self, username, password):
        """
        Fonction qui permet de demander à l'utilisateur de saisir l'id du collaborateur à modifier.
        On contrôle la saisie de l'utilisateur.

        :param username:
        :param password:
        :return:
        """
        while True:
            # On demande à l'utilisateur de saisir l'id du collaborateur à modifier
            user_id = self.user_view.get_collaborator_id_view()
            # Contrôle que la saisie soit bien un chiffre
            result = self.check_user_input_c.check_user_input_isdigit(user_id)
            if result:
                # Récupération de la liste des collaborateurs
                collaborator_list = self.table_c.get_information_for_all_collaborators_controller(username, password)
                # Vérifie que l'id du collaborateur est présent dans la liste
                collaborator_info = self.check_user_input_c.check_id_in_list_controller(collaborator_list,
                                                                                        int(user_id))
                if collaborator_info:
                    return user_id
                else:
                    self.error_messages_v.display_error_message_choice_view()
            else:
                self.error_messages_v.display_error_message_choice_view()

    def ask_user_which_field_to_edit(self):
        """
        Fonction qui permet de demander à l'utilisateur quel champ souhaite-t-il modifier.
        Un contrôle est effectué selon son choix.

        :return: result_choice
        """
        while True:
            result_choice = self.user_view.get_user_input_view()
            result_check = self.check_user_input_c.check_user_input_of_edit_collaborator_information_menu(result_choice)
            if result_check:
                break
            else:
                self.error_messages_v.display_error_message_choice_view()
        return result_choice

    def create_new_username_controller(self, user_id, username_admin, password_admin):
        """
        Fonction qui permet de gérer la création d'un nouvel identifiant de connexion.

        :param user_id :
        :param username_admin :
        :param password_admin :
        :return: new_username
        """
        result_collaborator_info = self.table_c.get_single_collaborator_info_with_id_controller(
            user_id, username_admin, password_admin)
        collaborator_name = ""
        collaborator_first_name = ""
        for info in result_collaborator_info:
            collaborator_name = info.name
            collaborator_first_name = info.first_name
        name_first_name = f"{collaborator_name} {collaborator_first_name}"
        new_username = self.user_c.get_username_controller(name_first_name)
        return new_username

    def get_old_username_controller(self, user_id, username_admin, password_admin):
        """
        Fonction qui permet de gérer la récupération de l'ancien identifiant de connexion.

        :param user_id :
        :param username_admin :
        :param password_admin :
        :return: old_username
        """
        result_collaborator_info = self.table_c.get_single_collaborator_info_with_id_controller(
            user_id, username_admin, password_admin)
        old_username = ""
        for info in result_collaborator_info:
            old_username = info.username
        return old_username
