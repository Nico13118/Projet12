from rich.panel import Panel
from rich.console import Console
from rich.prompt import Prompt
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

    def get_username_view(self):
        username = Prompt.ask("[bright_cyan]Username[/bright_cyan]")
        return username

    def get_password_view(self):
        mdp = Prompt.ask("[bright_cyan]Password[/bright_cyan]", password=True)
        return mdp

    def error_username_password_view(self):
        console.clear()
        cadre = Panel(
            "\n[red blink]Erreur !! Identifiant ou mot de passe incorrect...[/red blink]\n\n"
            "[red]Veuillez recommencer.[/red]",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="spring_green1",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def display_message_database_view(self):
        console.clear()
        cadre = Panel(
            "\n[red blink]Création de la base de données...[/red blink]\n\n"
            "[bright_cyan]Veuillez saisir le nom de votre base de données que vous souhaitez utiliser.[/bright_cyan]\n"
            "[bright_cyan]Le nom peut être composé de lettres majuscules, minuscules et de chiffres.[/bright_cyan]\n"
            "[red]Seul le caractère underscore '_' est autorisé comme caractère spécial. Les autres caractères[/red]\n"
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
            f"\n[bright_cyan]comme base de données ? ('Y', 'N')[/bright_cyan]")
        return user_response


    def display_message_error_database_view(self, x):
        cadre = Panel(
            "\n[red blink]Erreur lors de la saisie du nom de la database.[/red blink]\n\n"
            f"[red]Vous ne pouvez pas utiliser le(s) caractère()s suivant(s): {x}[red]",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",
            expand=True,
            border_style="spring_green1",
        )
        console.print(cadre, justify="left")

    def input_error_view(self):
        cadre = Panel(
            "\n[red]Erreur de saisie, veuillez recommencer.[/red ]\n\n",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="spring_green1",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def display_message_create_user_gestion_view(self):
        console.clear()
        cadre = Panel(
            "\n[red blink]Création d'un utilisateur MySQL'...[/red blink]\n\n"
            "[bright_cyan]Veuillez saisir les informations de l'utilisateur qui aura les droits[/bright_cyan]\n"
            "[bright_cyan]de créer, modifier ou supprimer des utilisateurs dans l'application.[/bright_cyan]\n",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",
            expand=True,
            border_style="spring_green1",
        )
        console.print(cadre, justify="left")

    def display_message_end_of_setting_view(self):
        console.clear()
        cadre = Panel(
            "\n[red blink]Fin du paramétrage de base...[/red blink]\n\n"
            "[bright_cyan]Vous pouvez maintenant vous connecter à l'application.[/bright_cyan]\n",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",
            expand=True,
            border_style="spring_green1",
        )
        console.print(cadre, justify="left")
