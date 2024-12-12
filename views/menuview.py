from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.table import Table
import os
console = Console()


class MenuView:
    def display_menu_gestion_view(self):
        table = Table(title="[deep_sky_blue1] Epic Events - Service Gestion[/deep_sky_blue1]", style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")
        
        table.add_row("\n1", "\nEnregistrer un nouveau collaborateur")
        table.add_row("\n2", "\nListe des collaborateurs et modification")
        table.add_row("\n3", "\nListe des clients et création de contrat")
        table.add_row("\n4", "\nListe des contrats et modification")
        table.add_row("\n5", "\nListe des événements non attribués et modification")
        table.add_row("\n6", "\nListe des événements attribués et modification")
        table.add_row("\n7", "\nAfficher tous les événements (Lecture seule)")
        table.add_row("\n8", "\nQuitter l'application\n")

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
        table = Table(title="[deep_sky_blue1] Epic Events - Service Commercial[/deep_sky_blue1]", style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")

        table.add_row("\n1", "\nEnregistrer un nouveau client")
        table.add_row("\n2", "\nListe des clients et modification")
        table.add_row("\n3", "\nListe des contrats et modification")
        table.add_row("\n4", "\nVisualiser les contrats")
        table.add_row("\n5", "\nCréer un événement")
        table.add_row("\n8", "\nQuitter l'application\n")

        console.print(table)

    def clear_terminal_view(self):
        os.system("cls")

