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

    def display_error_message_of_values_yes_and_no(self):
        """
        Fonction qui permet d'afficher un message d'erreur indiquant à l'utilisateur de saisir
        les valeurs attendues.
        """
        text = Text("Erreur !! Vous devez saisir les valeurs suivantes [Y/N].")
        text.stylize("bold red")
        console.print(text)

    def display_error_message_choice_view(self):
        """
        Fonction qui permet d'afficher un message d'erreur lorsque l'utilisateur saisi
        une valeur inatendue.
        """
        text = Text("Choix invalide, veuillez recommencer.")
        text.stylize("bold red")
        console.print(text)

    def error_message_empty_field_view(self):
        """
        Fonction qui permet d'afficher un message d'erreur lorsque l'utilisateur valide
        un champ vide.
        """
        text = Text("Le champ ne peut être vide, veuillez recommencer.")
        text.stylize("bold red")
        console.print(text)
