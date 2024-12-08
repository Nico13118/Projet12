import re
YES_RESPONSE = ["Y", "YES", "O", "OUI"]
NO_RESPONSE = ["N", "NO", 'NON']


class CheckUserInputController:
    def check_user_input_yes_no_controller(self, user_input):
        """
        Fonction qui contrôle que la saisie correspond aux constantes.

        :param user_input:
        :return: Y / N
        """
        x = user_input.upper()
        if x in YES_RESPONSE:
            return "Y"
        elif x in NO_RESPONSE:
            return "N"

    def check_id_in_list_controller(self, info_list, user_input):
        """
        Fonction qui vérifie si l'id choisi est présent dans la liste.
        S'il y a une correspondance, l'information est retourné.

        :param info_list:
        :param user_input:
        :return: collaborator_info
        """
        result_info = [c for c in info_list if c.id == user_input]
        return result_info

    def check_user_input_isdigit(self, user_input):
        """
        Fonction qui contrôle que la saisie de l'utilisateur soit bien un chiffre.

        :param user_input:
        :return: True / False
        """
        x = user_input.isdigit()
        return x

    def search_is_alpha_controller(self, user_input1):
        """
        Fonction qui permet de vérifier que la saisie ne contient que des lettres
        : param user_input1:
        :return: True / False
        """
        user_input2 = re.sub(r"\s", "", user_input1)
        x = user_input2.isalpha()
        return x

    def check_user_input_of_edit_collaborator_information_menu(self, result_choice):
        if 1 <= result_choice <= 6:
            return True
