class MenuGestionController:
    def __init__(self, menuview, userview, errormessagesview, gestioncontroller, tablecontroller, usercontroller,
                 databasecontroller):
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
        error = ''
        while True:
            self.menu_view.clear_terminal_view()
            self.menu_view.display_menu_gestion_view()
            if error:
                if error == 'error_1':
                    self.error_messages_v.display_error_message_choice_view()
                elif error == 'error_2':
                    self.error_messages_v.display_message_error_no_collaborator()
                elif error == 'error_4':
                    self.error_messages_v.no_contracts_to_create_view()
                elif error == 'error_5':
                    self.error_messages_v.no_contract_to_display_view()
                elif error == 'error_6':
                    self.error_messages_v.no_events_to_display_view()
                elif error == 'error_7':
                    self.error_messages_v.no_customer_to_display_view()
                elif error == 'error_8':
                    self.error_messages_v.no_contract_to_display_view()
                elif error == 'error_9':
                    self.error_messages_v.no_events_to_display_view()
                error = ''
            user_input_choice_menu = self.user_view.get_user_input_view()

            if user_input_choice_menu == '1':  # Enregistrer un collaborateur
                self.gestion_c.register_new_collaborator_controller(session)

            elif user_input_choice_menu == '2':  # Modifier un collaborateur
                collab_list = self.user_c.get_collaborator_list_controller(session)
                if collab_list:
                    while True:
                        self.menu_view.clear_terminal_view()
                        self.user_view.display_list_collaborator(collab_list, session)
                        # Demande si l'utilisateur souhaite modifier un collaborateur
                        response_y_n = self.gestion_c.ask_user_if_they_want_to_edit_collaborator()
                        if response_y_n:
                            # Demander à l'utilisateur de selectionner le collaborateur à modifier
                            user_id_username = self.gestion_c.ask_user_to_select_collaborator_controller(collab_list)
                            if user_id_username:
                                self.edit_collaborator_info_controller(session, user_id=user_id_username)
                        else:
                            break
                else:
                    error = "error_2"

            elif user_input_choice_menu == '3':  # Supprimer un collaborateur
                while True:
                    self.gestion_c.show_collaborator_list_controller(session)
                    response_y_n = self.gestion_c.ask_user_if_they_want_to_delete_collaborator()
                    if response_y_n:
                        user_id_username = self.gestion_c.ask_user_to_select_collaborator_controller(session)
                        self.database_c.delete_a_mysql_user_controller(session, username=user_id_username)
                        self.table_c.delete_collaborator_in_table_controller(session, user_id=user_id_username)
                        self.gestion_c.reassign_customers_to_commercials_controller(session)
                        self.user_view.prompt_the_user_to_press_the_enter_key()
                    else:
                        break
            elif user_input_choice_menu == '4':  # Créer un contrat client
                self.menu_view.clear_terminal_view()
                # Récupérer la liste de tous les clients
                result = self.user_c.get_list_all_customer_controller(session)
                if result:
                    self.user_view.display_list_customer_view(result)
                    response = self.gestion_c.ask_user_if_wants_create_customer_contract_controller()
                    if response:  # Si Gestion souhaite créer un contrat
                        user_input_id = self.gestion_c.ask_user_to_select_customer_id_controller(result)
                        self.gestion_c.create_customer_contract_controller(session, user_input_id)
                else:
                    error = "error_4"

            elif user_input_choice_menu == '5':  # Modifier un contrat client
                self.menu_view.clear_terminal_view()
                result_contract = self.user_c.get_all_contract_controller(session)
                # Affiche tous les contrats
                if result_contract:
                    self.user_view.display_list_contract_view(result_contract, info_title="Liste des contrats")
                    result_response_y_n = self.user_c.ask_user_if_they_want_to_edit_contract()
                    if result_response_y_n:
                        contract_id = self.user_c.ask_user_to_select_customer_contract_controller(session)
                        self.user_c.edit_info_customer_contract_controller(session, contract_id)
                else:
                    error = "error_5"

            elif user_input_choice_menu == '6':  # Afficher tous les événements (Modification)
                self.menu_view.clear_terminal_view()
                result_event_list = self.user_c.get_all_event_controller(session)  # Récupère la liste complète
                if result_event_list:
                    self.ask_the_user_to_choose_how_to_display_event_controller(session)
                else:
                    error = "error_6"

            elif user_input_choice_menu == '7':  # Afficher tous les clients (Lecture seule)
                self.menu_view.clear_terminal_view()
                list_customer = self.user_c.get_list_all_customer_controller(session)
                if list_customer:
                    self.user_view.display_list_customer_view(list_customer)
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                else:
                    error = "error_7"

            elif user_input_choice_menu == '8':  # Afficher tous les contrats (Lecture seule)
                self.menu_view.clear_terminal_view()
                result_contract = self.user_c.get_all_contract_controller(session)
                if result_contract:
                    self.user_view.display_list_contract_view(result_contract, info_title="Liste des contrats")
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                else:
                    error = 'error_8'

            elif user_input_choice_menu == '9':  # Afficher tous les événements (Lecture seule)
                self.menu_view.clear_terminal_view()
                result_event = self.user_c.get_all_event_controller(session)
                if result_event:
                    list_collab_supp = self.user_c.get_support_collaborator_controller(session)
                    self.user_view.display_list_all_events_view(result_event, list_collab_supp,
                                                                info_title="Liste d'événements")
                    self.user_view.prompt_the_user_to_press_the_enter_to_return_main_menu()
                else:
                    error = 'error_9'

            elif user_input_choice_menu == '10':
                break
            else:
                error = 'error_1'

    def ask_the_user_to_choose_how_to_display_event_controller(self, session):
        """
        Fonction qui permet de gérer l'affichage de tous les événements, les événements non associés afin que
        l'utilisateur puisse assigner ou réassigner un événement à un collaborateur du support.
        :param session:
        """
        error = ''
        while True:
            self.menu_view.clear_terminal_view()
            self.menu_view.ask_the_user_to_choose_how_to_display_events_view()
            if error:
                if error == 'error_1':
                    self.error_messages_v.no_collaborator_support_to_display_view()
                elif error == 'error_2':
                    self.error_messages_v.no_events_to_display_view()
                elif error == 'error_3':
                    self.error_messages_v.display_error_message_choice_view()
                error = ''

            user_input = self.user_view.get_user_input_view()

            if user_input == '1':  # Afficher tous les événements
                self.menu_view.clear_terminal_view()
                result_event_list = self.user_c.get_all_event_controller(session)
                list_collab_supp = self.user_c.get_support_collaborator_controller(session)
                self.user_view.display_list_all_events_view(result_event_list, list_collab_supp=list_collab_supp,
                                                            info_title="Liste d'événements")
                # On demande s'il souhaite assigner ou réassigner un événement à un collaborateur du support
                result_response_y_n = \
                    self.user_c.ask_user_if_they_want_assign_reassign_event_to_a_collaborator_controller()
                if result_response_y_n:
                    if list_collab_supp:
                        #  L'utilisateur saisi l'id de l'événement et on vérifie qu'il correspond à celle de la liste.
                        user_input_event_id = self.user_c.ask_user_to_select_event_id_controller(result_event_list)
                        #  Afficher la liste des collaborateurs du support
                        self.user_view.display_list_collaborator(list_collab_supp, session)
                        #  Demande de selectionner le collaborateur.
                        result_user_id = self.gestion_c.ask_user_to_select_collaborator_controller(list_collab_supp)
                        if result_user_id:
                            self.table_c.edit_a_field_in_table(session,
                                                               table_name='event', field='collaborator_supp_id',
                                                               new_value=result_user_id, object_id='event_id',
                                                               info_id=user_input_event_id)
                    else:
                        error = 'error_1'

            elif user_input == '2':  # Afficher uniquement les événements non associés.
                self.menu_view.clear_terminal_view()
                result_event_list = self.user_c.get_event_without_support_controller(session)
                if result_event_list:
                    self.user_view.display_list_all_events_view(result_event_list, list_collab_supp=False,
                                                                info_title="Liste d'événements")
                    # On demande s'il souhaite assigner un événement à un collaborateur du support
                    result_response_y_n = self.user_c.ask_user_if_they_want_assign_event_to_a_collaborator_controller()
                    if result_response_y_n:
                        list_collab_supp = self.user_c.get_support_collaborator_controller(session)
                        if list_collab_supp:
                            # L'utilisateur saisi l'id de l'événement et on vérifie qu'il correspond à celle
                            # de la liste.
                            user_input_event_id = self.user_c.ask_user_to_select_event_id_controller(result_event_list)
                            #  Afficher la liste des collaborateurs du support
                            self.user_view.display_list_collaborator(list_collab_supp, session)
                            #  Demande de selectionner le collaborateur.
                            result_user_id = self.gestion_c.ask_user_to_select_collaborator_controller(list_collab_supp)
                            if result_user_id:
                                self.table_c.edit_a_field_in_table(session,
                                                                   table_name='event', field='collaborator_supp_id',
                                                                   new_value=result_user_id, object_id='event_id',
                                                                   info_id=user_input_event_id)
                        else:
                            error = 'error_1'
                else:
                    error = 'error_2'

            elif user_input == '3':  # Retourner au menu principal
                break
            else:
                error = 'error_3'

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
                self.table_c.edit_a_field_in_table(session, table_name='collaborator', field='collab_name',
                                                   new_value=new_name, object_id='collab_id', info_id=user_id)

                # Récupère l'ancien username
                old_username = self.gestion_c.get_old_username_controller(user_id, session)
                # Fonction qui récupère le nom et prénom pour créer le nouveau username.
                new_username = self.gestion_c.create_new_username_controller(user_id, session)
                if new_username != old_username:
                    # On change username dans mysql
                    self.database_c.change_username_in_mysql_controller(session, old_username, new_username)
                    # On enregistre dans la table le nouveau username
                    self.table_c.edit_a_field_in_table(session, table_name='collaborator', field='collab_username',
                                                       new_value=new_username, object_id='collab_id', info_id=user_id)

            elif result_choice == 2:  # Modifier le prénom
                new_first_name = self.user_c.get_first_name_controller()
                #  Enregistre le nouveau prénom
                self.table_c.edit_a_field_in_table(session, table_name='collaborator', field='collab_first_name',
                                                   new_value=new_first_name, object_id='collab_id', info_id=user_id)

                # Récupère l'ancien username
                old_username = self.gestion_c.get_old_username_controller(user_id, session)
                # Fonction qui récupère le nom et prénom pour créer le nouveau username.
                new_username = self.gestion_c.create_new_username_controller(user_id, session)
                if new_username != old_username:
                    # On change username dans mysql
                    self.database_c.change_username_in_mysql_controller(session, old_username, new_username)
                    # On enregistre dans la table le nouveau username
                    self.table_c.edit_a_field_in_table(session, table_name='collaborator', field='collab_username',
                                                       new_value=new_username, object_id='collab_id', info_id=user_id)

            elif result_choice == 3:  # Modifier l'email
                new_email = self.user_c.get_email_controller()
                self.table_c.edit_a_field_in_table(session, table_name='collaborator', field='collab_email',
                                                   new_value=new_email, object_id='collab_id', info_id=user_id)

            elif result_choice == 4:  # Modifier le role
                self.gestion_c.change_collaborator_role(user_id, session)
            elif result_choice == 5:
                break
