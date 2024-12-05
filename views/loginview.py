from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
console = Console()


class LoginView:
    def display_message_info_authentication(self):
        """
        Fonction qui permet d'afficher un panneau d'information afin d'expliquer à l'utilisateur
        comment s'authentifier
        """
        cadre = Panel(
            "\n[bright_cyan]Pour vous connecter, vous devez saisir le nom et prénom de l'utilisateur et mot de passe."
            "[/bright_cyan]\n"
            "\n[bright_cyan]Format attendu: dupont_henry[bright_cyan]\n",
            title="[deep_sky_blue1] Epic Events Connexion[deep_sky_blue1]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="spring_green1",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def get_username_view(self):
        """
        Fonction qui permet de récupérer la saisie utilisateur et de la retourner

        :return: username
        """
        username = Prompt.ask("[bright_cyan]Username [bright_cyan]")
        return username

    def get_password_view(self):
        """
        Fonction qui permet de récupérer la saisie utilisateur et de la retourner

        :return: password
        """
        password = Prompt.ask("[bright_cyan]Password [bright_cyan]")
        return password

