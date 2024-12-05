from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
import os
console = Console()


class MenuView:
    def display_menu_gestion_view(self):
        cadre = Panel(
            "\n[bright_cyan]1) Enregistrer un nouveau collaborateur[/bright_cyan]\n"
            "\n[bright_cyan]2) Afficher la liste des collaborateurs[/bright_cyan]\n"    
            "\n[bright_cyan]3) Créer un contrat[/bright_cyan]\n"
            "\n[bright_cyan]4) Afficher la liste des contrats[/bright_cyan]\n"
            "\n[bright_cyan]5) Afficher la liste des évènements (non associé)[/bright_cyan]\n"
            "\n[bright_cyan]6) Afficher tous les clients (Lecture seule)[/bright_cyan]\n"  
            "\n[bright_cyan]7) Afficher tous les contrats (Lecture seule)[/bright_cyan]\n"
            "\n[bright_cyan]8) Afficher tous les évènements (Lecture seule)[/bright_cyan]\n"
            "\n[bright_cyan]9) Quitter l'application [/bright_cyan]\n",
            title="[deep_sky_blue1] Epic Events Menu Gestion[/deep_sky_blue1]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="spring_green1",  # Style de la bordure
        )
        console.print(cadre, justify="left")

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

    def display_error_message_view(self):
        text = Text("Choix invalide, veuillez recommencer.")
        text.stylize("bold red")
        console.print(text)

    def get_user_input_view(self):
        user_input = Prompt.ask("[bright_cyan]Faite votre choix [/bright_cyan]")
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
