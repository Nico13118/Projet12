from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console

console = Console()


class MenuView:
    def display_menu_gestion_view(self):
        cadre = Panel(
            "\n[bold green]1) Enregistrer un nouveau collaborateur[/bold green]\n"
            "\n[bold green]2) Afficher la liste des collaborateurs[/bold green]\n"  # Associers au commercial  
            "\n[bold green]3) Créer un contrat[/bold green]\n"
            "\n[bold green]4) Afficher la liste des contrats[/bold green]\n"
            "\n[bold green]5) Afficher la liste des évènements (non associé)[/bold green]\n"
            "\n[bold green]6) Afficher tous les clients (Lecture seule)[/bold green]\n"  # Associers au commercial
            "\n[bold green]7) Afficher tous les contrats (Lecture seule)[/bold green]\n"
            "\n[bold green]8) Afficher tous les évènements (Lecture seule)[/bold green]\n"
            "\n[bold green]9) Quitter l'application [/bold green]\n",
            title="[blue] Epic Events Menu Gestion[/blue]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="green",  # Style de la bordure
        )
        console.print(cadre, justify="left")
        user_input = Prompt.ask("[bold green]Faite votre choix [/bold green]")
        return user_input

    def display_menu_commercial_view(self):
        cadre = Panel(
            "\n[bold green]1) Enregistrer un nouveau client[/bold green]\n"
            "\n[bold green]2) Afficher ma liste de clients[/bold green]\n"  # Associers au commercial  
            "\n[bold green]3) Afficher les contrats signé[/bold green]\n"  
            "\n[bold green]4) Afficher les contrats non signé[/bold green]\n"
            "\n[bold green]5) Afficher les contrats non réglé[/bold green]\n"
            "\n[bold green]6) Afficher tous les clients (Lecture seule)[/bold green]\n"
            "\n[bold green]7) Afficher tous les contrats (Lecture seule)[/bold green]\n"
            "\n[bold green]8) Afficher tous les évènements (Lecture seule)[/bold green]\n"
            "\n[bold green]9) Quitter l'application [/bold green]\n",
            title="[blue] Epic Events Menu Commercial[/blue]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="green",  # Style de la bordure
        )
        console.print(cadre, justify="left")
        user_input = Prompt.ask("[bold green]Faite votre choix [/bold green]")
        return user_input
