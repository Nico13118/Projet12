import re
YES_RESPONSE = ["Y", "YES", "O", "OUI"]
NO_RESPONSE = ["N", "NO", 'NON']
ROLE = ["COM", "GES", "SUP"]


class CheckUserInputController:

    def __init__(self):
        self.session = None

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

    def check_user_input_role_controller(self, role):
        role = role.upper()
        if role in ROLE:
            return role
