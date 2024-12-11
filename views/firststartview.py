from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
import os
console = Console()


class FirstStartView:
    def first_connection_message_view(self):
        cadre = Panel(
            "\n[red blink]Démarrage de l'application...[/red blink]\n\n"
            "[bright_cyan]Vous devez saisir l'identifiant et le mot de passe d'un compte [/bright_cyan] \n"
            "[bold yellow]administrateur MySQL[/bold yellow] [bright_cyan]afin de procéder à la création[/bright_cyan] "
            "[bright_cyan]de votre base de données.[/bright_cyan]",  # Texte stylisé avec Rich
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="spring_green1",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def display_message_database_view(self):
        os.system("cls")
        cadre = Panel(
            "\n[red blink]Création de la base de données...[/red blink]\n\n"
            "[bright_cyan]Veuillez saisir le nom de votre base de données que vous souhaitez utiliser.[/bright_cyan]\n"
            "[bright_cyan]Le nom peut être composé de lettres majuscules, minuscules et de chiffres.[/bright_cyan]\n"
            "[red]Seul le caractère underscore '_' est autorisé comme caractère spécial.\nLes autres caractères[/red]"
            "[red]spéciaux, ainsi que les espaces, sont interdits.[/red]",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",
            expand=True,
            border_style="spring_green1",
        )
        console.print(cadre, justify="left")

    def get_database_name_view(self):
        database_name = Prompt.ask("[bright_cyan]Entrer le nom de la base de données [/bright_cyan]")
        return database_name

    def get_confirm_created_database_view(self, database_name):
        user_response = Prompt.ask(
            f"[bright_cyan]Confirmer que vous souhaitez utiliser[/bright_cyan] [red]{database_name!r}[/red]"
            f"[bright_cyan]comme base de données ? ('Y', 'N')[/bright_cyan]")
        return user_response

    def display_message_create_user_gestion_view(self):
        os.system("cls")
        cadre = Panel(
            "\n[red blink]Création d'un collaborateur Gestion...[/red blink]\n\n"
            "[bright_cyan]Veuillez saisir les informations du collaborateur qui occupera le poste [/bright_cyan]\n"
            "[bright_cyan][Gestion] afin qu'il puisse procédéder à la création des autres [/bright_cyan]\n"
            "[bright_cyan]collaborateurs.[/bright_cyan]\n",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",
            expand=True,
            border_style="spring_green1",
        )
        console.print(cadre, justify="left")

    def display_message_end_of_setting_view(self):
        os.system("cls")
        cadre = Panel(
            "\n[red blink]Fin du paramétrage de base...[/red blink]\n\n"
            "[bright_cyan]Vous pouvez maintenant vous connecter à l'application.[/bright_cyan]\n",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",
            expand=True,
            border_style="spring_green1",
        )
        console.print(cadre, justify="left")
