from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
from rich.table import Table

console = Console()


class UserView:
    def get_name_view(self):
        name = Prompt.ask("[bright_cyan]Nom [/bright_cyan]")
        return name

    def get_first_name_view(self):
        first_name = Prompt.ask("[bright_cyan]Prénom [/bright_cyan]")
        return first_name

    def get_email_view(self):
        email = Prompt.ask("[bright_cyan]Email [/bright_cyan]")
        return email

    def get_password_view(self):
        password = Prompt.ask("[bright_cyan]Password [/bright_cyan]")
        return password

    def get_role_view(self):
        role = Prompt.ask("[bright_cyan]Saisir le role du collaborateur [COM/GES/SUP] [/bright_cyan]")
        return role

    def error_message_empty_field_view(self):
        cadre = Panel(
            "\n[red]Le champ ne peut être vide, veuillez recommencer.[/red ]\n\n",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="spring_green1",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def error_message_field_contains_number(self):
        cadre = Panel(
            "\n[red]Le champ doit contenir que des lettres majuscules et minuscules, veuillez recommencer.[/red ]\n\n",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="spring_green1",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def error_message_choices_view(self):
        cadre = Panel(
            "\n[red]Vous devez saisir les valeurs suivantes [COM/GES/SUP].[/red ]\n\n",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="spring_green1",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def display_list_collaborator(self, result):
        table = Table(title="[bright_blue]Epic Events\nListe des collaborateurs[/bright_blue]", style="spring_green1")
        table.add_column("[bright_blue]ID[/bright_blue]", justify="center", style="bright_cyan")
        table.add_column("[bright_blue]Nom / Prénom[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]email[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Username[/bright_blue]", justify="left", style="bright_cyan")
        table.add_column("[bright_blue]Role ID[/bright_blue]", justify="center", style="bright_cyan")
        for row in result:
            table.add_row(f"{row.id}", f"{row.name} {row.first_name}", f"{row.email}", f"{row.username}",
                          f"{row.role_id}")
        console.print(table)

    def display_message_edit_collaborator_list(self):
        user_input = Prompt.ask("[bright_cyan]Souhaitez-vous modifier les informations d'un collaborateur "
                                "[Y/N] ?[/bright_cyan]")
        return user_input

    def display_error_message_edit_collaborator_list(self):
        cadre = Panel(
            "\n[red]Vous devez saisir les valeurs suivantes [Y/N].[/red ]\n\n",
            title="[deep_sky_blue1] Epic Events[/deep_sky_blue1]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="spring_green1",  # Style de la bordure
        )
        console.print(cadre, justify="left")
