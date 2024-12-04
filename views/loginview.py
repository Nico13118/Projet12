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
            "\n[bold green]Pour vous connecter, vous devez saisir le nom et prénom de l'utilisateur et mot de passe."
            "[/bold green]\n"
            "\n[bold green]Format attendu: dupont_henry[/bold green]\n",
            title="[blue] Epic Events Connexion[/blue]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="green",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def get_username_view(self):
        """
        Fonction qui permet de récupérer la saisie utilisateur et de la retourner

        :return: username
        """
        username = Prompt.ask("[bold green]Username [/bold green]")
        return username

    def get_password_view(self):
        """
        Fonction qui permet de récupérer la saisie utilisateur et de la retourner

        :return: password
        """
        password = Prompt.ask("[bold green]Password [/bold green]")
        return password

