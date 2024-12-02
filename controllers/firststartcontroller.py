import re
YES_RESPONSE = ["Y", "YES", "O", "OUI"]
NO_RESPONSE = ["N", "NO", 'NON']


class FirstStartController:
    def __init__(self, first_start_view, usercontroller, jsoncontroller, databasecontroller, tablecontroller):
        self.first_start_v = first_start_view
        self.user_c = usercontroller
        self.json_c = jsoncontroller
        self.database_c = databasecontroller
        self.table_c = tablecontroller

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
        self.user_c.start_create_user_controller(username, password)

    def username_password_controller(self):
        while True:
            result_username = self.first_start_v.get_username_view()
            result_password = self.first_start_v.get_password_view()
            connexion_test = self.user_c.test_username_password_controller(result_username, result_password)
            if connexion_test:
                break
            else:
                self.first_start_v.error_username_password_view()
        return result_username, result_password

    def get_database_name_controller(self):
        self.first_start_v.display_message_database_view()
        while True:
            # On demande à l'utilisateur de saisir le nom pour la base de données.
            input_database_name = self.first_start_v.get_database_name_view()
            # Controle la saisie de l'utilisateur
            x = re.findall(r"[+@=\\/*!^:;,><#-]", input_database_name)
            if x:
                # Si erreur, afficher un message d'erreur
                self.first_start_v.display_message_error_database_view(x)
            else:
                # Sinon, controle et remplacment les espaces dans le nom par des underscores si présent
                database_name = re.sub(r"\s", "_", input_database_name)
                # Demande à l'utilisateur de confirmer l'utilisation de ce nom pour la base de données
                user_response = self.check_user_response_controller(database_name)
                if user_response:
                    break
        return database_name

    def check_user_response_controller(self, database_name):
        get_confirm = self.first_start_v.get_confirm_created_database_view(database_name)
        x = get_confirm.upper()
        if x in YES_RESPONSE:
            return True
        if x in NO_RESPONSE:
            return False
        else:
            self.first_start_v.input_error_view()
            return False
