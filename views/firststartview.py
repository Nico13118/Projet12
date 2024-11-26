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


