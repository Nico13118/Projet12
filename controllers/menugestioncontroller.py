class MenuGestionController:
    def __init__(self, menuview, userview, errormessagesview, gestioncontroller, tablecontroller, usercontroller,
                 databasecontroller):
        self.session = None
        self.menu_view = menuview
        self.user_view = userview
        self.error_messages_v = errormessagesview
        self.gestion_c = gestioncontroller
        self.table_c = tablecontroller
        self.user_c = usercontroller
        self.database_c = databasecontroller

    def get_menu_gestion_controller(self, session):
        """
        Fonction qui gère le menu princpal de Gestion

        :param session
        """
        error = False
        while True:
            self.menu_view.clear_terminal_view()
            self.menu_view.display_menu_gestion_view()
            if error:
                self.error_messages_v.display_error_message_choice_view()
                error = False
            user_input_choice_menu = self.user_view.get_user_input_view()
            if not user_input_choice_menu:
                error = True
            else:
                if user_input_choice_menu == 1:  # Enregistrer un nouveau collaborateur
                    self.gestion_c.register_new_collaborator_controller(session)

                elif user_input_choice_menu == 2:  # Afficher la liste des collaborateurs
                    while True:
                        self.gestion_c.show_collaborator_list_controller(session)
                        # Demande si l'utilisateur souhaite modifier un collaborateur
                        response_y_n = self.gestion_c.ask_user_if_they_want_to_edit_collaborator()
                        if response_y_n:
                            # Demander à l'utilisateur de selectionner le collaborateur à modifier
                            user_id_username = self.gestion_c.ask_user_to_select_collaborator_controller(session)
                            self.edit_collaborator_info_controller(session, user_id=user_id_username[0])
                        else:
                            break

                elif user_input_choice_menu == 3:  # Liste des collaborateurs et suppression
                    while True:
                        self.gestion_c.show_collaborator_list_controller(session)
                        response_y_n = self.gestion_c.ask_user_if_they_want_to_delete_collaborator()
                        if response_y_n:
                            user_id_username = self.gestion_c.ask_user_to_select_collaborator_controller(session)
                            self.database_c.delete_a_mysql_user_controller(session, username=user_id_username[1])
                            self.table_c.delete_collaborator_in_table_controller(session, user_id=user_id_username[0])
                            self.gestion_c.reassign_customers_to_commercials_controller(session)
                            self.user_view.prompt_the_user_to_press_the_enter_key()
                        else:
                            break
                elif user_input_choice_menu == 4:  # Liste des clients et création de contrat
                    while True:
                        self.user_c.show_customer_list_controller(session)
                        response = self.gestion_c.ask_user_if_wants_they_want_create_customer_contract_controller(
                            session)
                        if response:  # Si Gestion souhaite créer un contrat
                            self.gestion_c.create_customer_contract_controller(session)
                            break
                            
                elif user_input_choice_menu == 5:
                    pass

                elif user_input_choice_menu == 6:
                    pass

                elif user_input_choice_menu == 7:
                    pass

                elif user_input_choice_menu == 8:
                    pass

                elif user_input_choice_menu == 9:
                    pass

                elif user_input_choice_menu == 10:
                    pass

                elif user_input_choice_menu == 11:
                    pass

                elif user_input_choice_menu == 12:
                    break
                else:
                    error = True

    def edit_collaborator_info_controller(self, session, user_id):
        """
        Fonction qui va gérer un sous menu afin de procéder à la modification d'informations d'un collaborateur.
        Selon le choix de l'utilisateur, d'autres fonctions sont appelés pour effectuer les changements.
        Les choix concernent la modification : nom, prénom, email et rôle

        :param user_id : Concerne l'id de l'utilisateur qui va recevoir les modifications.
        :param session : Correspond à l'utilisateur qui procède aux modifications.

        """
        while True:
            self.menu_view.clear_terminal_view()
            result_collaborator_info = self.table_c.get_single_collaborator_info_with_id_controller(int(user_id),
                                                                                                    session)
            # Affichage d'un menu avec plusieurs choix et les infos du collaborateur
            self.menu_view.display_edit_menu_of_a_collaborator_view(result_collaborator_info)
            # Demande à l'utilisateur quel champ modifier
            result_choice = self.gestion_c.ask_user_which_field_to_edit()

            if result_choice == 1:  # Modifier le nom
                new_name = self.user_c.get_name_controller()
                #  Enregistre le nouveau nom dans la table
                self.table_c.edit_a_field_in_table(session, user_id, new_value=new_name, table_name='collaborator',
                                                   object_id='collab_id', field='collab_name')
                # Récupère l'ancien username
                old_username = self.gestion_c.get_old_username_controller(user_id, session)
                # Fonction qui récupère le nom et prénom pour créer le nouveau username.
                new_username = self.gestion_c.create_new_username_controller(user_id, session)
                if new_username != old_username:
                    # On change username dans mysql
                    self.database_c.change_username_in_mysql_controller(session, old_username, new_username)
                    # On enregistre dans la table le nouveau username
                    self.table_c.edit_a_field_in_table(session, user_id, new_value=new_username,
                                                       table_name='collaborator', object_id='collab_id',
                                                       field='collab_username')
            elif result_choice == 2:  # Modifier le prénom
                new_first_name = self.user_c.get_first_name_controller()
                #  Enregistre le nouveau prénom
                self.table_c.edit_a_field_in_table(session, user_id,
                                                   new_value=new_first_name, table_name='collaborator',
                                                   object_id='collab_id', field='collab_first_name')
                # Récupère l'ancien username
                old_username = self.gestion_c.get_old_username_controller(user_id, session)
                # Fonction qui récupère le nom et prénom pour créer le nouveau username.
                new_username = self.gestion_c.create_new_username_controller(user_id, session)
                if new_username != old_username:
                    # On change username dans mysql
                    self.database_c.change_username_in_mysql_controller(session, old_username, new_username)
                    # On enregistre dans la table le nouveau username
                    self.table_c.edit_a_field_in_table(session, user_id,
                                                       new_value=new_username, table_name='collaborator',
                                                       object_id='collab_id', field='collab_username')
            elif result_choice == 3:  # Modifier l'email
                new_email = self.user_c.get_email_controller()
                self.table_c.edit_a_field_in_table(session, user_id, new_value=new_email, table_name='collaborator',
                                                   object_id='collab_id', field='collab_email')
            elif result_choice == 4:  # Modifier le role
                self.gestion_c.change_collaborator_role(user_id, session)
            elif result_choice == 5:
                break
