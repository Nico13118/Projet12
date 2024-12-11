from rich.text import Text
from rich.console import Console
console = Console()


class ErrorMessagesView:
    def error_username_password_view(self):
        """
        Fonction qui permet d'afficher un message d'erreur suite à une erreur de saisie
        identifiant / mot de passe.
        """
        text = Text("Erreur !! Identifiant ou mot de passe incorrect.")
        text.stylize("bold red")
        console.print(text)

    def display_error_message_edit_collaborator_list(self):
        """
        Fonction qui permet d'afficher un message d'erreur indiquant à l'utilisateur de saisir
        les valeurs attendues.
        """
        text = Text("Erreur !! Vous devez saisir les valeurs suivantes [Y/N].")
        text.stylize("bold red")
        console.print(text)
