import random


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
        self.user_view.display_list_collaborator(result, session)

    def ask_user_if_they_want_to_delete_collaborator(self):
        """
        Fonction qui permet de demander à l'utilisateur s'il souhaite supprimer un collaborateur.
        La reponse de l'utilisateur est contrôlé.

        :return: True
        """
        while True:
            user_input_y_n = self.user_view.display_message_delete_collaborator_list()
            response = self.check_user_input_c.check_user_input_yes_no_controller(user_input_y_n)
            if response == "Y":
                return True
            elif response == "N":
                break
            else:
                self.error_messages_v.display_error_message_of_values_yes_and_no()

    def ask_user_if_they_want_to_edit_collaborator(self):
        """
        Fonction qui permet de demander à l'utilisateur s'il souhaite modifier un collaborateur.
        La reponse de l'utilisateur est contrôlé.

        :return: True
        """
        while True:
            user_input_y_n = self.user_view.display_message_edit_collaborator_list()
            response = self.check_user_input_c.check_user_input_yes_no_controller(user_input_y_n)
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
            user_id = self.user_view.get_collaborator_id_view()
            result = self.check_user_input_c.check_user_input_isdigit(user_id)
            if result:
                selected_user = self.table_c.get_single_collaborator_info_with_id_controller(user_id, session)
                infos = selected_user.fetchone()
                if infos.collab_id == int(user_id):
                    return infos.collab_id, infos.collab_username
                else:
                    self.error_messages_v.display_error_message_choice_view()
            else:
                self.error_messages_v.display_error_message_choice_view()

    def ask_user_which_field_to_edit(self):
        """
        Fonction qui permet de demander à l'utilisateur quel champ souhaite-t-il modifier.
        Deux contrôles sont effectués :

        1) Vérification d'une saisie vide
        2) Vérification que la saisie correspond aux choix du menu.

        :return: result_choice
        """
        while True:
            result_choice = self.user_view.get_user_input_view()
            if result_choice:
                if 1 <= result_choice <= 5:
                    break
                else:
                    self.error_messages_v.display_error_message_choice_view()
            else:
                self.error_messages_v.error_message_empty_field_view()
        return result_choice

    def create_new_username_controller(self, user_id, session):
        """
        Fonction qui permet de gérer la création d'un nouvel identifiant de connexion.

        :param user_id :
        :param session
        :return: new_username
        """
        result_collaborator_info = self.table_c.get_single_collaborator_info_with_id_controller(user_id, session)
        infos = result_collaborator_info.fetchone()
        new_username = self.user_c.get_username_controller(f"{infos.collab_name} {infos.collab_first_name}")
        return new_username

    def get_old_username_controller(self, user_id, session):
        """
        Fonction qui permet de gérer la récupération de l'ancien identifiant de connexion.

        :param user_id :
        :param session
        :return: old_username
        """
        result_collaborator_info = self.table_c.get_single_collaborator_info_with_id_controller(user_id, session)
        infos = result_collaborator_info.fetchone()
        old_username = infos.collab_username
        return old_username

    def change_collaborator_role(self, user_id, session):
        """
        Fonction qui gère la modification du role pour un collaborateur.
        :param user_id:
        :param session
        """
        result_collaborator_info = self.table_c.get_single_collaborator_info_with_id_controller(user_id, session)
        infos = result_collaborator_info.fetchone()
        # On demande à l'utilisateur de saisir le nouveau rôle
        new_role = self.user_c.get_role_controller()
        int_role_id = self.user_c.get_role_id_controller(new_role)
        # Enregistrement du nouveau rôle dans la table collaborator
        self.table_c.edit_a_field_in_table(session, user_id, new_value=int_role_id, table_name='collaborator',
                                           object_id='collab_id', field='role_id')
        # Suppression de l'utilisateur dans la base MySQL
        self.database_c.delete_a_mysql_user_controller(session, infos.collab_username)
        # Création d'un nouvel utilisateur MySQL
        if new_role == "COM":
            self.database_c.save_collaborator_com_in_mysql_controller(session, infos.collab_username,
                                                                      infos.collab_password)
        elif new_role == "GES":
            self.database_c.save_collaborator_ges_in_mysql_controller(session, infos.collab_username,
                                                                      infos.collab_password)
        elif new_role == "SUP":
            self.database_c.save_collaborator_sup_in_mysql_controller(session, infos.collab_username,
                                                                      infos.collab_password)

    def reassign_customers_to_commercials_controller(self, session):
        list_commercial_id = []
        # On récupère la liste des commerciaux
        result_commercial = self.table_c.get_list_commercial_controller(session)
        for result_com in result_commercial:
            list_commercial_id.append(result_com.collab_id)
        random.shuffle(list_commercial_id)
        # On récupère la liste des clients sans commeciaux
        result_customer = self.table_c.get_list_customers_without_commercial_controller(session)
        for result_custom in result_customer:
            for commercial_id in list_commercial_id:
                self.table_c.edit_a_field_in_table(
                    session, info_id=result_custom.custom_id, new_value=commercial_id, table_name='customer',
                    object_id='custom_id', field='collaborator_id')
