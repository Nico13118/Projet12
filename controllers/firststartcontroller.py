import re


class FirstStartController:
    def __init__(self, firststartview, userview, errormessagesview, usercontroller, jsoncontroller, databasecontroller,
                 tablecontroller, checkuserinputcontroller):
        self.first_start_v = firststartview
        self.user_view = userview
        self.error_messages_v = errormessagesview
        self.user_c = usercontroller
        self.json_c = jsoncontroller
        self.database_c = databasecontroller
        self.table_c = tablecontroller
        self.check_user_input_c = checkuserinputcontroller

    def first_start_controller(self):
        self.first_start_v.first_connection_message_view()  # Affichage panneau d'information
        username_password = self.username_password_controller()  # L'utilisateur saisi ses identifiants
        username = username_password[0]
        password = username_password[1]
        database_name = self.get_database_name_controller()  # L'utilisateur saisi le nom de la bdd.
        self.json_c.create_json_info_file_controller(database_name)  # Création du fichier json
        self.database_c.create_databases_controller(username, password, database_name)  # Création de la bdd
        self.table_c.create_table_all_controller(username, password, database_name)  # Création de toutes les tables
        self.first_start_v.display_message_create_user_gestion_view()  # Panneau d'information création user Gestion
        self.user_c.start_create_user_controller(username, password)  # Création de l'utilisateur
        self.first_start_v.display_message_end_of_setting_view()
        self.user_view.prompt_the_user_to_press_the_enter_key()

    def username_password_controller(self):
        while True:
            result_username = self.user_view.get_username_view()
            result_password = self.user_view.get_login_password_view()
            connexion_test = self.database_c.test_username_password_controller(result_username, result_password)
            if connexion_test:
                break
            else:
                self.error_messages_v.error_username_password_view()
        return result_username, result_password

    def get_database_name_controller(self):
        self.first_start_v.display_message_database_view()
        while True:
            input_database_name = self.first_start_v.get_database_name_view()
            x = re.findall(r"[+@=\\/*!^:;,><#-]", input_database_name)
            if x:
                self.error_messages_v.display_message_error_database_view(x)
            else:
                # Sinon, controle et remplacment les espaces dans le nom par des underscores (si présent)
                database_name = re.sub(r"\s", "_", input_database_name)
                while True:
                    # Demande à l'utilisateur de confirmer l'utilisation de ce nom pour la base de données
                    user_input = self.first_start_v.get_confirm_created_database_view(database_name)
                    # Contrôle de la saisie utilisateur.
                    result = self.check_user_input_c.check_user_input_yes_no_controller(user_input)
                    if result == "Y":
                        break
                    elif result != "Y" or result != "N":
                        self.error_messages_v.input_error_view()
                return database_name

