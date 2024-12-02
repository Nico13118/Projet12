from rich.prompt import Prompt
from rich.panel import Panel
from rich.console import Console
console = Console()

class UserView:
    def get_name_view(self):
        name = Prompt.ask("[bold green]Nom [/bold green]")
        return name

    def get_first_name_view(self):
        first_name = Prompt.ask("[bold green]Prénom [/bold green]")
        return first_name

    def get_email_view(self):
        email = Prompt.ask("[bold green]Email [/bold green]")
        return email

    def get_password_view(self):
        password = Prompt.ask("[bold green]Password [/bold green]")
        return password

    def get_role_view(self):
        role = Prompt.ask("[bold green]Saisir le role du collaborateur [COM/GES/SUP] [/bold green]")
        return role

    def error_message_empty_field_view(self):
        cadre = Panel(
            "\n[red]Le champ ne peut être vide, veuillez recommencer.[/red ]\n\n",
            title="[blue] Epic Events[/blue]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="red",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def error_message_field_contains_number(self):
        cadre = Panel(
            "\n[red]Le champ doit contenir que des lettres majuscules et minuscules, veuillez recommencer.[/red ]\n\n",
            title="[blue] Epic Events[/blue]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="red",  # Style de la bordure
        )
        console.print(cadre, justify="left")

    def error_message_choices_view(self):
        cadre = Panel(
            "\n[red]Vous devez saisir les valeurs suivantes [COM/GES/SUP].[/red ]\n\n",
            title="[blue] Epic Events[/blue]",  # Titre du cadre (optionnel)
            expand=True,  # Le cadre prend toute la largeur du terminal
            border_style="red",  # Style de la bordure
        )
        console.print(cadre, justify="left")






