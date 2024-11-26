from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
console = Console()


class FirstStartView:
    def first_connection_message_view(self):
        cadre = Panel(
            "\n[red blink]Démarrage de l'application...[/red blink]\n\n"
            "[bold wihte]Vous devez saisir l'identifiant et le mot de passe d'un compte [/bold wihte] \n"
            "[bold yellow]administrateur MySQL[/bold yellow] [bold wihte]afin de procéder à la création[/bold wihte] "
            "[bold wihte]de votre base de données.[/bold wihte]",  # Texte stylisé avec Rich
            title="[blue] Epic Events[/blue]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="red",  # Style de la bordure
        )

        console.print(cadre, justify="left")

    def get_username_view(self):
        username = Prompt.ask("[bold green]Username[/bold green]")
        return username

    def get_password_view(self):
        mdp = Prompt.ask("[bold green]Password[/bold green]", password=True)
        return mdp

    def error_username_password_view(self):
        console.clear()
        cadre = Panel(
            "\n[red blink]Erreur !! Identifiant ou mot de passe incorrect...[/red blink]\n\n"
            "[red]Veuillez recommencer.[/red]",
            title="[blue] Epic Events[/blue]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="red",  # Style de la bordure
        )
        console.print(cadre, justify="left")
        