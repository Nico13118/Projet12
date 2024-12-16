from rich.console import Console
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
        table.add_row("\n3", "\nListe des collaborateurs et suppression")
        table.add_row("\n4", "\nListe des clients et création de contrat")
        table.add_row("\n5", "\nListe des contrats et modification")
        table.add_row("\n6", "\nListe des événements non attribués et modification")
        table.add_row("\n7", "\nListe des événements attribués et modification")
        table.add_row("\n8", "\nListe des événements")
        table.add_row("\n9", "\nListe des collaborateurs")
        table.add_row("\n10", "\nListe des clients")
        table.add_row("\n11", "\nListe des contrats")
        table.add_row("\n12", "\nQuitter l'application\n")

        console.print(table)

    def display_edit_menu_of_a_collaborator_view(self, infos):
        table = Table(title="[bright_blue]Epic Events\nModifier les informations d'un collaborateur.[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Infos collaborateur[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Identifiant de connexion[/bright_blue]", justify="center", style="bright_cyan")
        info = infos.fetchone()
        table.add_row(" ", " ", " ", f"{info.collab_username}")
        table.add_row("1", "Modifier le nom", f"{info.collab_name}")
        table.add_row("2", "Modifier le prénom ", f"{info.collab_first_name}")
        table.add_row("3", "Modifier l'email", f"{info.collab_email}")
        table.add_row("4", "Modifier le role", f"{info.role_name}")
        table.add_row("5", "Quitter", "")

        console.print(table)

    def display_edit_menu_of_a_customer_view(self, infos):
        table = Table(title="[bright_blue]Epic Events\nModifier les informations d'un client.[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Infos client[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Infos supplémentaires[/bright_blue]", justify="left", style="bright_cyan")
        info = infos.fetchone()
        table.add_row(" ", " ", " ", f"Commercial: {info.collab_name} {info.collab_first_name}")
        table.add_row(" ", " ", " ", f"Date de création: {info.custom_created_date}")
        table.add_row(" ", " ", " ", f"Dernière mise à jour: {info.custom_update_date}")
        table.add_row("1", "Modifier le nom", f"{info.custom_name}")
        table.add_row("2", "Modifier le prénom ", f"{info.custom_first_name}")
        table.add_row("3", "Modifier l'email", f"{info.custom_email}")
        table.add_row("4", "Modifier N° de télélphone", f"{info.custom_phone}")
        table.add_row("5", "Modifier intitulé de l'entreprise", f"{info.custom_company_name}")
        table.add_row("6", "Quitter", "")

        console.print(table)

    def display_menu_commercial_view(self):
        table = Table(title="[deep_sky_blue1] Epic Events - Service Commercial[/deep_sky_blue1]", style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")

        table.add_row("\n1", "\nEnregistrer un nouveau client")
        table.add_row("\n2", "\nListe des clients et modification")
        table.add_row("\n3", "\nListe des contrats non signés et modification")
        table.add_row("\n4", "\nListe des contrats non soldés et modification")
        table.add_row("\n5", "\nCréer un événement")
        table.add_row("\n6", "\nListe des événements")
        table.add_row("\n7", "\nListe des collaborateurs")
        table.add_row("\n8", "\nListe des clients")
        table.add_row("\n9", "\nListe des contrats")
        table.add_row("\n10", "\nQuitter l'application\n")

        console.print(table)

    def display_menu_support_view(self):
        table = Table(title="[deep_sky_blue1] Epic Events - Service Support[/deep_sky_blue1]", style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")

        table.add_row("\n1", "\nListe des événements et modification")
        table.add_row("\n2", "\nListe des événements")
        table.add_row("\n3", "\nListe des collaborateurs")
        table.add_row("\n4", "\nListe des clients")
        table.add_row("\n5", "\nListe des contrats")
        table.add_row("\n6", "\nQuitter l'application\n")

        console.print(table)

    def clear_terminal_view(self):
        os.system("cls")

