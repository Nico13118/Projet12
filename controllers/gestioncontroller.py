class GestionController:
    def __init__(self, menuview, errormessagesview, userview, tablecontroller, usercontroller, checkuserinputcontroller,
                 databasecontroller):
        self.session = None
        self.menu_view = menuview
        self.user_view = userview
        self.error_messages_v = errormessagesview
        self.table_c = tablecontroller
        self.user_c = usercontroller
        self.check_user_input_c = checkuserinputcontroller
        self.database_c = databasecontroller

    def register_new_collaborator_controller(self, session):
        """
        Fonction qui permet d'enregistrer un nouveau collaborateur.
        :param session
        """

        self.menu_view.clear_terminal_view()
        self.user_view.display_message_create_new_collaborator()
        self.user_c.start_create_user_controller(session)

    def show_collaborator_list_controller(self, session):
        """
        Fonction qui permet de récupérer la liste des collaborateurs puis transmet les informations à la vue
        pour être affichées.

        :param session

        """
        self.menu_view.clear_terminal_view()
        result = self.table_c.get_information_for_all_collaborators_controller(session)
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

    def ask_user_to_select_collaborator_controller(self, session):
        """
        Fonction qui permet de demander à l'utilisateur de saisir l'id du collaborateur à modifier.
        On contrôle la saisie de l'utilisateur.

        :param session
        """
        while True:
            # On demande à l'utilisateur de saisir l'id du collaborateur à modifier
            user_id = self.user_view.get_collaborator_id_view()
            # Contrôle que la saisie soit bien un chiffre
            result = self.check_user_input_c.check_user_input_isdigit(user_id)
            if result:
                # Récupération de la liste des collaborateurs
                collaborator_list = self.table_c.get_information_for_all_collaborators_controller(session)
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

    def create_new_username_controller(self, user_id, session):
        """
        Fonction qui permet de gérer la création d'un nouvel identifiant de connexion.

        :param user_id :
        :param session
        :return: new_username
        """
        result_collaborator_info = self.table_c.get_single_collaborator_info_with_id_controller(user_id, session)
        collaborator_name = ""
        collaborator_first_name = ""
        for info in result_collaborator_info:
            collaborator_name = info.name
            collaborator_first_name = info.first_name
        name_first_name = f"{collaborator_name} {collaborator_first_name}"
        new_username = self.user_c.get_username_controller(name_first_name)
        return new_username

    def get_old_username_controller(self, user_id, session):
        """
        Fonction qui permet de gérer la récupération de l'ancien identifiant de connexion.

        :param user_id :
        :param session
        :return: old_username
        """
        result_collaborator_info = self.table_c.get_single_collaborator_info_with_id_controller(user_id, session)
        old_username = ""
        for info in result_collaborator_info:
            old_username = info.username
        return old_username

    def change_collaborator_role(self, user_id, session):
        """
        Fonction qui gère la modification du role pour un collaborateur.
        :param user_id:
        :param session
        """
        username_delete = ""
        password_delete = ""
        result_collaborator_info = self.table_c.get_single_collaborator_info_with_id_controller(user_id, session)
        for infos in result_collaborator_info:
            username_delete = infos.username

        # On demande à l'utilisateur de saisir le nouveau rôle
        new_role = self.user_c.get_role_controller()
        int_role_id = self.user_c.get_role_id_controller(new_role)
        # Enregistrement du nouveau rôle dans la table collaborator
        self.table_c.edit_collaborator_fields_controller(user_id, int_role_id, self.session, field='role_id')
        # Suppression de l'utilisateur dans la base MySQL
        self.database_c.delete_a_mysql_user_controller(self.session, username_delete)
        # Création d'un nouvel utilisateur MySQL
        if new_role == "COM":
            self.database_c.save_collaborator_com_in_mysql_controller(session, username_delete, password_delete)
        elif new_role == "GES":
            self.database_c.save_collaborator_ges_in_mysql_controller(session, username_delete, password_delete)
        elif new_role == "SUP":
            self.database_c.save_collaborator_sup_in_mysql_controller(session, username_delete, password_delete)
