from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import os
console = Console()


class UserView:
    def __init__(self):
        self.session = None

    def display_message_info_authentication(self):
        """
        Fonction qui permet d'afficher un panneau d'information afin d'expliquer à l'utilisateur
        comment s'authentifier
        """
        os.system("cls")
        cadre = Panel(
            "\n[bright_cyan]Pour vous connecter, vous devez saisir le nom et prénom de l'utilisateur et mot de passe."
            "[/bright_cyan]\n"
            "\n[bright_cyan]Format attendu: dupont_henry[bright_cyan]\n",
            title="[deep_sky_blue1] Epic Events Connexion[deep_sky_blue1]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="spring_green1",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def get_username_view(self):
        """
        Fonction qui permet de récupérer la saisie utilisateur et de la retourner
        :return: username
        """
        username = Prompt.ask("[bright_cyan]Username [bright_cyan]")
        return username

    def get_name_view(self):
        name = Prompt.ask("[bright_cyan]Nom [/bright_cyan]")
        return name

    def get_first_name_view(self):
        first_name = Prompt.ask("[bright_cyan]Prénom [/bright_cyan]")
        return first_name

    def get_email_view(self):
        email = Prompt.ask("[bright_cyan]Email [/bright_cyan]")
        return email

    def get_number_phone_view(self):
        phone = Prompt.ask("[bright_cyan]Téléphone [/bright_cyan]")
        return phone

    def get_company_name_view(self):
        company_name = Prompt.ask("[bright_cyan]Nom de l'entreprise [/bright_cyan]")
        return company_name

    def get_password_view(self):
        password = Prompt.ask("[bright_cyan]Password [/bright_cyan]")
        return password

    def get_login_password_view(self):
        password = Prompt.ask("[bright_cyan]Password [/bright_cyan]", password=True)
        return password

    def get_role_view(self):
        role = Prompt.ask("[bright_cyan]Saisir le role du collaborateur [COM/GES/SUP] [/bright_cyan]")
        return role

    def display_list_collaborator(self, result, session):
        self.session = session
        table = Table(title="[bright_blue]Epic Events\nListe des collaborateurs[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]ID[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Nom[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Prénom[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]email[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Username[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Role[/bright_blue]", justify="center", style="bright_cyan")
        for row in result:
            if self.session.collab_id != row.collab_id:
                table.add_row(f"{row.collab_id}", f"{row.collab_name}", f"{row.collab_first_name}",
                              f"{row.collab_email}", f"{row.collab_username}", f"{row.role_name}")
        console.print(table)

    def display_message_edit_collaborator_list(self):
        user_input = Prompt.ask("[bright_cyan]Souhaitez-vous modifier les informations d'un collaborateur "
                                "[Y/N] ?[/bright_cyan]")
        return user_input

    def display_message_delete_collaborator_list(self):
        user_input = Prompt.ask("[bright_cyan]Souhaitez-vous supprimer un collaborateur [Y/N] ?[/bright_cyan]")
        return user_input
    
    def display_message_edit_customer_list_view(self):
        user_input = Prompt.ask("[bright_cyan]Souhaitez-vous consulter ou modifier une fiche client "
                                "[Y/N] ?[/bright_cyan]")
        return user_input

    def get_collaborator_id_view(self):
        user_input = Prompt.ask("[bright_cyan]Veuillez saisir l'id du collaborateur [/bright_cyan]")
        return user_input

    def get_customer_code_id_view(self):
        user_input = Prompt.ask("[bright_cyan]Veuillez saisir le N° Client [/bright_cyan]")
        return user_input

    def get_contract_id_view(self):
        user_input = Prompt.ask("[bright_cyan]Veuillez saisir le N° Contrat [/bright_cyan]")
        return user_input

    def display_list_customer_view(self, result_customer):
        table = Table(title="[bright_blue]Epic Events\nListe des clients[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]N° Client[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Nom du client[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Nom de l'entreprise[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Contact commercial[/bright_blue]", justify="left", style="bright_cyan")
        for row in result_customer:
            table.add_row(f"{row.custom_id}", f"{row.custom_name} {row.custom_first_name}",
                          f"{row.custom_company_name}", f"{row.collab_name} {row.collab_first_name}")
        console.print(table)

    def prompt_the_user_to_press_the_enter_key(self):
        return Prompt.ask("[bright_cyan]Appuyez sur la touche entrée de votre clavier pour continuer...[/bright_cyan]")

    def prompt_the_user_to_press_the_enter_to_return_main_menu(self):
        return Prompt.ask("[bright_cyan]Appuyez sur la touche entrée de votre clavier pour retourner au menu principal "
                          "...[/bright_cyan]")

    def get_user_input_view(self):
        user_input = Prompt.ask("[bright_cyan]Faite votre choix[/bright_cyan]")
        return user_input

    def display_message_create_new_collaborator(self):
        cadre = Panel(
            "\n[bright_cyan]Veuillez saisir les informations du nouveau collaborateur.[/bright_cyan]\n",
            title="[deep_sky_blue1] Epic Events Enregistrement[/deep_sky_blue1]",
            expand=True,
            border_style="spring_green1",
        )
        console.print(cadre, justify="left")

    def display_message_create_new_customer(self):
        cadre = Panel(
            "\n[bright_cyan]Veuillez saisir les informations du nouveau client.[/bright_cyan]\n",
            title="[deep_sky_blue1] Epic Events Enregistrement[/deep_sky_blue1]",
            expand=True,
            border_style="spring_green1",
        )
        console.print(cadre, justify="left")

    def display_message_create_customer_contract_view(self):
        user_input = Prompt.ask("[bright_cyan]Souhaitez-vous créer un contrat client [Y/N] ?[/bright_cyan]")
        return user_input

    def display_message_edit_customer_contract_view(self):
        user_input = Prompt.ask("[bright_cyan]Souhaitez-vous modifier un contrat client [Y/N] ?[/bright_cyan]")
        return user_input

    def get_contract_description_view(self):
        user_input = Prompt.ask("[bright_cyan]Veuillez saisir la description du contrat [/bright_cyan]")
        return user_input

    def get_contract_total_price_view(self):
        user_input = Prompt.ask("[bright_cyan]Veuillez saisir le prix total du contrat [/bright_cyan]")
        return user_input

    def get_contract_amount_remaining_view(self):
        user_input = Prompt.ask("[bright_cyan]Veuillez saisir le prix total restant à régler [/bright_cyan]")
        return user_input

    def display_list_contract_view(self, result, info_title):
        table = Table(title=f"[bright_blue]Epic Events\n{info_title}[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]N° Contrat[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Nom du client[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Nom de l'entrprise[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Date de création[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Statut du contrat[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Total TTC[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Reste à payer[/bright_blue]", justify="left", style="bright_cyan")
        for row in result:
            table.add_row(f"{row.contract_id}", f"{row.custom_name}" f" {row.custom_first_name}",
                          f"{row.custom_company_name}", f"{row.contract_created_date}", f"{row.contract_status_name}",
                          f"{row.contract_total_price} €", f"{row.contract_amount_remaining} €")
        console.print(table)

    def display_message_of_a_signed_contract_view(self):
        user_input = Prompt.ask("[bright_cyan]Modifier le statut du contrat: Confirmez que le contrat a bien été "
                                "signé [Y/N] ?[/bright_cyan]")
        return user_input

    def display_message_of_an_unsigned_contract_view(self):
        user_input = Prompt.ask("[bright_cyan]Modifier le statut du contrat: Confirmez que le contrat n'a pas été "
                                "signé [Y/N] ?[/bright_cyan]")
        return user_input

    def display_message_create_contract_event_view(self):
        user_input = Prompt.ask("[bright_cyan]Souhaitez-vous créer un événement pour un contrat client "
                                "[Y/N] ?[/bright_cyan]")
        return user_input

    def get_start_date_view(self):
        start_date = Prompt.ask("[bright_cyan]Veuillez saisir la date et l'heure du début de l'événement "
                                "<< Exemple : 31 Décembre 2025 18:00 >>[/bright_cyan]")
        return start_date

    def get_end_date_view(self):
        end_date = Prompt.ask("[bright_cyan]Veuillez saisir la date et l'heure de fin de l'événement"
                              "<< Exemple : 01 Janvier 2026 08:00 >>[/bright_cyan]")
        return end_date

    def get_location_view(self):
        info_location = Prompt.ask("[bright_cyan]Veuillez saisir l'adresse où se passera l'événement")
        return info_location

    def get_attendees_view(self):
        info_attendees = Prompt.ask("[bright_cyan]Veuillez saisir le nombre d'invités prévu pour cet événement")
        return info_attendees

    def get_notes_event_view(self):
        info_notes = Prompt.ask("[bright_cyan]Veuillez saisir une note d'information de cet événement")
        return info_notes

    def display_end_message_event_view(self):
        return Prompt.ask("[bright_cyan]Événement enregistré avec succès, appuyez sur la touche entrée de votre "
                          "clavier pour continuer...[/bright_cyan]")

    def display_list_all_events_view(self, result_event, list_collab_supp, info_title):
        table = Table(title=f"[bright_blue]Epic Events\n{info_title}[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]N° Événement[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]N° Contrat[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Nom du client[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Téléphone[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Contact Support[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Date de l'événement[/bright_blue]", justify="left", style="bright_cyan")
        for row in result_event:
            collab_supp = [c for c in list_collab_supp if c.collab_id == row.collaborator_supp_id]
            if collab_supp:
                name_collab = f"{collab_supp[0].collab_name} {collab_supp[0].collab_first_name}"
            else:
                name_collab = "Non attribué"
            table.add_row(f"{row.event_id}", f"{row.contract_id}", f"{row.custom_name} {row.custom_first_name}",
                          f"{row.custom_phone}", f"{name_collab}", f"{row.event_date_start}")
        console.print(table)

    def display_collaborator_event_list(self, result_event, info_title):
        table = Table(title=f"[bright_blue]Epic Events\n{info_title}[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]N° Événement[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]N° Contrat[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Nom du client[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Téléphone[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Contact Support[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Date de l'événement[/bright_blue]", justify="left", style="bright_cyan")
        for row in result_event:
            table.add_row(f"{row.event_id}", f"{row.contract_id}", f"{row.custom_name} {row.custom_first_name}",
                          f"{row.custom_phone}", f"{row.collab_name} {row.collab_first_name}",
                          f"{row.event_date_start}")
        console.print(table)
