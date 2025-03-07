from rich.console import Console
from rich.table import Table
import os
console = Console()


class MenuView:
    def display_menu_gestion_view(self):
        table = Table(title="[deep_sky_blue1] Epic Events - Service Gestion[/deep_sky_blue1]", style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")
        
        table.add_row("\n1", "\nEnregistrer un collaborateur")
        table.add_row("\n2", "\nModifier un collaborateur")
        table.add_row("\n3", "\nSupprimer un collaborateur")
        table.add_row("\n4", "\nCréer un contrat client")
        table.add_row("\n5", "\nModifier un contrat client")
        table.add_row("\n6", "\nAfficher tous les événements (Modification)")
        table.add_row("\n7", "\nAfficher tous les clients (Lecture seule)")
        table.add_row("\n8", "\nAfficher tous les contrats (Lecture seule)")
        table.add_row("\n9", "\nAfficher tous les événements (Lecture seule)")
        table.add_row("\n10", "\nQuitter l'application\n")

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

    def display_edit_menu_of_a_customer_contract_view(self, result_contract):
        table = Table(title="[bright_blue]Epic Events\nModifier le contrat d'un client.[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Infos contrat[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Infos supplémentaires[/bright_blue]", justify="left", style="bright_cyan")
        infos = result_contract.fetchone()
        table.add_row(" ", " ", " ", f"Nom du client: {infos.custom_name} {infos.custom_first_name}")
        table.add_row(" ", " ", " ", f"Nom de l'entreprise: {infos.custom_company_name}")
        table.add_row(" ", " ", " ", f"N° Téléphone: {infos.custom_phone}")
        table.add_row(" ", " ", " ", f"Commercial: {infos.collab_name} {infos.collab_first_name}")
        table.add_row(" ", " ", " ", f"Date de création: {infos.contract_created_date}")
        table.add_row("1", "Modifier la description du contrat", f"{infos.contract_description}")
        table.add_row("2", "Modifier le prix du contrat", f"{infos.contract_total_price}")
        table.add_row("3", "Modifier le solde restant", f"{infos.contract_amount_remaining}")
        table.add_row("4", "Modifier le statut du contrat", f"{infos.contract_status_name}")
        table.add_row("5", "Quitter", "")

        console.print(table)

    def display_edit_menu_of_a_event_view(self, result_event):
        table = Table(title="[bright_blue]Epic Events\nModifier l'événement d'un contrat.[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Infos événement[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Infos supplémentaires[/bright_blue]", justify="left", style="bright_cyan")
        for row in result_event:
            table.add_row(" ", " ", " ", f"Nom du client: {row.custom_name} {row.custom_first_name}")
            table.add_row(" ", " ", " ", f"Email: {row.custom_email}")
            table.add_row(" ", " ", " ", f"Téléphone: {row.custom_phone}")
            table.add_row(" ", " ", " ", f"N° Événement: {row.custom_phone}")
            table.add_row(" ", " ", " ", f"N° Contrat: {row.custom_phone}")
            table.add_row(" ", " ", " ", f"Contact Support: {row.collab_name} {row.collab_first_name}")
            table.add_row("1", "Modifier la date et l'heure de début", f"{row.event_date_start}")
            table.add_row("2", "Modifier la date et l'heure de fin", f"{row.event_date_end}")
            table.add_row("3", "Modifier l'adresse de l'événement", f"{row.location}")
            table.add_row("4", "Modifier le nombre d'invités", f"{row.attendees}")
            table.add_row("5", "Modifier la note d'information", f"{row.notes}")
            table.add_row("6", "Quitter", "")

            console.print(table)

    def display_menu_commercial_view(self):
        table = Table(title="[deep_sky_blue1] Epic Events - Service Commercial[/deep_sky_blue1]", style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")

        table.add_row("\n1", "\nEnregistrer un client")
        table.add_row("\n2", "\nModifier un client")
        table.add_row("\n3", "\nAfficher tous les contrats (Modification)")
        table.add_row("\n4", "\nCréer un événement")
        table.add_row("\n5", "\nAfficher tous les clients (Lecture seule)")
        table.add_row("\n6", "\nAfficher tous les contrats (Lecture seule)")
        table.add_row("\n7", "\nAfficher tous les événements (Lecture seule)")
        table.add_row("\n8", "\nQuitter l'application\n")

        console.print(table)

    def display_menu_support_view(self):
        table = Table(title="[deep_sky_blue1] Epic Events - Service Support[/deep_sky_blue1]", style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")

        table.add_row("\n1", "\nModifier un événement")
        table.add_row("\n2", "\nAfficher tous les clients (Lecture seule)")
        table.add_row("\n3", "\nAfficher tous les contrats (Lecture seule)")
        table.add_row("\n4", "\nAfficher tous les événements (Lecture seule)")
        table.add_row("\n5", "\nQuitter l'application\n")

        console.print(table)

    def clear_terminal_view(self):
        os.system("cls")

    def ask_the_user_to_choose_how_to_display_contracts_view(self):
        table = Table(title="[bright_blue]Epic Events\nModifier le contrat d'un client.[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")

        table.add_row("\n1", "\nAfficher tous les contrats")
        table.add_row("\n2", "\nAfficher uniquement les contrats non signés")
        table.add_row("\n3", "\nAfficher uniquement les contrats non soldés")
        table.add_row("\n4", "\nRetourner au menu principal\n")

        console.print(table)

    def ask_the_user_to_choose_how_to_display_events_view(self):
        table = Table(title="[bright_blue]Epic Events\nModifier l'événement d'un contrat.[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]Choix[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Actions[/bright_blue]", justify="left", style="bright_cyan")

        table.add_row("\n1", "\nAfficher tous les événements")
        table.add_row("\n2", "\nAfficher uniquement les événements non associé")
        table.add_row("\n3", "\nRetourner au menu principal\n")

        console.print(table)
