from rich.prompt import Prompt
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
import os
console = Console()


class UserView:
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

    def display_list_collaborator(self, result):
        table = Table(title="[bright_blue]Epic Events\nListe des collaborateurs[/bright_blue]",
                      style="spring_green1")
        table.add_column("[bright_blue]ID[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Nom[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Prénom[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]email[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Username[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Role[/bright_blue]", justify="center", style="bright_cyan")
        for row in result:
            table.add_row(f"{row.collab_id}", f"{row.collab_name}", f"{row.collab_first_name}",
                          f"{row.collab_email}", f"{row.collab_username}", f"{row.role_name}")

        console.print(table)

    def display_message_edit_collaborator_list(self):
        user_input = Prompt.ask("[bright_cyan]Souhaitez-vous modifier les informations d'un collaborateur "
                                "[Y/N] ?[/bright_cyan]")
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

    def get_user_input_view(self):
        user_input = Prompt.ask("[bright_cyan]Faite votre choix[/bright_cyan]")
        return int(user_input)

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
