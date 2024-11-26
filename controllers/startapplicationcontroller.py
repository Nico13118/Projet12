class StartApplicationController:
    def __init__(self, controller):
        self.controller = controller

    def start_application(self):
        """
        Fonction qui a pour but de contrôler si c'est la première connexion.
        Si première connexion :
            Création de la database et d'un utilisateur MySQL.
        Sinon l'utilisateur se connectera directement à l'application.
        """
        print("Hello World !")
