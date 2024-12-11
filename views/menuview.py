from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.table import Table
import os
console = Console()


class MenuView:
    def display_menu_gestion_view(self):
        table = Table(title="[deep_sky_blue1] Epic Events - Gestion[/deep_sky_blue1]", style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")
        
        table.add_row("1", "Enregistrer un nouveau collaborateur\n")
        table.add_row("2", "Liste des collaborateurs et modification\n")
        table.add_row("3", "Liste des clients et création de contrat\n")
        table.add_row("4", "Liste des contrats et modification\n")
        table.add_row("5", "Liste des événements non attribués et modification\n")
        table.add_row("6", "Liste des événements attribués et modification\n")
        table.add_row("7", "Afficher tous les événements (Lecture seule)\n")
        table.add_row("8", "Quitter l'application\n")

        console.print(table)

    def display_edit_menu_of_a_collaborator_view(self, infos):
        table = Table(title="[bright_blue]Epic Events\nModifier les informations d'un collaborateur.[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Infos collaborateur[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Identifiant de connexion[/bright_blue]", justify="center", style="bright_cyan")
        for info in infos:
            table.add_row(" ", " ", " ", f"{info.username}")
            table.add_row("1", "Modifier le nom", f"{info.name}")
            table.add_row("2", "Modifier le prénom ", f"{info.first_name}")
            table.add_row("3", "Modifier l'email", f"{info.email}")
            table.add_row("4", "Modifier le role", f"{info.role_name}")
            table.add_row("5", "Quitter", "")

        console.print(table)

    def display_menu_commercial_view(self):
        cadre = Panel(
            "\n[bright_cyan]1) Enregistrer un nouveau client[/bright_cyan]\n"
            "\n[bright_cyan]2) Afficher ma liste de clients[/bright_cyan]\n"  
            "\n[bright_cyan]3) Afficher les contrats signé[/bright_cyan]\n"  
            "\n[bright_cyan]4) Afficher les contrats non signé[/bright_cyan]\n"
            "\n[bright_cyan]5) Afficher les contrats non réglé[/bright_cyan]\n"
            "\n[bright_cyan]6) Afficher tous les clients (Lecture seule)[/bright_cyan]\n"
            "\n[bright_cyan]7) Afficher tous les contrats (Lecture seule)[/bright_cyan]\n"
            "\n[bright_cyan]8) Afficher tous les évènements (Lecture seule)[/bright_cyan]\n"
            "\n[bright_cyan]9) Quitter l'application [/bright_cyan]\n",
            title="[deep_sky_blue1] Epic Events Menu Commercial[/deep_sky_blue1]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="spring_green1",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def display_error_message_choice_view(self):
        """Fonction déplacée dans userview, faire les changements dans le code"""
        text = Text("Choix invalide, veuillez recommencer.")
        text.stylize("bold red")
        console.print(text)

    def get_user_input_view(self):
        user_input = Prompt.ask("[bright_cyan]Faite votre choix[/bright_cyan]")
        return int(user_input)

    def clear_terminal_view(self):
        os.system("cls")

    def display_message_create_new_collaborator(self):
        cadre = Panel(
            "\n[bright_cyan]Veuillez saisir les informations du nouveau collaborateur.[/bright_cyan]\n",
            title="[deep_sky_blue1] Epic Events Enregistrement[/deep_sky_blue1]",
            expand=True,
            border_style="spring_green1",
        )
        console.print(cadre, justify="left")
