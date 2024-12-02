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

    def display_message_database_view(self):
        console.clear()
        cadre = Panel(
            "\n[red blink]Création de la base de données...[/red blink]\n\n"
            "[bold wihte]Veuillez saisir le nom de votre base de données que vous souhaitez utiliser.[/bold wihte]\n"
            "[bold wihte]Le nom peut être composé de lettres (majuscules et minuscules) et de chiffres.[/bold wihte]\n"
            "[red]Seul le caractère underscore '_' est autorisé comme caractère spécial. Les autres caractères[/red]\n"
            "[red]spéciaux, ainsi que les espaces, sont interdits.[/red]",
            title="[blue] Epic Events[/blue]",
            expand=True,
            border_style="red",
        )
        console.print(cadre, justify="left")

    def get_database_name_view(self):
        database_name = Prompt.ask("[green]Entrer le nom de la base de données [/green]")
        return database_name

    def get_confirm_created_database_view(self, database_name):
        user_response = Prompt.ask(f"[green]Confirmer que vous souhaitez utiliser [red]{database_name!r}[/red] comme "
                                   f"base de données ? ('Y', 'N')[/green]")
        return user_response


    def display_message_error_database_view(self, x):
        cadre = Panel(
            "\n[red blink]Erreur lors de la saisie du nom de la database.[/red blink]\n\n"
            f"[red]Vous ne pouvez pas utiliser le(s) caractère()s suivant(s): {x}[red]",
            title="[blue] Epic Events[/blue]",
            expand=True,
            border_style="red",
        )
        console.print(cadre, justify="left")

    def input_error_view(self):
        cadre = Panel(
            "\n[red]Erreur de saisie, veuillez recommencer.[/red ]\n\n",
            title="[blue] Epic Events[/blue]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="red",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def display_message_create_user_gestion_view(self):
        console.clear()
        cadre = Panel(
            "\n[red blink]Création d'un utilisateur MySQL'...[/red blink]\n\n"
            "[bold wihte]Veuillez saisir les informations de l'utilisateur qui aura les droits[/bold wihte]\n"
            "[bold wihte]de créer, modifier ou supprimer des utilisateurs dans l'application.[/bold wihte]\n",
            title="[blue] Epic Events[/blue]",
            expand=True,
            border_style="red",
        )
        console.print(cadre, justify="left")

