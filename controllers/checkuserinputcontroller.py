import re
YES_RESPONSE = ["Y", "YES", "O", "OUI"]
NO_RESPONSE = ["N", "NO", 'NON']
ROLE = ["COM", "GES", "SUP"]


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
        """
        Fonction qui permet de contrôler que la saisie du role correspond à la liste de la constante ROLE.
        :param role:
        :return: role
        """
        role = role.upper()
        if role in ROLE:
            return role

    def check_input_length(self, user_input, max_length):
        """
        Fonction qui permet de contrôler que la saisie utilisateur ne dépasse pas la longueur autorisée.
        :param user_input:
        :param max_length:
        :return: Boolean
        """
        if len(user_input) <= max_length:
            return True
